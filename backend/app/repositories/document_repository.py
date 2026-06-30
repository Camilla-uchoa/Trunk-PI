from sqlalchemy.orm import Session
from app.models.document import Document
from typing import Optional, List


class DocumentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, doc_id: int) -> Optional[Document]:
        return self.db.query(Document).filter(Document.id == doc_id).first()

    def get_by_project(self, project_id: int) -> List[Document]:
        return self.db.query(Document).filter(Document.project_id == project_id).all()

    def create(self, doc: Document) -> Document:
        self.db.add(doc)
        self.db.commit()
        self.db.refresh(doc)
        return doc

    def delete(self, doc: Document) -> None:
        self.db.delete(doc)
        self.db.commit()