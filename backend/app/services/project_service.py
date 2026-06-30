from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from datetime import date
from typing import Optional, List


class ProjectService:
    def __init__(self, db: Session):
        self.repo = ProjectRepository(db)

    def _check_owner_or_admin(self, project: Project, current_user: User):
        if project.autor_id != current_user.id and current_user.perfil not in ("coordenador", "professor"):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Você não tem permissão para esta ação")

    def create(self, data: dict, autor_id: int) -> Project:
        project = Project(
            titulo=data["titulo"],
            resumo=data.get("resumo"),
            curso_id=data.get("curso_id"),
            periodo=data.get("periodo"),
            equipe=data.get("equipe"),
            orientador_id=data.get("orientador_id"),
            area_tematica=data.get("area_tematica"),
            status=data.get("status", "em-desenvolvimento"),
            autor_id=autor_id,
            created_at=date.today(),
            updated_at=date.today(),
        )
        return self.repo.create(project)

    def get_by_id(self, project_id: int) -> Project:
        project = self.repo.get_by_id(project_id)
        if not project:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Projeto não encontrado")
        return project

    def list_all(self, filters: dict) -> List[Project]:
        return self.repo.get_all(**filters)

    def update(self, project_id: int, data: dict, current_user: User) -> Project:
        project = self.get_by_id(project_id)
        self._check_owner_or_admin(project, current_user)
        for key, value in data.items():
            if value is not None:
                setattr(project, key, value)
        project.updated_at = date.today()
        return self.repo.update(project)

    def delete(self, project_id: int, current_user: User) -> None:
        project = self.get_by_id(project_id)
        self._check_owner_or_admin(project, current_user)
        self.repo.delete(project)

    def get_reports(self, filters: dict) -> dict:
        projects = self.repo.get_all(**filters)
        itens = []
        for p in projects:
            curso_nome = p.curso.nome if p.curso else None
            orientador_nome = p.orientador.nome if p.orientador else None
            notas = [av.nota for av in p.avaliacoes if av.nota is not None]
            media = round(sum(notas) / len(notas), 2) if notas else None
            itens.append({
                "id": p.id,
                "titulo": p.titulo,
                "curso": curso_nome,
                "periodo": p.periodo,
                "equipe": p.equipe,
                "orientador": orientador_nome,
                "status": p.status,
                "media_nota": media,
            })
        return {"total": len(itens), "itens": itens}