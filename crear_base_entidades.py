from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

# se importa información de configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de bd sqlite

engine = create_engine(cadena_base_datos)

Base = declarative_base()

# crear clases
class Institucion(Base):
    __tablename__ ='institucion'

    id = Column(Integer(), nullable=False, primary_key=True) 
    nombre = Column(String(50), nullable=False, unique=True)
    ciudad = Column(String(50), nullable=False)
    pais = Column(String(50), nullable=False)

    departamentos = relationship("Departamento", back_populates="institucion")

    def __repr__(self):
        return "Institucion: id=%s nombre=%s ciudad=%s pais=%s" % (
                          self.id,
                          self.nombre, 
                          self.ciudad, 
                          self.pais)


class Departamento(Base):
    __tablename__ = 'departamento'

    id = Column(Integer(), nullable=False, primary_key=True)
    nombre = Column(String(50), nullable=True)
    codigo = Column(String(10), nullable=True)
    institucion_id = Column(Integer, ForeignKey('institucion.id'))
    
    def __repr__(self):
        return "Departamento: id=%s nombre=%s codigo=%s" % (
                             self.id,
                             self.nombre,
                             self.codigo)

    institucion = relationship("Institucion", back_populates="departamentos")

    investigadores = relationship("Investigador", back_populates="departamento")


class Investigador(Base):
    __tablename__='investigador'

    id = Column(Integer(), nullable=False, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    area_investigacion = Column(String(100), nullable=False)
    departamento_id = Column(Integer, ForeignKey('departamento.id'))

    def __repr__(self):
        return "Investigador: id=%s nombre=%s apellido=%s email=%s area_investigacion=%s" % (
                             self.id,
                             self.nombre,
                             self.apellido,
                             self.email,
                             self.area_investigacion)
    departamento = relationship("Departamento", back_populates="investigadores")
    publicaciones = relationship("Publicacion", back_populates="investigador")


class Publicacion(Base):
    __tablename__='publicacion'

    id = Column(Integer(), nullable=False, primary_key=True)
    titulo = Column(String(50), nullable=False, unique=True)
    fecha_publicacion = Column(DateTime, default=datetime.now())
    doi = Column(String(50))
    tipo_publicacion = Column(String(50))
    investigador_id = Column(Integer, ForeignKey('investigador.id'))

    def __str__(self):
        return "Publicacion: id=%s titulo=%s fecha_publicacion=%s doi=%s tipo_publicacion=%s" % (
                                self.id,
                                self.titulo,
                                self.fecha_publicacion,
                                self.doi,
                                self.tipo_publicacion)
    investigador = relationship("Investigador", back_populates="publicaciones")



Base.metadata.create_all(engine)
