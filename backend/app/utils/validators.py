from fastapi import HTTPException, UploadFile, status
from app.core.config import settings

FILE_EXTENSIONS = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".zip", ".rar", ".jpg", ".jpeg", ".png", ".txt"}


def validate_file_size(file: UploadFile) -> None:
    max_bytes = settings.max_upload_size_mb * 1024 * 1024
    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)
    if size > max_bytes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Arquivo excede o limite de {settings.max_upload_size_mb}MB",
        )