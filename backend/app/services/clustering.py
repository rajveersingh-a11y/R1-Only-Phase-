from sklearn.cluster import DBSCAN
from app.config import settings

def apply_dbscan(features):
    dbscan = DBSCAN(eps=settings.DBSCAN_EPS, min_samples=settings.DBSCAN_MIN_SAMPLES)
    labels = dbscan.fit_predict(features)
    return labels