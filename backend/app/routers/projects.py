from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.services.project_service import ProjectService
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse

router = APIRouter(prefix="/projects", tags=["Projetos"])


@router.get("/", response_model=list[ProjectResponse])
def list_projects(
    curso_id: Optional[int] = Query(None),
    periodo: Optional[str] = Query(None),
    orientador_id: Optional[int] = Query(None),
    status: Optional[str] = Query(None),
    equipe: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    service = ProjectService(db)
    filters = {k: v for k, v in {"curso_id": curso_id, "periodo": periodo, "orientador_id": orientador_id, "status": status, "equipe": equipe}.items() if v is not None}
    return service.list_all(filters)


@router.post("/", response_model=ProjectResponse, status_code=201)
def create_project(
    data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(db)
    return service.create(data.model_dump(), autor_id=current_user.id)


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    service = ProjectService(db)
    return service.get_by_id(project_id)


@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: int,
    data: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(db)
    return service.update(project_id, data.model_dump(exclude_none=True), current_user)


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(db)
    service.delete(project_id, current_user)
    return {"message": "Projeto removido"}