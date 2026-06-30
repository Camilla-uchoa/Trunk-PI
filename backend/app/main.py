from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.core.cors import setup_cors
from app.routers import auth, users, projects, documents, evaluations, followup, reports, support, help

app = FastAPI(
    title="Trunk - API",
    description="Sistema de Gerenciamento de Projetos Integradores",
    version="1.0.0",
)

setup_cors(app)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(documents.router)
app.include_router(evaluations.router)
app.include_router(followup.router)
app.include_router(reports.router)
app.include_router(support.router)
app.include_router(help.router)

frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
if frontend_dir.is_dir():
    app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")