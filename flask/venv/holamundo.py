from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "hola mundo"

# GET, POST, PUT, PATCH, DELTE

@app.route("/post/<post_id>", methods=['GET', 'POST'])
def page(post_id):
    if request.method == 'GET':
        return "El id del GET es:  " + post_id
    else: 
        return "El id del POST es: " + post_id

@app.route("/otraruta", methods=['POST'])
def otraruta():
    print (request.form)
    print (request.form['llave1'])
    print (request.form['llave2'])
    return "Otra ruta"