import os
import shutil
from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.core.config import settings
from app.utils.validators import validate_file_size, FILE_EXTENSIONS
from datetime import date
from typing import List
from pathlib import Path


class DocumentService:
    def __init__(self, db: Session):
        self.repo = DocumentRepository(db)

    def upload(self, project_id: int, tipo: str, file: UploadFile) -> Document:
        if not file.filename:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Arquivo inválido")
        ext = Path(file.filename).suffix.lower()
        if ext not in FILE_EXTENSIONS:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Extensão {ext} não permitida")
        validate_file_size(file)

        upload_dir = Path(settings.upload_dir) / str(project_id)
        upload_dir.mkdir(parents=True, exist_ok=True)

        file_path = upload_dir / file.filename
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        doc = Document(
            project_id=project_id,
            tipo=tipo,
            nome_arquivo=file.filename,
            caminho=str(file_path),
            data_upload=date.today(),
        )
        return self.repo.create(doc)

    def list_by_project(self, project_id: int) -> List[Document]:
        return self.repo.get_by_project(project_id)

    def delete(self, doc_id: int) -> None:
        doc = self.repo.get_by_id(doc_id)
        if not doc:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Documento não encontrado")
        if os.path.exists(doc.caminho):
            os.remove(doc.caminho)
        self.repo.delete(doc)