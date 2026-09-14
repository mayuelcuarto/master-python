from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Aprendiendo Flask con Victor Robles"

@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<apellidos>')
def informacion(nombre = None, apellidos = None):
    texto = ""
    if nombre != None and apellidos != None:
        texto = f"<h3>Bienvenido, {nombre} {apellidos}</h3>"

    return f"""
            <h1>Página de información</h1>
            <p>Esta es la página de información<p>
            {texto}
    """

@app.route('/contacto')
def contacto():
    return "<h1>Página de contactos</h1>"

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return "<h1>Página de lenguajes</h1>"

if __name__ == '__main__':
    app.run(debug=True)