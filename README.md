# 🏥 API de Clínicas - Meu Projeto de Estudo com FastAPI + SQLAlchemy

> Este é um projeto de estudo pessoal focado em construir uma API RESTful completa para gerenciar o cadastro de clínicas. Uma ótima oportunidade para consolidar o conhecimento com a poderosa combinação de **FastAPI**, **SQLAlchemy (Async)** e **Supabase (PostgreSQL)**.

---

## 🎯 Motivação (Foco no Aprendizado)

O principal objetivo deste projeto é simular um **CRUD (Criar, Ler, Atualizar, Deletar)** robusto em uma arquitetura de camadas. Este projeto está sendo usado como peça central do meu portfólio para aprofundar em:

* **Desenvolvimento Assíncrono:** Uso do **AsyncIO** no Python e no SQLAlchemy.
* **Arquitetura de Camadas:** Separação clara entre Rotas, Lógica de Negócio (Controllers) e Acesso a Dados (Services).
* **Contêineres de DB:** Conexão e persistência de dados utilizando o **PostgreSQL** hospedado no Supabase.

---

## ✨ Tecnologias Utilizadas (Tech Stack)

| Categoria | Tecnologia | Uso |
| :--- | :--- | :--- |
| **Linguagem** | Python | Versão 3.10+ |
| **Framework** | **FastAPI** | Alto desempenho e documentação automática. |
| **Servidor** | Uvicorn | Servidor ASGI para rodar o FastAPI. |
| **ORM** | **SQLAlchemy** | Mapeamento Objeto-Relacional (AsyncIO). |
| **Validação** | **Pydantic v2** | Definição e validação robusta dos modelos de dados. |
| **Banco de Dados** | PostgreSQL | Hospedado no **Supabase** (serviço BaaS). |
| **Migrações** | Alembic | Gerenciamento do esquema do banco de dados (Opcional por enquanto). |

---

## ⚙️ Estrutura do Projeto
. ├── app/ │ ├── api/ │ │ ├── controllers/ # 🧠 Lógica de negócio da API. │ │ ├── routes/ # 🛣 Definição dos endpoints (caminhos da API). │ │ └── schemas/ # 📋 Modelos de dados (Pydantic para requisições/respostas e SQLAlchemy para o DB). │ ├── services/ # 💾 Camada que interage com o banco de dados (ou dicionário interno). │ └── config.py # ⚙️ Arquivo de configurações e variáveis de ambiente. ├── main.py # Ponto de entrada da aplicação FastAPI. ├── requirements.txt # Lista de dependências. └── .env.example # Exemplo das variáveis de ambiente necessárias.

---

## 🚀 Como Rodar o Projeto (Instalação e Setup)

### Pré-requisitos
* **Python 3.10+** instalado.
* **Git** instalado.

### 1. Baixar o Código

```bash
git clone [URL_DO_SEU_REPOSITORIO] 
cd api-de-clinicas
```
### 2. Ambiente Virtual
Criação e Ativação (Linux/macOS):
```
python -m venv venv
```
source venv/bin/activate


Ativação (Windows):
.\venv\Scripts\activate

###  3. Instalar as Dependências
```
pip install -r requirements.txt
```

### 4.Configuração do Ambiente (.env)
Crie um arquivo chamado .env na raiz do projeto. O projeto suporta dois modos de operação via variável API_MODE: db (Supabase/PostgreSQL) ou internal (dicionário em memória).
# Use sua URL de conexão REAL aqui para o modo 'db':
DATABASE_URL="postgresql+asyncpg://<USER>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>"

# Escolha o modo de operação:
API_MODE="db"

### 5. Configuração da Tabela (Modo db)
Se for rodar no modo db, o PostgreSQL precisa da seguinte tabela:
CREATE TABLE IF NOT EXISTS clinicas (
    id SERIAL PRIMARY KEY,
    clinica TEXT NOT NULL,
    especialidade TEXT NOT NULL,
    endereco TEXT NOT NULL
);

### 6. Executar a Aplicação
uvicorn main:app --reload
O servidor estará rodando em: http://localhost:8000

###Endpoints Disponíveis
Com o servidor rodando, você pode usar a documentação interativa:

Swagger UI: http://localhost:8000/docs (Recomendado)

ReDoc: http://localhost:8000/redoc

|Método|Rota|Descrição (CRUD)|
| :--- | :--- | :--- |
|GET|/clinicas/|Read: Lista todas as clínicas.|
|GET|/clinicas/{id}|Read: Detalha uma clínica específica pelo ID.|
|POST|/clinicas/|Create: Adiciona uma clínica nova.|
|PUT|/clinicas/{id}|Update: Edita os dados de uma clínica existente.|
|DELETE|/clinicas/{id}|Delete: Remove uma clínica do sistema.|

Contribuição e Feedback
Como este é um projeto de aprendizado, todo feedback é super bem-vindo!

Abrir uma Issue (para bugs ou sugestões).

Criar um Pull Request (para enviar código corrigido/melhorado).

Obrigado por conferir meu projeto!

**Autor:**
*Miguel S Cruz*
