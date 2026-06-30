from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.services.evaluation_service import EvaluationService
from app.schemas.evaluation import EvaluationCreate, EvaluationResponse
from typing import List

router = APIRouter(prefix="/projects/{project_id}/evaluations", tags=["Avaliações"])


@router.get("/", response_model=List[EvaluationResponse])
def list_evaluations(
    project_id: int,
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    service = EvaluationService(db)
    return service.list_by_project(project_id)


@router.post("/", response_model=EvaluationResponse, status_code=201)
def add_evaluation(
    project_id: int,
    data: EvaluationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = EvaluationService(db)
    return service.add(project_id, current_user.id, nota=data.nota, parecer=data.parecer)