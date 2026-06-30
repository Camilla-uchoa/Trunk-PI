from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserResponse
from typing import List

router = APIRouter(prefix="/users", tags=["Usuários"])


@router.get("/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db), _=Depends(get_current_user)):
    repo = UserRepository(db)
    return repo.get_all()