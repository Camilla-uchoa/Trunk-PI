from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.services.document_service import DocumentService
from app.schemas.document import DocumentResponse
from typing import List

router = APIRouter(prefix="/projects/{project_id}/documents", tags=["Documentos"])


@router.get("/", response_model=List[DocumentResponse])
def list_documents(
    project_id: int,
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    service = DocumentService(db)
    return service.list_by_project(project_id)


@router.post("/", response_model=DocumentResponse, status_code=201)
def upload_document(
    project_id: int,
    tipo: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    service = DocumentService(db)
    return service.upload(project_id, tipo, file)