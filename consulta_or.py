from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import or_

# se importa la clases de crear_base_entidades
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# se genera en enlace al gestor de bd sqlite
engine = create_engine('sqlite:///demobase3.db')

Session = sessionmaker(bind=engine)
session = Session()


#Obtener los nombres de Alexandra o Martin 
# en la clase investigador
investigador = session.query(Investigador).filter(
                (Investigador.nombre == "Alexandra") | 
                (Investigador.nombre == "Martin")
                ).all()

#Imprimir resultados
for r in investigador:
    print(r)
