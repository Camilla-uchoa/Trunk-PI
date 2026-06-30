from sqlalchemy.orm import Session
from app.models.project import Project
from typing import Optional, List


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, project_id: int) -> Optional[Project]:
        return self.db.query(Project).filter(Project.id == project_id).first()

    def get_all(self, **filters) -> List[Project]:
        q = self.db.query(Project)
        for key, value in filters.items():
            if value is not None:
                q = q.filter(getattr(Project, key) == value)
        return q.order_by(Project.id.desc()).all()

    def create(self, project: Project) -> Project:
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def update(self, project: Project) -> Project:
        self.db.commit()
        self.db.refresh(project)
        return project

    def delete(self, project: Project) -> None:
        self.db.delete(project)
        self.db.commit()