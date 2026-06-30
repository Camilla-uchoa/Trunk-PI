from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    avaliador_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    nota = Column(Float, nullable=True)
    parecer = Column(Text, nullable=True)
    data_avaliacao = Column(Date, nullable=True)

    project = relationship("Project", back_populates="avaliacoes")
    avaliador = relationship("User", lazy="joined")