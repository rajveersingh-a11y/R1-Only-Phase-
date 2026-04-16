from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.config import settings
import os

router = APIRouter()

@router.get("/download/{folder}/{filename}")
async def download_file(folder: str, filename: str):
    file_path = os.path.join(settings.OUTPUT_DIR, folder, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}