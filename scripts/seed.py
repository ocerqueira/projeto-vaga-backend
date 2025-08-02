from app.database import Base, SessionLocal, engine
from app.models.colaborador_model import Colaborador
from app.models.departamento_model import Departamento


print("Resetando banco de dados...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()


print("Inserindo departamentos...")
rh = Departamento(nome='RH')
tecnologia = Departamento(nome='Tecnologia')
financeiro = Departamento(nome='Financeiro')

db.add_all([rh, tecnologia, financeiro])
db.commit()


db.refresh(rh)
db.refresh(tecnologia)
db.refresh(financeiro)


print("Inserindo colaboradores...")
db.add_all([
    Colaborador(
        nome='João', sobrenome='Silva', departamento_id=rh.id, dependentes='Lucas,Marina'
    ),
    Colaborador(nome='Pedro', sobrenome='Santos', departamento_id=rh.id, dependentes=''),
    Colaborador(nome='Mariana', sobrenome='Santos', departamento_id=rh.id, dependentes=''),
    Colaborador(nome='Maria', sobrenome='Pio', departamento_id=rh.id, dependentes='Otavio, Enzo'),
    Colaborador(nome='Atila', sobrenome='Pio', departamento_id=rh.id, dependentes='Otavio, Enzo'),
])

db.commit()
db.close()

print("Seed finalizado com sucesso.")
