from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clases de crear_base_entidades
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# se genera en enlace al gestor de bd sqlite
engine = create_engine('sqlite:///demobase3.db')

Session = sessionmaker(bind=engine)
session = Session()

#Ordenar los nombres de Departamento en 
#orden alfabetico de A --> Z

departamento = session.query(Departamento).order_by(
                Departamento.nombre).all()

#Imprimir resultados
for i in departamento:
    print(i.nombre)
