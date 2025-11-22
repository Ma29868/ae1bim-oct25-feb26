from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clases de crear_base_entidades 
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de bd sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de clase Institucion 
institucion = session.query(Institucion).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Institucion")
for s in institucion:
    print("%s" % (s))
    print("---------")

# Obtener todos los registros de clase Departamento
departamento = session.query(Departamento).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Departamento")
for s in departamento:
    print("%s" % (s))
    print("---------")

# Obtener todos los registros de clase Investigador
investigador = session.query(Investigador).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Investigador")
for s in institucion:
    print("%s" % (s))
    print("---------")

# Obtener todos los registros de clase Publicacion 
pnstitucion = session.query(Publicacion).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de Publicacion")
for s in institucion:
    print("%s" % (s))
    print("---------")
