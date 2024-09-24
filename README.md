## FastAPI Example
Este repositorio es simplemente un ejemplo del uso de FastAPI para Introducción al Desarrollo de Software TB022 curso Esteban.

La branch main está vacía, cada branch contiene ejemplos de distintas features.

`basic`

Setup básico de FastAPI con un modelo de Alumno en memoria.

`basic-with-routers`

Setup básico de FastAPI con un modelo de Alumno en memoria pero separando los endpoints por recurso usando routers.

`sql-model`

Setup con db connection a SQLite de un modelo de Alumno.

`sql-model-with-relations`

Setup con db connection a SQLite con modelos de Alumno y Grupo para representar relaciones 1:N

`sql-model-with-relations-advanced`

Setup con db connection a SQLite con modelos de Alumo, Grupo, Curso, Materia para representar relaciones N:M


## Setup
El entorno virtual y las dependencias son manejadas usando [uv](https://docs.astral.sh/uv/)

1. Instalar dependencias
```
uv sync
```

## Correr servidor
```
uv run fastapi dev main.py
```
