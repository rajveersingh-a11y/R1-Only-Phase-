from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

def calculate_metrics(features, labels):
    clean_mask = labels != -1
    metrics = {
        'silhouette_score': None,
        'davies_bouldin': None,
        'calinski_harabasz': None
    }
    
    if len(set(labels[clean_mask])) > 1:
        metrics['silhouette_score'] = float(silhouette_score(features[clean_mask], labels[clean_mask]))
        metrics['davies_bouldin'] = float(davies_bouldin_score(features[clean_mask], labels[clean_mask]))
        metrics['calinski_harabasz'] = float(calinski_harabasz_score(features[clean_mask], labels[clean_mask]))
        
    return metrics