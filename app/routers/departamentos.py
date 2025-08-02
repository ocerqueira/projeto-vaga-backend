from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.colaborador import Colaborador
from app.schemas.departamento import Departamento
from app.services.departamento_service import (
    get_db,
    obter_colaboradores_por_departamento,
    obter_departamentos,
)

router = APIRouter(prefix='/departamentos')


@router.get('/', response_model=List[Departamento])
def listar_departamentos(db: Session = Depends(get_db)):
    return obter_departamentos(db)


@router.get('/{departamento_id}/colaboradores', response_model=List[Colaborador])
def listar_colaboradores_por_departamento(
    departamento_id: int, db: Session = Depends(get_db)
):
    return obter_colaboradores_por_departamento(departamento_id, db)
