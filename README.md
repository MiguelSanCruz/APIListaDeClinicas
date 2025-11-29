API de Clínicas - Meu Projeto de Estudo com FastAPI + SQLAlchemy + Supabase

Este é um projeto de estudo pessoal focado em construir uma API RESTful completa para gerenciar o cadastro de clínicas. É mais um passo na minha jornada de aprendizado, e estou muito animado(a) com a combinação dessas tecnologias!

A ideia aqui é simular um CRUD (Criar, Ler, Atualizar, Deletar) robusto.

Um detalhe legal: A API tem dois modos de operação que eu criei para facilitar os testes:

Modo DB (oficial): Conecta ao PostgreSQL do Supabase para ter dados reais e persistentes.

Modo Interno (para testes): Usa um dicionário Python em memória. Perfeito para testar rápido sem me preocupar com o banco!

O que eu estou usando (Tech Stack)

Estou treinando bastante com essa stack:

Linguagem: Python 3.10+ (Amo Python!)

Framework: FastAPI (Muita velocidade!)

Servidor ASGI: Uvicorn

ORM: SQLAlchemy (Com suporte a AsyncIO, o que me deu um bom trabalho para aprender, mas valeu a pena!)

Validação de Dados: Pydantic v2

Banco de Dados: PostgreSQL (Hospedado no Supabase - que é um serviço incrível)

Migrações: Alembic (Ainda estou pegando o jeito, mas é opcional por enquanto)

Estrutura das Pastas

Tentei organizar o código seguindo as boas práticas que estou aprendendo, separando a lógica de negócio, rotas e modelos:

app/
├── api/
│   ├── controllers/  → A lógica de negócio (o "cérebro" da minha API).
│   ├── routes/       → Onde defino os caminhos (endpoints).
│   └── schemas/      → Modelos de dados (SQLAlchemy e Pydantic).
├── services/         → A parte que conversa com o banco de dados (ou com o dicionário interno).
├── config.py         → Arquivo de configurações (para mudar do modo DB para o Interno).
main.py               → Onde a aplicação FastAPI inicia.
requirements.txt      → Lista de pacotes necessários.
.env.example          → Para mostrar as variáveis de ambiente necessárias.


Como Rodar Aqui (Instalação e Setup)

Se quiser testar ou dar uma olhada, é bem simples!

1. Requisitos

Python 3.10+ instalado.

2. Baixar o Código

git clone <URL_DO_SEU_REPOSITORIO>
cd api-de-clinicas


3. Ambiente Virtual (Recomendado)

Sempre bom isolar as dependências!

# Cria e ativa (Linux/macOS)
python -m venv venv
source venv/bin/activate

# Ativa no Windows
.\venv\Scripts\activate


4. Instalar as Dependências

pip install -r requirements.txt


5. Configuração do Banco de Dados (Se quiser usar o modo DB)

Crie um arquivo chamado .env e coloque a URL do seu PostgreSQL/Supabase.

Use a variável API_MODE para escolher entre 'db' ou 'internal':

# Conteúdo do arquivo .env
# Use sua URL de conexão REAL aqui:
DATABASE_URL="postgresql+asyncpg://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>"

# API_MODE="db" para rodar com o banco | API_MODE="internal" para rodar com o dicionário
API_MODE="db" 


Tabela no Supabase: Se for usar o DB, o Supabase precisa dessa tabela:

CREATE TABLE IF NOT EXISTS clinicas (
    id SERIAL PRIMARY KEY,
    clinica TEXT NOT NULL,
    especialidade TEXT NOT NULL,
    endereco TEXT NOT NULL
);


Como rodar

É só usar o Uvicorn para iniciar o servidor. O --reload é mágico para o desenvolvimento, pois salva e já recarrega na hora!

uvicorn main:app --reload


Testando os Endpoints

Com o servidor rodando em http://localhost:8000, você pode usar a documentação interativa:

Swagger UI: http://localhost:8000/docs (Eu uso muito essa!)

ReDoc: http://localhost:8000/redoc

Os endpoints disponíveis são:

GET /clinicas/    - Me mostra todas as clínicas.

GET /clinicas/{id}    - Me mostra uma clínica específica.

POST /clinicas/    - Adiciona uma clínica nova.

PUT /clinicas/{id}    - Edita uma clínica.

DELETE /clinicas/{id}    -Remove uma clínica.


Como estou aprendendo, todo feedback é super bem-vindo!

Se você viu algo que eu poderia fazer melhor ou quiser sugerir uma feature, sinta-se à vontade para:

Abrir uma Issue (para bugs ou sugestões).

Criar um Pull Request (para mandar código corrigido/melhorado).

Obrigado por conferir meu projeto! 

Licença

Este projeto está sob a licença 

$$Escolha uma licença, ex: MIT$$


