# 🚀 API Flask de Usuarios

Esta es una API RESTful sencilla desarrollada con [Flask](https://flask.palletsprojects.com/) y SQLite, empaquetada como imagen Docker. El objetivo es demostrar cómo funcionan las rutas (`routes`) en Python mediante un ejemplo práctico y productivo.

---

## 📁 Estructura del Proyecto

demo_rutas/
├── app_flask.py # Código principal de la aplicación Flask
├── requirements.txt # Dependencias Python
├── Dockerfile # Definición de la imagen Docker
└── HELP.md # Documentación interactiva expuesta en la ruta "/"

---

## 🧰 Requisitos

- Python 3.12+ (solo para ejecución local)
- Docker (para construir y desplegar la imagen)
- Cuenta en [Docker Hub](https://hub.docker.com/) (opcional para publicar)

---

## 🚀 Instalación y Ejecución

### 🔧 Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/demo_rutas.git
cd demo_rutas
Cambia tu_usuario por tu nombre de usuario en GitHub.

⚙️ Ejecución local (sin Docker)
Crear entorno virtual (opcional pero recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate
Instalar dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecutar la app:

bash
Copiar
Editar
python app_flask.py
Accede a: http://localhost:5000

🐳 Construir y ejecutar con Docker
Construir imagen Docker:

docker build -t acolmenares/api-flask-usuarios:1.0 .
Ejecutar contenedor:

docker run -d -p 5000:5000 acolmenares/api-flask-usuarios:1.0
Accede en navegador o vía curl:

curl http://localhost:5000/
☁️ Subir imagen a Docker Hub
Iniciar sesión:

docker login
Subir imagen:

docker push acolmenares/api-flask-usuarios:1.0
Descargar desde cualquier máquina:

docker pull acolmenares/api-flask-usuarios:1.0
🔌 Endpoints disponibles
Método	Ruta	Descripción
GET	/	Muestra la documentación (HELP)
GET	/saludo/<nombre>	Saludo personalizado
POST	/usuarios	Crea un nuevo usuario
GET	/usuarios	Lista todos los usuarios

📚 Ejemplos de uso con curl
Crear usuario
curl -X POST -H "Content-Type: application/json" \
     -d '{"nombre":"María"}' \
     http://localhost:5000/usuarios
Ver usuarios
curl http://localhost:5000/usuarios
Ver documentación en texto plano:
curl http://localhost:5000/
🧑‍💻 Autor
Alan Colmenares
🔗 Docker Hub

🙌 Contribuciones
¡Contribuciones son bienvenidas!

Haz un fork del repositorio

Crea una rama con tus cambios (git checkout -b feature/nueva-funcion)

Haz commit (git commit -am 'Agrega nueva función')

Sube tu rama (git push origin feature/nueva-funcion)

Abre un Pull Request

🛡️ Licencia
Este proyecto está bajo licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.

📌 Notas finales
El contenido de HELP.md se muestra directamente en la ruta / como una página HTML.

La base de datos usuarios.db se crea automáticamente con SQLite dentro del contenedor o carpeta local.


---









