from typing import List

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.colaborador_model import Colaborador as ColaboradorModel
from app.models.departamento_model import Departamento as DepartamentoModel


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def obter_departamentos(db: Session) -> List[DepartamentoModel]:
    return db.query(DepartamentoModel).all()


def obter_colaboradores_por_departamento(
    departamento_id: int, db: Session
) -> List[dict]:
    departamento = (
        db.query(DepartamentoModel)
        .filter(DepartamentoModel.id == departamento_id)
        .first()
    )
    if not departamento:
        print('Departamento não encontrado')

    colaboradores = (
        db.query(ColaboradorModel)
        .filter(ColaboradorModel.departamento_id == departamento_id)
        .all()
    )

    return [
        {
            'nome_completo': f'{c.nome} {c.sobrenome}'.strip(),
            'tem_dependentes': bool(c.dependentes and c.dependentes.strip()),
        }
        for c in colaboradores
    ]
