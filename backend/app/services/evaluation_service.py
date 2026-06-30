from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.evaluation import Evaluation
from app.repositories.evaluation_repository import EvaluationRepository
from datetime import date
from typing import List


class EvaluationService:
    def __init__(self, db: Session):
        self.repo = EvaluationRepository(db)

    def add(self, project_id: int, avaliador_id: int, nota: float = None, parecer: str = None) -> Evaluation:
        evaluation = Evaluation(
            project_id=project_id,
            avaliador_id=avaliador_id,
            nota=nota,
            parecer=parecer,
            data_avaliacao=date.today(),
        )
        return self.repo.create(evaluation)

    def list_by_project(self, project_id: int) -> List[Evaluation]:
        return self.repo.get_by_project(project_id)