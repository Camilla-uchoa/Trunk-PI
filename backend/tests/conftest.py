import pytest
import tempfile
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import get_db
from app.models.base import Base


@pytest.fixture(scope="function")
def db_engine():
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    engine = create_engine(f"sqlite:///{tmp.name}", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    yield engine
    engine.dispose()
    os.unlink(tmp.name)


@pytest.fixture
def client(db_engine):
    TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

    def override_get_db():
        db = TestSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def user_token(client):
    client.post("/auth/register", json={"nome": "Teste", "email": "teste@teste.com", "senha": "123456", "perfil": "aluno"})
    resp = client.post("/auth/login", json={"email": "teste@teste.com", "senha": "123456"})
    return resp.json()["access_token"]


@pytest.fixture
def auth_header(user_token):
    return {"Authorization": f"Bearer {user_token}"}