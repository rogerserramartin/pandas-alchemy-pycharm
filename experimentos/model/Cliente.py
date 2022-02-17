# https://docs.sqlalchemy.org/en/14/orm/tutorial.html
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido1 = Column(String)
    apellido2 = Column(String)
    dni = Column(String)
    patrimonio = Column(Float)


"""
    def __init__(self, nombre, apellido1, apellido2, dni, patrimonio):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.dni = dni
        self.patrimonio = patrimonio
"""