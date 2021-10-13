from flask import request
import json

with open('usuarios.json') as users:
    data = json.load(users)
    usuarios = data['usuarios']

cedula = '12345678'
password = '87654321'
encontrado = [usuario for usuario in usuarios if usuario["cedula"] == cedula]

if encontrado[0]['password'] == password:
    print('bien')