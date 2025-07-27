from config.db import base
from sqlalchemy import Column, Integer, String, DateTime, BigInteger
import datetime


class Biblioteca(base):
    """Modelo de la tabla Biblioteca se delcaran columnas y su tipo"""

    __tablename__ = "Biblioteca"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(50))
    autor = Column(String(50))
    anio_publicacion = Column(DateTime)
    isbn = Column(BigInteger)
    categoria = Column(String(20))
    fecha_creacion = Column(DateTime)
    fecha_actualizacion = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
