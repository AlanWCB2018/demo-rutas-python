# Imagen base
FROM python:3.12-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY app_flask.py .
COPY HELP.md .

# Puerto expuesto
EXPOSE 5000

# Comando de inicio
CMD ["python", "app_flask.py"]
