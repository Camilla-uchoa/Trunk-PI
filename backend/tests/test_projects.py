def test_create_project(client, auth_header):
    resp = client.post("/projects/", json={"titulo": "Projeto Teste"}, headers=auth_header)
    assert resp.status_code == 201
    data = resp.json()
    assert data["titulo"] == "Projeto Teste"
    assert data["status"] == "em-desenvolvimento"


def test_list_projects(client, auth_header):
    client.post("/projects/", json={"titulo": "P1"}, headers=auth_header)
    client.post("/projects/", json={"titulo": "P2"}, headers=auth_header)
    resp = client.get("/projects/", headers=auth_header)
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 2


def test_get_project(client, auth_header):
    create = client.post("/projects/", json={"titulo": "Meu Projeto"}, headers=auth_header)
    pid = create.json()["id"]
    resp = client.get(f"/projects/{pid}", headers=auth_header)
    assert resp.status_code == 200
    assert resp.json()["titulo"] == "Meu Projeto"


def test_update_project(client, auth_header):
    create = client.post("/projects/", json={"titulo": "Original"}, headers=auth_header)
    pid = create.json()["id"]
    resp = client.put(f"/projects/{pid}", json={"titulo": "Atualizado"}, headers=auth_header)
    assert resp.status_code == 200
    assert resp.json()["titulo"] == "Atualizado"


def test_delete_project(client, auth_header):
    create = client.post("/projects/", json={"titulo": "Vai ser deletado"}, headers=auth_header)
    pid = create.json()["id"]
    resp = client.delete(f"/projects/{pid}", headers=auth_header)
    assert resp.status_code == 200
    assert resp.json()["message"] == "Projeto removido"


def test_filter_by_status(client, auth_header):
    client.post("/projects/", json={"titulo": "Em andamento"}, headers=auth_header)
    resp = client.get("/projects/?status=concluido", headers=auth_header)
    assert resp.status_code == 200
    assert len(resp.json()) == 0


def test_unauthorized_without_token(client):
    resp = client.get("/projects/")
    assert resp.status_code == 403