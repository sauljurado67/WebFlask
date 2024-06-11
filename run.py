# Importamos Flask 
from flask import Flask, render_template

# Crear app mediante Instancia
app = Flask(__name__)

# Crear rutas con sus correspondientes funciones
@app.route('/', methods=['GET']) # Indicamos metodo GET
def holamundo():
    return render_template('/index.html')

# MIS PROYECTOS
@app.route('/mis-proyectos', methods=['GET'])
def mostrarproyectos():
    return 'Aqui se motrarán mis proyectos'

# MI BLOG
@app.route('/blog', methods=['GET'])
def blog():
    return render_template('/blog.html')

# CONTACTO
@app.route('/contacto', methods=['GET'])
def contacto():
    return render_template('/contacto.html')


# Ejecutar nuestra app cuando ejecutemos este archivo run.py

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1',port='5001')

