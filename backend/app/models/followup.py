from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class FollowUp(Base):
    __tablename__ = "followups"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    descricao = Column(Text, nullable=False)
    tipo = Column(String(30), default="orientacao")
    data = Column(Date, nullable=True)

    project = relationship("Project", back_populates="acompanhamentos")