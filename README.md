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

2. Crear ambiente virtual usando venv 

```
python3 -m venv <dir>
```

3. Activar el ambiente virtual
```
source <dir>/bin/activate
```
(a partir de acá, todo se hará dentro de ese ambiente virtual usando ese python para este proyecto)

4. Instalar dependencias
```
pip install -r requirements.txt
```

## Correr migraciones
```
alembic upgrade head
```

## Correr servidor
```
python -m fastapi dev main.py
```

## Correr tests
```
python -m pytest tests/
```
