from sqlalchemy import Column, Integer, String, Boolean
from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    curso = Column(String(100), nullable=True)
    perfil = Column(String(30), nullable=False, default="aluno")
    hash_senha = Column(String(255), nullable=False)
    pergunta_seguranca = Column(String(255), nullable=True)
    resposta_seguranca = Column(String(255), nullable=True)
    ativo = Column(Boolean, default=True)