from fastapi import APIRouter, HTTPException
from app.config import settings
from app.schemas import RunResponse, MetricsResponse
from app.services.excel_reader import read_excel_file
from app.services.preprocessing import extract_and_align_time_series, standardize_data
from app.services.dimensionality_reduction import apply_pca, apply_tsne
from app.services.clustering import apply_dbscan
from app.services.knn_assignment import assign_noise_points
from app.services.phase_mapper import map_clusters_to_phases
from app.services.evaluation import calculate_metrics
from app.services.visualization import plot_tsne_clusters, plot_phase_distribution
import os
import pandas as pd
import numpy as np

router = APIRouter()

@router.post("/run-phase-mapping", response_model=RunResponse)
async def run_phase_mapping(filename: str):
    filepath = os.path.join(settings.DATA_DIR, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")
        
    try:
        meters_df, transformers_df, ground_truth_df = read_excel_file(filepath)
        m_ts, t_ts, meter_id_col, tf_id_col, common_ts = extract_and_align_time_series(meters_df, transformers_df, ground_truth_df)
        
        scaled_data = standardize_data(m_ts, common_ts)
        pca_features, explained_var = apply_pca(scaled_data)
        tsne_embeddings = apply_tsne(pca_features)
        
        dbscan_labels = apply_dbscan(tsne_embeddings)  
        final_labels, noise_count = assign_noise_points(tsne_embeddings, dbscan_labels)
        
        predicted_phases = map_clusters_to_phases(final_labels, ground_truth_df, m_ts[meter_id_col].values)
        
        metrics = calculate_metrics(tsne_embeddings, final_labels)
        
        pd.DataFrame(pca_features).to_csv(f"{settings.OUTPUT_DIR}/csv/pca_features.csv", index=False)
        pd.DataFrame(tsne_embeddings).to_csv(f"{settings.OUTPUT_DIR}/csv/tsne_embeddings.csv", index=False)
        pd.DataFrame({'cluster': dbscan_labels}).to_csv(f"{settings.OUTPUT_DIR}/csv/dbscan_labels.csv", index=False)
        
        final_df = pd.DataFrame({
            'consumer_id': m_ts[meter_id_col].values,
            'cluster_label_dbscan': dbscan_labels,
            'final_cluster_label': final_labels,
            'predicted_phase': predicted_phases
        })
        final_df.to_csv(f"{settings.OUTPUT_DIR}/csv/final_phase_mapping.csv", index=False)
        
        plot_tsne_clusters(tsne_embeddings, dbscan_labels, f"{settings.OUTPUT_DIR}/plots/tsne_dbscan_clusters.png")
        plot_phase_distribution(predicted_phases, f"{settings.OUTPUT_DIR}/plots/final_phase_distribution.png")
        
        # Convert NumPy types to native Python types
        phase_counts = final_df['predicted_phase'].value_counts().to_dict()
        phase_counts = {str(k): int(v) for k, v in phase_counts.items()}
        
        metrics_response = MetricsResponse(
            total_consumers=int(len(m_ts)),
            dbscan_clusters_found=int(len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)),
            noise_points_count=int(sum(dbscan_labels == -1)),
            knn_reassigned_count=int(noise_count),
            phase_counts=phase_counts,
            silhouette_score=metrics.get('silhouette_score'),
            davies_bouldin=metrics.get('davies_bouldin'),
            calinski_harabasz=metrics.get('calinski_harabasz')
        )
        
        return {
            "message": "Pipeline completed successfully",
            "metrics": metrics_response,
            "output_paths": {
                "csv": f"{settings.OUTPUT_DIR}/csv/",
                "plots": f"{settings.OUTPUT_DIR}/plots/"
            }
        }
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))