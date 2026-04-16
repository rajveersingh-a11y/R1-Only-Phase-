from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_upload, routes_phase_mapping, routes_results

app = FastAPI(title="Phase Mapping API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_upload.router)
app.include_router(routes_phase_mapping.router)
app.include_router(routes_results.router, prefix="/results")

@app.get("/")
def read_root():
    return {"message": "Phase Mapping API is running. Please access the frontend at http://localhost:5173"}

@app.get("/health")
def health_check():
    return {"status": "ok"}