import pandas as pd
from collections import Counter

def map_clusters_to_phases(final_labels, ground_truth_df, consumer_ids):
    df = pd.DataFrame({'consumer_id': consumer_ids, 'cluster': final_labels})
    
    gt_id_col = next((col for col in ground_truth_df.columns if 'meter' in col or 'consumer' in col), ground_truth_df.columns[0])
    phase_col = next((col for col in ground_truth_df.columns if 'phase' in col), None)
    
    mapping_dict = {}
    
    if phase_col and gt_id_col:
        merged = df.merge(ground_truth_df, left_on='consumer_id', right_on=gt_id_col, how='left')
        for cluster in set(final_labels):
            cluster_data = merged[merged['cluster'] == cluster]
            if not cluster_data[phase_col].dropna().empty:
                dominant_phase = cluster_data[phase_col].mode().iloc[0]
                mapping_dict[cluster] = dominant_phase
    
    available_phases = ['A', 'B', 'C']
    used_phases = list(mapping_dict.values())
    unused_phases = [p for p in available_phases if p not in used_phases]
    
    cluster_counts = Counter(final_labels)
    sorted_clusters = [c for c, _ in cluster_counts.most_common()]
    
    for c in sorted_clusters:
        if c not in mapping_dict:
            if unused_phases:
                mapping_dict[c] = unused_phases.pop(0)
            else:
                mapping_dict[c] = 'Unknown'
                
    predicted_phases = [mapping_dict.get(cl, 'Unknown') for cl in final_labels]
    
    return predicted_phases