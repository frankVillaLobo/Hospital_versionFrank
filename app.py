from types import MethodType
from flask import Flask, render_template, request, jsonify, url_for, redirect
import json

app = Flask(__name__)

with open('usuarios.json') as users:
    data = json.load(users)
    usuarios = data['usuarios']

@app.route("/")
def inicio():
    return render_template("Principal.html")

@app.route("/inicio")
def principal():
    return render_template("Principal.html")

@app.route("/inicio/registro", methods = ['POST', 'GET'])
def registro():
    if request.method == 'GET':
        return render_template("registrar.html")
    else:
        tipo = 'paciente'
        cedula = request.form['cedula']
        password = request.form['password']
        newUser = {'tipo': tipo, 'cedula':cedula, 'password':password}
        encontrado = [usuario for usuario in usuarios if usuario["cedula"] == cedula]
        if len(encontrado)>0:
            return '<h1>El número de identificación registrado ya se encuentra en nuestra base de datos<a class="link" href="iniciarSesion">Iniciar Sesión</a></h1>'
        else:
            usuarios.append(newUser)
            with open('usuarios.json', 'w') as users:
                json.dump(data, users, indent = 4)
            return '<h1>Tú registro ha sido exitoso si deseas iniciar sesión <a class="link" href="iniciarSesion">Iniciar Sesión</a></h1></br><h1>Si deseas volver a nuestra pagina principal <a class="link" href="/inicio">Inicio</a></h1>'

@app.route("/inicio/iniciarSesion", methods = ['POST', 'GET'])
def iniciarSesion():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        cedula = request.form['cedula']
        password = request.form['password']
        encontrado = [usuario for usuario in usuarios if usuario["cedula"] == cedula]
        if len(encontrado)>0:
            if encontrado[0]['password'] == password:
                if encontrado[0]['tipo'] =='paciente':
                    return redirect(url_for('iniciarSesionPaciente'))
                elif encontrado[0]['tipo'] == 'medico':
                    return redirect(url_for('iniciarSesionMedico'))
                elif encontrado[0]['tipo'] == 'superadministrador':
                    return redirect(url_for('dashboard'))
            else:
                return '<h1>Contraseña incorrecta, intentar de nuevo <a class="link" href="iniciarSesion">Iniciar Sesión</a></h1>'
        else:
            return '<h1>El usuario no se encuentra registrado <a class="link" href="regitro">Regitrate</a></br><h1>Si fue un error inicia sesión nuevamente<a class="link" href="iniciarSesión">Iniciar Sesión</a></h1>'

@app.route("/inicio/busqueda", methods = ['POST', 'GET'])
def busqueda():
    return render_template("busqueda.html")

@app.route("/inicio/iniciarSesion/paciente")
def iniciarSesionPaciente():
    return render_template("principalPaciente.html")

@app.route("/inicio/iniciarSesion/medico")
def iniciarSesionMedico():
    return render_template("principalMedico.html")

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