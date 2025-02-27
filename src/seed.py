import csv
import os
import random

from fastapi import Path

from src.dependencies import get_database
from src.models import Alumno

src_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def seed():
    cargar_alumnos(os.path.join(src_root, "resources", "alumnos.csv"))

def cargar_alumnos(path):
    alumnos = []
    with open(path) as f:
        csvFile = csv.DictReader(f, delimiter=";")
        for linea in csvFile:
            alumnos.append(
                Alumno(
                    padron=int(linea["Padron"]),
                    nombre=linea["Nombre"],
                    apellido=linea["Apellido"],
                    edad=random.randint(18, 35)
                )
            )
    get_database().cargar_alumnos(sorted(alumnos, key= lambda x: x.padron))