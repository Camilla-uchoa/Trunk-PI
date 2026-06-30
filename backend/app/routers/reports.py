from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.services.report_service import ReportService

router = APIRouter(prefix="/reports", tags=["Relatórios"])


@router.get("/")
def generate_report(
    curso_id: Optional[int] = Query(None),
    periodo: Optional[str] = Query(None),
    orientador_id: Optional[int] = Query(None),
    status: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    service = ReportService(db)
    filters = {k: v for k, v in {"curso_id": curso_id, "periodo": periodo, "orientador_id": orientador_id, "status": status}.items() if v is not None}
    return service.generate(filters)