def test_register(client):
    resp = client.post("/auth/register", json={"nome": "Alice", "email": "alice@teste.com", "senha": "123456"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["message"] == "Usuário cadastrado com sucesso"
    assert data["usuario"]["email"] == "alice@teste.com"


def test_register_duplicate_email(client):
    client.post("/auth/register", json={"nome": "Alice", "email": "dup@teste.com", "senha": "123456"})
    resp = client.post("/auth/register", json={"nome": "Bob", "email": "dup@teste.com", "senha": "654321"})
    assert resp.status_code == 400
    assert "já cadastrado" in resp.json()["detail"]


def test_login(client):
    client.post("/auth/register", json={"nome": "Alice", "email": "alice@teste.com", "senha": "123456"})
    resp = client.post("/auth/login", json={"email": "alice@teste.com", "senha": "123456"})
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post("/auth/register", json={"nome": "Alice", "email": "alice@teste.com", "senha": "123456"})
    resp = client.post("/auth/login", json={"email": "alice@teste.com", "senha": "wrong"})
    assert resp.status_code == 401
    assert "inválidos" in resp.json()["detail"]


def test_recuperar_senha(client):
    client.post("/auth/register", json={
        "nome": "Alice", "email": "alice@teste.com", "senha": "123456",
        "pergunta_seguranca": "Cor favorita?", "resposta_seguranca": "Azul",
    })
    resp = client.post("/auth/recuperar-senha", json={
        "email": "alice@teste.com", "resposta_seguranca": "Azul", "nova_senha": "nova456",
    })
    assert resp.status_code == 200
    assert "redefinida" in resp.json()["message"]