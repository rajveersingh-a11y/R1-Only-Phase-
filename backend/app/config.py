import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATA_DIR: str = "backend/app/data"
    OUTPUT_DIR: str = "backend/app/outputs"
    PCA_COMPONENTS: float = 0.95
    TSNE_PERPLEXITY: int = 30
    TSNE_ITER: int = 1000
    DBSCAN_EPS: float = 1.5
    DBSCAN_MIN_SAMPLES: int = 5
    KNN_NEIGHBORS: int = 3
    
    class Config:
        case_sensitive = True

settings = Settings()

os.makedirs(f"{settings.OUTPUT_DIR}/csv", exist_ok=True)
os.makedirs(f"{settings.OUTPUT_DIR}/plots", exist_ok=True)
os.makedirs(settings.DATA_DIR, exist_ok=True)