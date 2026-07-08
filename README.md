# 📚 Trunk PI

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python">
  <img src="https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-red">
  <img src="https://img.shields.io/badge/Alembic-Migrations-green">
</p>

## 📖 Sobre o Projeto

O **Trunk PI** é uma plataforma acadêmica desenvolvida para centralizar, organizar e disponibilizar os **Projetos Integradores (PI)** produzidos pelos estudantes da instituição.

A proposta é criar um ambiente onde alunos e professores possam armazenar, consultar e compartilhar projetos desenvolvidos ao longo da graduação, promovendo a disseminação do conhecimento, reutilização de boas práticas e incentivo à inovação.

A plataforma permite que os usuários tenham acesso aos projetos organizados por cursos, facilitando pesquisas, consultas e referências para futuras produções acadêmicas.

---

# 🎯 Objetivos

- Centralizar o armazenamento dos Projetos Integradores.
- Facilitar a consulta de projetos anteriores.
- Organizar projetos por curso.
- Incentivar o compartilhamento de conhecimento.
- Disponibilizar uma API moderna e escalável.

---

# 🛠️ Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- SQLite3
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn

---

# 📂 Estrutura do Projeto

```
backend/
│
├── app/
│   ├── core/              # Configurações gerais da aplicação
│   ├── models/            # Modelos do banco de dados
│   ├── repositories/      # Camada de acesso aos dados
│   ├── routers/           # Rotas da API
│   ├── schemas/           # Validação dos dados (Pydantic)
│   ├── services/          # Regras de negócio
│   ├── utils/             # Funções auxiliares
│   ├── __init__.py
│   └── main.py            # Inicialização da aplicação
│
├── frontend/              # Interface da aplicação
├── migrations/            # Migrações do Alembic
├── tests/                 # Testes automatizados
│
├── alembic.ini
├── requirements.txt
└── .gitignore
```

---

# 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas (**Layered Architecture**), promovendo separação de responsabilidades e maior facilidade de manutenção.

### Core

Responsável pelas configurações da aplicação.

### Models

Representam as tabelas do banco de dados através do SQLAlchemy.

### Schemas

Realizam validação e serialização utilizando Pydantic.

### Repositories

Responsáveis pelas operações de acesso ao banco de dados (CRUD).

### Services

Implementam toda a regra de negócio da aplicação.

### Routers

Definem os endpoints da API.

### Utils

Contém funções auxiliares reutilizáveis.

---

# ⚙️ Como executar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/Camilla-uchoa/Trunk-PI.git
```

Entre na pasta:

```bash
cd Trunk-PI/backend
```

---

## 2. Crie um ambiente virtual

Windows

```bash
python -m venv .venv
```

Linux/Mac

```bash
python3 -m venv .venv
```

---

## 3. Ative o ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 5. Execute as migrações do banco

Caso o banco ainda não exista:

```bash
alembic upgrade head
```

O SQLite será criado automaticamente.

---

## 6. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

Servidor disponível em:

```
http://127.0.0.1:8000
```

---

# 📑 Documentação da API

Após iniciar o servidor, a documentação estará disponível em:

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🗄️ Banco de Dados

O projeto utiliza **SQLite3**, um banco de dados relacional leve e embarcado.

As tabelas são gerenciadas utilizando:

- SQLAlchemy (ORM)
- Alembic (controle de migrações)

---

# 🔄 Fluxo da Aplicação

```text
Cliente
   │
   ▼
Routers (API)
   │
   ▼
Services
   │
   ▼
Repositories
   │
   ▼
Models
   │
   ▼
SQLite
```

---

# 🧪 Testes

Para executar os testes:

```bash
pytest
```

Ou

```bash
python -m pytest
```

---

# 🚀 Funcionalidades

- Cadastro de Projetos Integradores
- Consulta de projetos
- Organização por cursos
- Persistência em banco de dados
- API REST
- Documentação automática
- Estrutura escalável

---

# 📈 Melhorias Futuras

- Autenticação JWT
- Controle de permissões
- Upload de arquivos
- Busca avançada
- Favoritos
- Sistema de comentários
- Dashboard administrativo
- Integração com banco PostgreSQL
- Deploy em ambiente de produção

---

# 👨‍💻 Equipe de Desenvolvimento

Projeto desenvolvido durante o Projeto Integrador da graduação em **Análise e Desenvolvimento de Sistemas**, utilizando metodologias ágeis e arquitetura em camadas para construção de uma API REST moderna com FastAPI.

---

# 📄 Licença

Este projeto possui finalidade exclusivamente acadêmica.
