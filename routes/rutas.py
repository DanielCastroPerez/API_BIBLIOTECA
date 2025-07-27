import datetime
from http.client import responses
from typing import List

from pyexpat.errors import messages

from config.db import get_db
from models.tab_biblioteca_model import Biblioteca
from schemas.mod_biblioteca import BibliotecaResponse, BibliotecaCreate
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/usuarios", response_model=List[BibliotecaResponse])
def Usuarios(db: Session = Depends(get_db)):
    libros = db.query(Biblioteca)
    if not libros:
        raise HTTPException(status_code=404, detail="No hay libros para mostrar")
    return libros


@router.get("/obtener_usuario/{id}", response_model=List[BibliotecaResponse])
def obtener_user(id: int, db: Session = Depends(get_db)):
    libro = db.query(Biblioteca).filter(Biblioteca.id == id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


@router.post("/Nuevo_Libro", response_model=BibliotecaCreate)
def crear_libro(libro: BibliotecaCreate, db: Session = Depends(get_db)):
    libro_creado = Biblioteca(**libro.dict())
    db.add(libro_creado)
    db.commit()
    db.refresh(libro_creado)
    return libro_creado


@router.put("/Modificar_Libro/{id}", response_model=BibliotecaResponse)
def modificar_libro(id: str, Libro_Modifi: BibliotecaCreate, db: Session = Depends(get_db)):
    libro_id = db.query(Biblioteca).filter(Biblioteca.id == id).first()
    print("valor de libro_id", libro_id)
    print("Valor_ de id ", id, " typo de id", type(id))
    if not libro_id:
        raise   HTTPException(status_code=404, detail="Libro no encontrado")
    for key, value in Libro_Modifi.dict().items():
        setattr(libro_id, key, value)
    libro_id.fecha_actualizacion=datetime.datetime.now()
    db.commit()
    db.refresh(libro_id)
    return libro_id


@router.delete("/Eliminar_libro/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    delet_book = db.query(Biblioteca).filter(Biblioteca.id == id).first()
    if not delet_book:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    db.delete(delet_book)
    db.commit()
    return {"message": "Libro eliminado correctamente"}
