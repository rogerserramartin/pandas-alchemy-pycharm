import pandas as pd
import model.Cliente as Cliente
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# mirar como meter usuario y password
engine = create_engine('postgresql://localhost:5432/test')

FILEPATH = 'recursos/clientes.csv'

dataframe_clientes = pd.read_csv(FILEPATH)

# Aqui yo podria hacer el tratamiento de los datos del dataframe

# print(dataframe_clientes.columns)
clientes = []
for index, row in dataframe_clientes.iterrows():
    cliente = Cliente
    cliente.nombre = row['nombre']
    cliente.apellido1 = row['apellido1']
    cliente.apellido2 = row['apellido2']
    cliente.dni = row['dni']
    cliente.patrimonio = row['patrimonio']
    clientes.append(cliente)

# Conectar con base de datos
Session = sessionmaker(bind=engine)
session = Session()
# metemos todos los clientes a la vez
# https://docs.sqlalchemy.org/en/14/orm/tutorial.html
# https://docs.sqlalchemy.org/en/14/orm/session_transaction.html <- mirar esto porque son transactions y no hace falta try catch/exception
try:
    session.addAll(clientes)
    session.commit()
except ValueError:
    mensaje = f"Se produjo un error incorporando los datos!: {ValueError}"
    print(mensaje)
    session.rollback()
finally:
    session.close()
