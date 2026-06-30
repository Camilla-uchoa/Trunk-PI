from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.auth_service import AuthService
from app.schemas.auth import LoginRequest, RegisterRequest, RecuperarSenhaRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/register", response_model=dict)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    user = service.register(
        nome=data.nome,
        email=data.email,
        senha=data.senha,
        perfil=data.perfil,
        curso=data.curso,
        pergunta_seguranca=data.pergunta_seguranca,
        resposta_seguranca=data.resposta_seguranca,
    )
    return {"message": "Usuário cadastrado com sucesso", "usuario": {"id": user.id, "nome": user.nome, "email": user.email}}


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login(email=data.email, senha=data.senha)


@router.post("/recuperar-senha")
def recuperar_senha(data: RecuperarSenhaRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.recuperar_senha(email=data.email, resposta_seguranca=data.resposta_seguranca, nova_senha=data.nova_senha)