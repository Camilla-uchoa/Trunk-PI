from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.services.followup_service import FollowUpService
from app.schemas.followup import FollowUpCreate, FollowUpResponse
from typing import List

router = APIRouter(prefix="/projects/{project_id}/followups", tags=["Acompanhamentos"])


@router.get("/", response_model=List[FollowUpResponse])
def list_followups(
    project_id: int,
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    service = FollowUpService(db)
    return service.list_by_project(project_id)


@router.post("/", response_model=FollowUpResponse, status_code=201)
def add_followup(
    project_id: int,
    data: FollowUpCreate,
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    service = FollowUpService(db)
    return service.add(project_id, data.descricao, data.tipo)