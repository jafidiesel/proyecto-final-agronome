from app.model.hlmodel import Usuario, SessionUser
#import jwt
import datetime
from flask import jsonify
from app.repositorio.repositorioUsuario import getUsuarioByName

def login(data):
    if not data:
        return('Data vacio')

    usuario = getUsuarioByName(data.get('usuario'))
    token = jwt.encode({usuario.cod, datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, 'secret')
    print(token)
    if not usuario:
        return ('Usuario no existente')


    if (data.get('contrasenia')==usuario.contraseniaUsuario):
        #Generar un token y almacenar los datos en la tabla Session
        token = jwt.encode({usuario.cod, datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, 'secret')
        #Crear objeto Session
        SessionUser(codPublic = usuario.cod, usuario = usuario.nombre, token = token, rol = usuario.rol.nombre)
        return jsonify({'token' : token.decode('UTF-8')})

    return True
