from sqlalchemy import Column, Integer, String

from app.database import Base


class Departamento(Base):
    __tablename__ = 'departamentos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
