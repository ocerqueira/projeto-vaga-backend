from fastapi import FastAPI

from app.database import Base, engine
from app.routers import departamentos

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(departamentos.router)


@app.get('/')
def read_root():
    return {'message': 'Bem-vindo à API AcmeVita!'}
