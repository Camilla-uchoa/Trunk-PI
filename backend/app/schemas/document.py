from pydantic import BaseModel
from typing import Optional
from datetime import date


class DocumentResponse(BaseModel):
    id: int
    project_id: int
    tipo: str
    nome_arquivo: str
    caminho: str
    data_upload: Optional[date] = None

    model_config = {"from_attributes": True}