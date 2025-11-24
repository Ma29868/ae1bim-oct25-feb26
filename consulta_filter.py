from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clases de crear_base_entidades
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# se genera en enlace al gestor de bd sqlite
engine = create_engine('sqlite:///demobase3.db')

Session = sessionmaker(bind=engine)
session = Session()

#Obtener todos los registro donde el atributo id
# de la clase investigador sea menor o igual a 012
investigador = session.query(Investigador
             ).filter(Investigador.id <= "012").all()

#Imprimir resultados
for r in investigador:
    print(r)
