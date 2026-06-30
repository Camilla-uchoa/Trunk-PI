from fastapi import APIRouter

router = APIRouter(prefix="/help", tags=["Ajuda"])


@router.get("/")
def get_help():
    return {
        "sistema": "Trunk - Gerenciamento de Projetos Integradores",
        "versao": "1.0.0",
        "descricao": "Sistema para armazenar, organizar e gerenciar projetos integradores.",
        "funcionalidades": [
            {"nome": "Autenticação", "descricao": "Login, cadastro e recuperação de senha"},
            {"nome": "Projetos", "descricao": "CRUD completo de projetos integradores com filtros"},
            {"nome": "Documentos", "descricao": "Upload e consulta de documentos por projeto"},
            {"nome": "Acompanhamento", "descricao": "Registro de orientações, entregas e pendências"},
            {"nome": "Avaliação", "descricao": "Registro de notas e pareceres por avaliador"},
            {"nome": "Relatórios", "descricao": "Geração de relatórios por curso, período, orientador e status"},
            {"nome": "Suporte", "descricao": "Página de contato para dúvidas e suporte"},
        ],
        "perfis": [
            {"nome": "Aluno", "descricao": "Cadastra projetos, envia documentos, acompanha status"},
            {"nome": "Professor", "descricao": "Acompanha projetos, orienta equipes, avalia"},
            {"nome": "Coordenador", "descricao": "Visão geral, gerencia usuários, relatórios"},
            {"nome": "Avaliador", "descricao": "Registra avaliações e pareceres"},
        ],
    }