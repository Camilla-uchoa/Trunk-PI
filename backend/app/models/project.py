from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    resumo = Column(Text, nullable=True)
    curso_id = Column(Integer, ForeignKey("courses.id"), nullable=True)
    periodo = Column(String(20), nullable=True)
    equipe = Column(String(500), nullable=True)
    orientador_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    area_tematica = Column(String(150), nullable=True)
    status = Column(String(30), default="em-desenvolvimento")
    autor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(Date, nullable=True)
    updated_at = Column(Date, nullable=True)

    curso = relationship("Course", lazy="joined")
    orientador = relationship("User", foreign_keys=[orientador_id], lazy="joined")
    autor = relationship("User", foreign_keys=[autor_id], lazy="joined")
    documentos = relationship("Document", back_populates="project", cascade="all, delete-orphan", lazy="joined")
    avaliacoes = relationship("Evaluation", back_populates="project", cascade="all, delete-orphan", lazy="joined")
    acompanhamentos = relationship("FollowUp", back_populates="project", cascade="all, delete-orphan", lazy="joined")