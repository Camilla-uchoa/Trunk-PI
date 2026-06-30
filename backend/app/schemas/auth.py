from pydantic import BaseModel
from typing import Optional


class LoginRequest(BaseModel):
    email: str
    senha: str


class RegisterRequest(BaseModel):
    nome: str
    email: str
    curso: Optional[str] = None
    perfil: str = "aluno"
    senha: str
    pergunta_seguranca: Optional[str] = None
    resposta_seguranca: Optional[str] = None


class RecuperarSenhaRequest(BaseModel):
    email: str
    resposta_seguranca: str
    nova_senha: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: dict