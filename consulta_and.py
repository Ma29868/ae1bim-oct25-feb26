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

#Obtener todos los registros que tengan el atributo 
#ciudad sea igual a Cuenca y ademas valor atributo
# sea igual a pais Ecuador

institucion = session.query(Institucion).filter(Institucion.ciudad=="Cuenca", \
            Institucion.pais=="Ecuador").all()

#Imprimir resultados
print(institucion)


