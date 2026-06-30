from sqlalchemy.orm import Session
from app.services.project_service import ProjectService


class ReportService:
    def __init__(self, db: Session):
        self.project_service = ProjectService(db)

    def generate(self, filters: dict) -> dict:
        return self.project_service.get_reports(filters)