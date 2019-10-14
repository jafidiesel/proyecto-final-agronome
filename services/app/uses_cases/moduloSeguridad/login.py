from app.model.hlmodel import Usuario, SessionUser
import jwt
import datetime
from flask import jsonify
from app.repositorio.repositorioUsuario import getUsuarioByName
from app.repositorio.hlDb import saveEntidadSinCommit,Commit, Rollback,deleteObject
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
import uuid
from werkzeug.security import check_password_hash

def login(data):
    try:
        if not data:
            raise Exception('N', 'Data vacio')
        #Buscar Usuario 
        usuarioRst = getUsuarioByName(data.get('usuario'))
        # contraseniaCheck = check_password_hash(data.get('contraseniaUsuario'),contraseniaRst)
        # print(contraseniaCheck)
        if (data.get('contraseniaUsuario')== usuarioRst.contraseniaUsuario):
            print('EN IF')
            #Generar un token y almacenar los datos en la tabla Session
            #Armado de Token            
            payload = {'user': usuarioRst.usuario,'rol': usuarioRst.rol.nombre,'jti':str(uuid.uuid4()), 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
            tokenRst = jwt.encode(payload, 'AgronomeKey', algorithm='HS256')
            #Verificar si el Usuario ya existe en Session
            try:
                sessionUserRst = SessionUser.query.filter(SessionUser.codPublic == usuarioRst.cod).one()
                #Si el usuario ya tiene sesion, actualizar token
                sessionUserRst.token = tokenRst
                saveEntidadSinCommit(sessionUserRst)
            except Exception as e:
                #Si no se encontro sesion, crear objeto Session
                session = SessionUser(codPublic = usuarioRst.cod, usuario = usuarioRst.usuario, token = tokenRst, rol = usuarioRst.rol.nombre)
                saveEntidadSinCommit(session)
            
            
            """ if sessionUserRst:
                sessionUserRst.token = tokenRst
                saveEntidadSinCommit(sessionUserRst) """
           
            Commit()
            return jsonify({'token' : tokenRst.decode('UTF-8')})
        else:
            return jsonify({'message': 'User or Password invalid'})
    except Exception as e:
        Rollback()
        return ResponseException(e)

def logout(userCode): 
    try:   
        sessionUserRst = SessionUser.query.filter(SessionUser.codPublic == userCode).one()
        deleteObject(sessionUserRst) 
        Commit()
        return jsonify({'message' : 'Logout exitoso'})
    except Exception as e:
        Rollback()
        return ResponseException(e)
