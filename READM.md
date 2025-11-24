API de Clpinicas - FastAPI +SQLAlchemy + Supabase

Este é um projeto de API completa para cadastro de clínicas médicas, construido em FastAPI, com persistência de dados usando SQLAlchemy e banco de dados PostgreSQL hospedado no Supabase.

O codígo também tem um "Dicionario" interno para executar a API de forma interna (útil para fazer teste).

TECNOLOGIAS ULTILIZADAS
Python 3.10+

FastAPI

Uvicorn

SQLAlchemy

Pydantic v2

PostgreSQL (Supabase)

scoped_session

Alembic (opcional para migrações)


Estrutura das pastas
app/
│
├── api/
│   ├── controllers/       → Lógica dos endpoints
│   ├── routes/            → Rotas da API
│   ├── schemas/           → SQLAlchemy e Pydantic
│   ├── services/          → Services (interno e banco)
│   ├── config.py          → Configuração (internal/db)
│   └── __init__.py
│
main.py                    → Inicialização FastAPI
requirements.txt           → Dependências
README.md                  → Documentação


Endpoints disponíveis
GET /clinicas/
POST /clinicas/
PUT /clinicas/{id}
DELETE /clinicas/{id}


Tabela do Banco no Supabase
create table if not exists clinicas (
    id serial primary key,
    clinica text not null,
    especialidade text not null,
    endereco text not null
);

Testar no navegador
http://localhost:8000/docs

http://localhost:8000/redoc

Forma de executação
No CMD dentro da pasta do projeto coloque "uvicorn main:app --reload"



