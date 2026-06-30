from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    codigo = Column(String(30), unique=True, nullable=False)