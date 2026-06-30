from pydantic import BaseModel
from typing import Optional


class UserResponse(BaseModel):
    id: int
    nome: str
    email: str
    curso: Optional[str] = None
    perfil: str
    ativo: bool

    model_config = {"from_attributes": True}