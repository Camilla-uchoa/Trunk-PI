from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if settings.database_url.startswith("sqlite") else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
     CREATE DATABASE banco_projetos_academicos;

USE banco_projetos_academicos;

-- =====================================
-- USUARIO
-- =====================================

CREATE TABLE usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha_criptografada TEXT NOT NULL,
    tipo_perfil TEXT NOT NULL CHECK (
        tipo_perfil IN ('ALUNO', 'PROFESSOR')
    )
);

CREATE TABLE aluno (
    id_usuario INTEGER PRIMARY KEY,
    matricula TEXT NOT NULL UNIQUE,
    curso TEXT NOT NULL,

    FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
        ON DELETE CASCADE
);

CREATE TABLE professor (
    id_usuario INTEGER PRIMARY KEY,
    id_funcional TEXT NOT NULL UNIQUE,
    departamento TEXT NOT NULL,

    FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
        ON DELETE CASCADE
);

CREATE TABLE curso (
    id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE turma (
    id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    periodo TEXT NOT NULL
);

CREATE TABLE categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE projeto (
    id_projeto INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    resumo TEXT,
    ano_letivo INTEGER NOT NULL,
    status_aprovacao TEXT NOT NULL DEFAULT 'PENDENTE',

    id_aluno INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    id_turma INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    id_professor INTEGER NOT NULL,

    FOREIGN KEY (id_aluno)
        REFERENCES aluno(id_usuario),

    FOREIGN KEY (id_curso)
        REFERENCES curso(id_curso),

    FOREIGN KEY (id_turma)
        REFERENCES turma(id_turma),

    FOREIGN KEY (id_categoria)
        REFERENCES categoria(id_categoria),

    FOREIGN KEY (id_professor)
        REFERENCES professor(id_usuario)
);

CREATE TABLE arquivo (
    id_arquivo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_arquivo TEXT NOT NULL,
    caminho_diretorio TEXT NOT NULL,
    tamanho_bytes INTEGER NOT NULL,

    id_projeto INTEGER NOT NULL,

    FOREIGN KEY (id_projeto)
        REFERENCES projeto(id_projeto)
        ON DELETE CASCADE
);
