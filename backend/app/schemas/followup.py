from pydantic import BaseModel
from typing import Optional
from datetime import date


class FollowUpCreate(BaseModel):
    descricao: str
    tipo: str = "orientacao"


class FollowUpResponse(BaseModel):
    id: int
    project_id: int
    descricao: str
    tipo: str
    data: Optional[date] = None

    model_config = {"from_attributes": True}