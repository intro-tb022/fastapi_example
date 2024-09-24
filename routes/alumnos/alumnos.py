from models import Alumno, AlumnoCreate, Error, alumnos

from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/")
def list() -> list[Alumno]:
    return alumnos

@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(padron: int) -> Alumno:
    return buscar_alumno(padron)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(alumno_a_crear: AlumnoCreate) -> Alumno:
    alumno = Alumno(
        padron=len(alumnos),
        nombre=alumno_a_crear.nombre,
        apellido=alumno_a_crear.apellido,
        edad=alumno_a_crear.edad
    )
    alumno.padron = len(alumnos)
    alumnos.append(alumno)
    return alumno

@router.put("/{padron}")
def update(padron: int, alumno_actualizado: Alumno) -> Alumno:
    for alumno, indice in alumnos.items():
        if alumno.padron == padron:
            alumnos[indice] = alumno_actualizado
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Alumno not found")

@router.delete("/{padron}")
def delete(padron: int) -> Alumno:
    alumno = buscar_alumno(padron)
    alumnos.remove(alumno)
    return alumno

@router.put("/{padron}/cargar_nota")
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
