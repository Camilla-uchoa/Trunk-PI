from pydantic import BaseModel
from typing import Optional
from datetime import date


class EvaluationCreate(BaseModel):
    nota: Optional[float] = None
    parecer: Optional[str] = None


class EvaluationResponse(BaseModel):
    id: int
    project_id: int
    avaliador_id: Optional[int] = None
    nota: Optional[float] = None
    parecer: Optional[str] = None
    data_avaliacao: Optional[date] = None

    model_config = {"from_attributes": True}