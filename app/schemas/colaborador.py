from pydantic import BaseModel


class Colaborador(BaseModel):
    nome_completo: str
    tem_dependentes: bool
