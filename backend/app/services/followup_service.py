from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.followup import FollowUp
from app.repositories.followup_repository import FollowUpRepository
from datetime import date
from typing import List


class FollowUpService:
    def __init__(self, db: Session):
        self.repo = FollowUpRepository(db)

    def add(self, project_id: int, descricao: str, tipo: str = "orientacao") -> FollowUp:
        followup = FollowUp(
            project_id=project_id,
            descricao=descricao,
            tipo=tipo,
            data=date.today(),
        )
        return self.repo.create(followup)

    def list_by_project(self, project_id: int) -> List[FollowUp]:
        return self.repo.get_by_project(project_id)