from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
db = SQLAlchemy(app)

# Modelo de base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)

# Crear la base de datos
with app.app_context():
    db.create_all()

# Ruta raíz que muestra HELP.md como HTML
@app.route('/')
def mostrar_help():
    help_path = os.path.join(os.path.dirname(__file__), 'HELP.md')
    if os.path.exists(help_path):
        with open(help_path, 'r', encoding='utf-8') as f:
            markdown = f.read()
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Documentación API Flask de Alan Colmenares</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    padding: 2em;
                    background-color: #f5f5f5;
                    color: #333;
                }}
                code, pre {{
                    background: #eee;
                    padding: 0.5em;
                    border-radius: 4px;
                    display: block;
                    overflow-x: auto;
                }}
                h1, h2, h3 {{
                    color: #2c3e50;
                }}
                hr {{
                    border: 0;
                    height: 1px;
                    background: #ccc;
                    margin: 2em 0;
                }}
            </style>
        </head>
        <body>
        <pre>{markdown}</pre>
        </body>
        </html>
        """
        return html
    else:
        return "<h1>HELP.md no encontrado</h1>", 404

# Ruta con parámetro
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f'Hola, {nombre}!'

# Ruta POST (crear usuario)
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nuevo = Usuario(nombre=data['nombre'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado", "id": nuevo.id})

# Ruta GET (consultar usuarios)
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nombre": u.nombre} for u in usuarios])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

