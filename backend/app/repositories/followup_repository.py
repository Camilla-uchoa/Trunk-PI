from sqlalchemy.orm import Session
from app.models.followup import FollowUp
from typing import List


class FollowUpRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_project(self, project_id: int) -> List[FollowUp]:
        return self.db.query(FollowUp).filter(FollowUp.project_id == project_id).order_by(FollowUp.id.desc()).all()

    def create(self, followup: FollowUp) -> FollowUp:
        self.db.add(followup)
        self.db.commit()
        self.db.refresh(followup)
        return followup