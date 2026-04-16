from pydantic import BaseModel
from typing import List, Dict, Optional

class UploadResponse(BaseModel):
    filename: str
    message: str

class MetricsResponse(BaseModel):
    total_consumers: int
    dbscan_clusters_found: int
    noise_points_count: int
    knn_reassigned_count: int
    phase_counts: Dict[str, int]
    silhouette_score: Optional[float]
    davies_bouldin: Optional[float]
    calinski_harabasz: Optional[float]

class RunResponse(BaseModel):
    message: str
    metrics: MetricsResponse
    output_paths: Dict[str, str]