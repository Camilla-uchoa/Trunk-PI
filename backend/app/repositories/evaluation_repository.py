from sqlalchemy.orm import Session
from app.models.evaluation import Evaluation
from typing import Optional, List


class EvaluationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_project(self, project_id: int) -> List[Evaluation]:
        return self.db.query(Evaluation).filter(Evaluation.project_id == project_id).all()

    def create(self, evaluation: Evaluation) -> Evaluation:
        self.db.add(evaluation)
        self.db.commit()
        self.db.refresh(evaluation)
        return evaluation