from types import MethodType
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("Principal.html")

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

@app.route("/inicio/iniciarSesion/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/inicio/iniciarSesion/dashboard/paciente")
def dashboardPaciente():
    return render_template("dashboardPaciente.html")

@app.route("/inicio/iniciarSesion/dashboard/medico")
def dashboardMedico():
    return render_template("dasboardMedico.html")

@app.route("/inicio/iniciarSesion/dashboard/citas")
def dashboardCitas():
    return render_template("dasboardCitas.html")

@app.route("/inicio/iniciarSesion/dashboard/hclinica")
def dashboardHClinica():
    return render_template("dashboardHistoriaClinica.html")

@app.route("/inicio/iniciarSesion/dashboard/agenda")
def dashboardAgenda():
    return render_template("dashboardAgenda.html")

@app.route("/inicio/iniciarSesion/dashboard/ayuda")
def dashboardAyuda():
    return render_template("dashboardAyuda.html")

@app.route("/inicio/iniciarSesion/medico")
def perfilMedico():
    return render_template("PrincipalMedico.html")

@app.route("/inicio/iniciarSesion/medico/detalleCita")
def detalleCita():
    return render_template("detallecitamedico.html")