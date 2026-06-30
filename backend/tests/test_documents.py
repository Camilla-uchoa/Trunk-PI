import io


def test_upload_document(client, auth_header):
    create = client.post("/projects/", json={"titulo": "P Documentos"}, headers=auth_header)
    pid = create.json()["id"]
    resp = client.post(
        f"/projects/{pid}/documents/",
        data={"tipo": "monografia"},
        files={"file": ("teste.pdf", io.BytesIO(b"conteudo"), "application/pdf")},
        headers=auth_header,
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["nome_arquivo"] == "teste.pdf"
    assert data["project_id"] == pid


def test_list_documents(client, auth_header):
    create = client.post("/projects/", json={"titulo": "P Docs"}, headers=auth_header)
    pid = create.json()["id"]
    client.post(
        f"/projects/{pid}/documents/",
        data={"tipo": "monografia"},
        files={"file": ("doc1.pdf", io.BytesIO(b"um"), "application/pdf")},
        headers=auth_header,
    )
    client.post(
        f"/projects/{pid}/documents/",
        data={"tipo": "artigo"},
        files={"file": ("doc2.pdf", io.BytesIO(b"dois"), "application/pdf")},
        headers=auth_header,
    )
    resp = client.get(f"/projects/{pid}/documents/", headers=auth_header)
    assert resp.status_code == 200
    assert len(resp.json()) == 2