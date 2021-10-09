from types import MethodType
from flask import Flask, render_template

app = Flask(__name__, 
            template_folder='Principal',
            static_folder='Principal')

@app.route("/inicio")
def principal():
    return render_template("Principal.html")

@app.route("/inicio/Registro", methods = ['POST', 'GET'])
def registro():
    return render_template("Registrar/registrar.html")

@app.route("/inicio/IniciarSesion", methods = ['POST', 'GET'])
def iniciarSesion():
    return render_template("Registrar/login.html")

@app.route("/inicio/busqueda", methods = ['POST', 'GET'])
def busqueda():
    return render_template("Registrar/busqueda.html")

@app.route("/inicio/IniciarSesion/Paciente")
def iniciarSesionPaciente():
    return render_template("Registrar/Paciente/principalPaciente.html")