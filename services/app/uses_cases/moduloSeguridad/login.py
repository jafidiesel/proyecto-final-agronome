from app.model.hlmodel import Usuario, SessionUser
#import jwt
import datetime
from flask import jsonify
from app.repositorio.repositorioUsuario import getUsuarioByName
from app.repositorio.hlDb import saveEntidadSinCommit,Commit, Rollback
from app.api.helperApi.hlResponse import ResponseException, ResponseOk

def login(data):
    try:
        if not data:
            return('Data vacio')
        #Buscar Usuario 
        usuarioRst = getUsuarioByName(data.get('usuario'))
        
        if not usuarioRst:
            return ('Usuario no existente')

        if (data.get('contrasenia')==usuarioRst.contraseniaUsuario):
            #Verificar si el Usuario ya existe en Session
            sessionUserRst = SessionUser.query.filter(SessionUser.codPublic == usuarioRst.cod).one()
            #Generar un token y almacenar los datos en la tabla Session
            payload = {'user': usuarioRst.usuario}
            print(payload)
            tokenRst = jwt.encode(payload, 'AgronomeKey', algorithm='HS256')
            print('Token')
            print(tokenRst)

            #Si el usuario ya tiene sesion, actualizar token
            if sessionUserRst:
                sessionUserRst.token = tokenRst
                saveEntidadSinCommit(sessionUserRst)
           
            #Si no se encontro sesion, crear objeto Session
            if not sessionUserRst:
                session = SessionUser(codPublic = usuarioRst.cod, usuario = usuarioRst.usuario, token = tokenRst, rol = usuarioRst.rol.nombre)
                saveEntidadSinCommit(session)
            Commit()
            return jsonify({'token' : tokenRst.decode('UTF-8')})
    except Exception as e:
        Rollback()
        return ResponseException(e)
