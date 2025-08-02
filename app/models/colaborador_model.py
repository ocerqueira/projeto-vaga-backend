from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Colaborador(Base):
    __tablename__ = 'colaboladores'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    sobrenome = Column(String)
    departamento_id = Column(Integer, ForeignKey('departamentos.id'))
    dependentes = Column(String)

    departamento = relationship('Departamento', backref='colaboradores')
