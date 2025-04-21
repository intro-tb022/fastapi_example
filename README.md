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
pyenv install 3.13.2
```

2. Crear venv usando pipenv 

```
pipenv shell
```

3. Instalar dependencias
```
pipenv install
```

## Correr servidor
```
python -m fastapi dev main.py
```

## Correr tests
```
python -m pytest tests/
```
