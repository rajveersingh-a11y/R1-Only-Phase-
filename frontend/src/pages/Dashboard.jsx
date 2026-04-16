import React, { useState } from 'react';
import FileUpload from '../components/FileUpload';
import PipelineControls from '../components/PipelineControls';
import { getDownloadUrl } from '../api';

export default function Dashboard() {
  const [filename, setFilename] = useState(null);
  const [metrics, setMetrics] = useState(null);

  return (
    <div className="dashboard-grid">
      <aside className="sidebar">
        <FileUpload onUploadSuccess={setFilename} />
        <PipelineControls 
          filename={filename} 
          onAnalysisComplete={(m) => setMetrics(m)} 
        />
        
        {metrics && (
          <div className="card">
            <h2 className="card-title">Downloads</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              <a href={getDownloadUrl("csv", "final_phase_mapping.csv")} target="_blank" className="btn btn-secondary" download>
                📥 Download Mapping CSV
              </a>
              <a href={getDownloadUrl("csv", "tsne_embeddings.csv")} target="_blank" className="btn btn-secondary" download>
                📥 Download Embeddings
              </a>
              <a href={getDownloadUrl("plots", "tsne_dbscan_clusters.png")} target="_blank" className="btn btn-secondary" download>
                🖼️ Download Cluster Plot
              </a>
            </div>
          </div>
        )}
      </aside>

      <section className="content-area">
        {!metrics ? (
          <div className="card" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '400px', flexDirection: 'column', gap: '1rem', color: 'var(--text-muted)' }}>
            <div style={{ fontSize: '4rem', opacity: 0.5 }}>⚡</div>
            <h3>Waiting for data...</h3>
            <p>Upload a grid data file and run the analysis to see results.</p>
          </div>
        ) : (
          <>
            <div className="metrics-grid">
              <div className="metric-card">
                <span className="metric-label">Consumers Analyzed</span>
                <span className="metric-value">{metrics.total_consumers}</span>
              </div>
              <div className="metric-card success">
                <span className="metric-label">Clusters Found</span>
                <span className="metric-value">{metrics.dbscan_clusters_found}</span>
              </div>
              <div className="metric-card warning">
                <span className="metric-label">Noise / Reassigned</span>
                <span className="metric-value">{metrics.noise_points_count} / {metrics.knn_reassigned_count}</span>
              </div>
              <div className="metric-card accent">
                <span className="metric-label">Silhouette Score</span>
                <span className="metric-value">{metrics.silhouette_score ? metrics.silhouette_score.toFixed(3) : "N/A"}</span>
              </div>
            </div>

            <div className="results-grid">
              <div className="card">
                <h2 className="card-title">Cluster Visualization</h2>
                <div className="plot-container">
                  <img src={getDownloadUrl("plots", "tsne_dbscan_clusters.png")} alt="t-SNE Clusters" />
                </div>
              </div>
              
              <div className="card">
                <h2 className="card-title">Phase Distribution</h2>
                <div className="plot-container">
                  <img src={getDownloadUrl("plots", "final_phase_distribution.png")} alt="Phase Distribution" />
                </div>
                
                <div style={{ marginTop: '1.5rem', display: 'flex', gap: '1rem', justifyContent: 'center' }}>
                  {Object.entries(metrics.phase_counts).map(([phase, count]) => (
                    <div key={phase} style={{ textAlign: 'center', padding: '0.5rem 1rem', background: 'var(--bg-main)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border)' }}>
                      <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: '0.2rem' }}>Phase {phase}</div>
                      <div style={{ fontWeight: 'bold', fontSize: '1.2rem', color: 'var(--primary-light)' }}>{count}</div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </>
        )}
      </section>
    </div>
  );
}