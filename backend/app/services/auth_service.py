from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register(self, nome: str, email: str, senha: str, perfil: str = "aluno", curso: str = None, pergunta_seguranca: str = None, resposta_seguranca: str = None):
        if self.repo.get_by_email(email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado")
        user = User(
            nome=nome,
            email=email,
            curso=curso,
            perfil=perfil,
            hash_senha=hash_password(senha),
            pergunta_seguranca=pergunta_seguranca,
            resposta_seguranca=resposta_seguranca,
        )
        return self.repo.create(user)

    def login(self, email: str, senha: str):
        user = self.repo.get_by_email(email)
        if not user or not verify_password(senha, user.hash_senha):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou senha inválidos")
        if not user.ativo:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário inativo")
        token = create_access_token(data={"sub": str(user.id)})
        return {"access_token": token, "token_type": "bearer", "usuario": {"id": user.id, "nome": user.nome, "email": user.email, "perfil": user.perfil, "curso": user.curso}}

    def recuperar_senha(self, email: str, resposta_seguranca: str, nova_senha: str):
        user = self.repo.get_by_email(email)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        if not user.resposta_seguranca or user.resposta_seguranca.lower() != resposta_seguranca.lower():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Resposta de segurança incorreta")
        user.hash_senha = hash_password(nova_senha)
        self.repo.update(user)
        return {"message": "Senha redefinida com sucesso"}