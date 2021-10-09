from types import MethodType
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/inicio")
def principal():
    return render_template("Principal.html")

@app.route("/inicio/registro", methods = ['POST', 'GET'])
def registro():
    return render_template("registrar.html")

@app.route("/inicio/iniciarSesion", methods = ['POST', 'GET'])
def iniciarSesion():
    return render_template("login.html")

@app.route("/inicio/busqueda", methods = ['POST', 'GET'])
def busqueda():
    return render_template("busqueda.html")

@app.route("/inicio/iniciarSesion/paciente")
def iniciarSesionPaciente():
    return render_template("principalPaciente.html")