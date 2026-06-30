from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    tipo = Column(String(50), nullable=False)
    nome_arquivo = Column(String(255), nullable=False)
    caminho = Column(String(500), nullable=False)
    data_upload = Column(Date, nullable=True)

    project = relationship("Project", back_populates="documentos")