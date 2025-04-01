## FastAPI Example
Este repositorio es simplemente un ejemplo del uso de FastAPI para Introducción al Desarrollo de Software TB022 curso Esteban.

La branch main está vacía, cada branch contiene ejemplos de distintas features.

`basic`

Setup básico de FastAPI con un modelo de Alumno en memoria.

`basic-with-structure`

Setup básico de FastAPI con un modelo de Alumno en memoria pero separando los endpoints por recurso usando routers y usando una capa de Database. Los datos se cargan de un CSV.

`sql-model`

Setup con db connection a SQLite de un modelo de Alumno.

`sql-model-with-relations`

Setup con db connection a SQLite con modelos de Alumo, Grupo, Integrante para representar relaciones N:M


## Setup

1. Setup pyenv
```
pyenv local 3.13.2
```

2. Crear venv

```
pyenv exec python -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias
```
pip install -r requirements.txt
```

## Correr migraciones
```
alembic upgrade head
```

## Correr servidor
```
python -m astapi dev main.py
```

## Correr tests
```
python -m pytest test/
```
