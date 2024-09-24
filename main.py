from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Alumno(BaseModel):
    padron: int
    nombre: str
    apellido: str
    edad: int | None = None

class AlumnoCreate(BaseModel):
    nombre: str
    apellido: str
    edad: int | None = None

class Error(BaseModel):
    detail: str

alumnos: list[Alumno] = [
    Alumno(padron=94557, nombre="Federico", apellido="Esteban"),
    Alumno(padron=95557, nombre="Daniela", apellido="Riesgo"),
    Alumno(padron=98713, nombre="Juan Ignacio", apellido="Kristal")
]


@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/alumnos/")
def list() -> list[Alumno]:
    return alumnos

@app.get("/alumnos/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(padron: int) -> Alumno:
    return buscar_alumno(padron)

@app.post("/alumnos/", status_code=status.HTTP_201_CREATED)
def create(alumno: Alumno) -> Alumno:
    alumno.padron = len(alumnos)
    alumnos.append(alumno)
    return alumno

@app.put("/alumnos/{padron}")
def update(padron: int, alumno_actualizado: Alumno) -> Alumno:
    for alumno, indice in alumnos.items():
        if alumno.padron == padron:
            alumnos[indice] = alumno_actualizado
    raise HTTPException(status_code=status.HTTP_NOT_FOUND,
                        detail="Alumno not found")

@app.delete("/alumnos/{padron}")
def delete(padron: int) -> Alumno:
    for alumno in alumnos:
        if alumno.padron == padron:
            alumnos.remove(alumno)
            return alumno
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Alumno not found")

@app.put("/alumnos/{padron}/cargar_nota")
def cargar_nota(padron: int, nota: int) -> Alumno:
    alumno = buscar_alumno(padron)
    alumno.notas.append(nota)
    return alumno

def buscar_alumno(padron: int) -> Alumno:
    for alumno in alumnos:
        if alumno.padron == padron:
            return alumno
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Alumno not found")
