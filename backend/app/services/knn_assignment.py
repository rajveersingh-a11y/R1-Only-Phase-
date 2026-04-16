from sklearn.neighbors import KNeighborsClassifier
from app.config import settings

def assign_noise_points(features, labels):
    noise_mask = labels == -1
    
    if not any(noise_mask):
        return labels, 0
        
    clean_mask = ~noise_mask
    
    if not any(clean_mask):
        return labels, sum(noise_mask)
        
    X_clean = features[clean_mask]
    y_clean = labels[clean_mask]
    
    knn = KNeighborsClassifier(n_neighbors=settings.KNN_NEIGHBORS)
    knn.fit(X_clean, y_clean)
    
    X_noise = features[noise_mask]
    new_labels = knn.predict(X_noise)
    
    final_labels = labels.copy()
    final_labels[noise_mask] = new_labels
    return final_labels, sum(noise_mask)