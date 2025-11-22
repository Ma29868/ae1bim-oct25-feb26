from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clases de crear_base_entidades
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

# se genera en enlace al gestor de bd sqlite
engine = create_engine('sqlite:///demobase3.db')

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Institucion
institucion1 = Institucion(id="001", nombre="Universidad Tecnica Particular de Loja", ciudad="Loja", pais="Ecuador")
institucion2 = Institucion(id="002", nombre="Universidad Estatal de Cuenca", ciudad="Cuenca", pais="Ecuador")
institucion3  = Institucion(id="003", nombre="Universidad Politecnica Salesiana", ciudad="Cuenca", pais="Ecuador")


# se crea un objetos de tipo departamento
departamento1 = Departamento(id="015", nombre="Administrativo", codigo="AD15")
departamento2 = Departamento(id="016", nombre="Gerencial", codigo="GE16")
departamento3 = Departamento(id="017", nombre="Operativo", codigo="op17")

# se crea un objetos de tipo Investigador
investigador1 = Investigador(id="011", nombre="Juan", apellido="Perez", email="juan@gmail.com", area_investigacion="Psicologia")
investigador2 = Investigador(id="012", nombre="Alexandra", apellido="Lopez", email="ale45@gmail.com", area_investigacion="Economia")
investigador3 = Investigador(id="013", nombre="Martin", apellido="Brito", email="brito732@gmail.com", area_investigacion="Administracion de Empresas")

# se crea un objetos de tipo Publicacion
publicacion1 = Publicacion(id="111", titulo="El impacto de la inteligencia emocional en la efectividad del liderazgo", fecha_publicacion= datetime(2025,11,22), doi="LBE345", tipo_publicacion="Tesis")
publicacion2 = Publicacion(id="112", titulo="Estrategias gerenciales para la implementación de la inteligencia artificial en el sector salud", fecha_publicacion= datetime(2025,11,22), doi="ASS398", tipo_publicacion="Tesis")
publicacion3 = Publicacion(id="113", titulo="Plan de mejora de la línea de producción de la empresa XXX utilizando el estudio del trabajo", fecha_publicacion= datetime(2025,11,22), doi="EST098", tipo_publicacion="Tesis")


# se agrega los objetos a la sesión a la espera de un commit para agregar un registro a la bd
session.add(institucion1)
session.add(institucion2)
session.add(institucion3)
session.add(departamento1)
session.add(departamento2)
session.add(departamento3)
session.add(investigador1)
session.add(investigador2)
session.add(investigador3)
session.add(publicacion1)
session.add(publicacion2)
session.add(publicacion3)

# se confirma las transacciones
session.commit()
