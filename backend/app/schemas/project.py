from pydantic import BaseModel
from typing import Optional
from datetime import date


class ProjectCreate(BaseModel):
    titulo: str
    resumo: Optional[str] = None
    curso_id: Optional[int] = None
    periodo: Optional[str] = None
    equipe: Optional[str] = None
    orientador_id: Optional[int] = None
    area_tematica: Optional[str] = None
    status: str = "em-desenvolvimento"


class ProjectUpdate(BaseModel):
    titulo: Optional[str] = None
    resumo: Optional[str] = None
    curso_id: Optional[int] = None
    periodo: Optional[str] = None
    equipe: Optional[str] = None
    orientador_id: Optional[int] = None
    area_tematica: Optional[str] = None
    status: Optional[str] = None


class ProjectResponse(BaseModel):
    id: int
    titulo: str
    resumo: Optional[str] = None
    curso_id: Optional[int] = None
    periodo: Optional[str] = None
    equipe: Optional[str] = None
    orientador_id: Optional[int] = None
    area_tematica: Optional[str] = None
    status: str
    autor_id: int
    created_at: Optional[date] = None
    updated_at: Optional[date] = None

    model_config = {"from_attributes": True}