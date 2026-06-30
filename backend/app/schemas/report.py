from pydantic import BaseModel
from typing import Optional


class ReportItem(BaseModel):
    id: int
    titulo: str
    curso: Optional[str] = None
    periodo: Optional[str] = None
    equipe: Optional[str] = None
    orientador: Optional[str] = None
    status: str
    media_nota: Optional[float] = None


class ReportResponse(BaseModel):
    total: int
    itens: list[ReportItem]