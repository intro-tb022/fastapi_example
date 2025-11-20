FROM python:3.13-slim

WORKDIR /app

# Instalamos las dependencias
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos el codigo fuente
COPY . .

EXPOSE 8000

# Usamos un user que no sea root (es opcional, puede ser cualquiera)
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Corremos las migraciones siempre
RUN alembic upgrade head

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
