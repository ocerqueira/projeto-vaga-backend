
# ACMEVita - Backend API

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker e Docker Compose
- Pytest (para testes)
- Uvicorn (servidor ASGI)

---

## Requisitos

Antes de iniciar, instale o docker se não tiver:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Bora lá rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/ocerqueira/projeto-vaga-backend.git
cd projeto-vaga-backend
````

### 2. Inicie a aplicação com Docker Compose

```bash
docker compose up --build
```

Esse comando:

* Ele sobe o banco de dados PostgreSQL
* Sobe o backend com FastAPI
* Executa automaticamente uma seed com dados de exemplo para popular o banco de dados com departamentos e colaboradores

---

## Acessando os Endpoints

Após o container subir, acesse:

* **Documentação Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Documentação Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Rodando os Testes

Se quiser executar os testes unitários (fora do container docker), use:

```bash
source .venv/Scripts/activate  # Windows
# ou
source .venv/bin/activate  # Linux/macOS

pytest
```

---

## Variáveis de Ambiente

A variável de conexão com o banco já está configurada por padrão. Se quiser customizar, só edite o arquivo `.env` (ou crie um):

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/acmevita
```

---

## Estrutura do Projeto

```
├── app/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
    |-- app.py
│   └── database.py
├── scripts/
│   └── seed.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
```

---
