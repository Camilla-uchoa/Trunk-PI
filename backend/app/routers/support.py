from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional


class ContactRequest(BaseModel):
    nome: str
    email: str
    assunto: str
    mensagem: str


router = APIRouter(prefix="/support", tags=["Suporte"])


@router.post("/contact")
def contact(data: ContactRequest):
    return {"message": f"Mensagem de {data.nome} recebida. Entraremos em contato em breve."}