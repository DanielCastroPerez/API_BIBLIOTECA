from pydantic import BaseModel
import datetime


class BibliotecaCreate(BaseModel):
    titulo: str
    autor: str
    anio_publicacion: datetime.datetime
    isbn: int
    categoria: str
    fecha_creacion: datetime.datetime


class BibliotecaResponse(BibliotecaCreate):
    id: int
    fecha_actualizacion: datetime.datetime

    class Config:
        orm_mode = True
