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

# Imprimir resultados
for i in institucion:
    print(i)


# Obtener todos los registros de clase Departamento 
departamento = session.query(Departamento).all()

# Imprimir resultados
for i in departamento:
    print(i)


# Obtener todos los registros de clase Investigador 
investigador = session.query(Investigador).all()

# Imprimir resultados
for i in investigador:
    print(i)


# Obtener todos los registros de clase Publicacion
publicacion = session.query(Publicacion).all()

# Imprimir resultados
for i in publicacion:
    print(i)
