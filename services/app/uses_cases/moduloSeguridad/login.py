from app.model.hlmodel import Usuario, SessionUser
import jwt
import datetime
from flask import jsonify,make_response
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
        if (data.get('contraseniaUsuario')== usuarioRst.contraseniaUsuario):
            print('EN IF')
            #Generar un token y almacenar los datos en la tabla Session
            #Armado de Token        
            tokenRst = usuarioRst.getToken(5) 
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
            nombre =  usuarioRst.nombre + ' ' + usuarioRst.apellido 
            rol = usuarioRst.rol.nombre
            dtoUsuario = dict(nombre=nombre, rol = rol, token = tokenRst.decode('UTF-8'))

            if not rol =="administrador":
                fincaUsuarioList = usuarioRst.fincaUsuarioList
                dtoFincaList = []

                for fincaUsuario in fincaUsuarioList:
                    dtoFincaAux= dict(codFinca=fincaUsuario.finca.codFinca, nombreFinca= fincaUsuario.finca.nombreFinca)
                    dtoFincaList.append(dtoFincaAux)

                dtoUsuario['finca'] = dtoFincaList

            
            return dtoUsuario
            #return jsonify({'token' : tokenRst.decode('UTF-8'), 'rol': usuarioRst.rol.nombre})
        else:
            return make_response(jsonify({'message': 'User or Password invalid'}),400)
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

def solicitarReinicioPsw(data):
    #Comprobar que el usuario existe
    usuarioRst = getUsuarioByName(data.get('usuario'))
    # Si existe se comprueba el email
    if (data.get('email')== usuarioRst.email):
        usuarioRst.isRecuperarContrasenia = True
        #Generar contraseña random
        import string
        import random
        usuarioRst.randomContrasenia = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))    
        #Generar token de 24hs para reestablecer contraseña
        payload = {'user': usuarioRst.usuario,'jti':str(uuid.uuid4()), 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2)}
        tokenRst = jwt.encode(payload, 'AgronomeKey', algorithm='HS256')
        Commit()
        return jsonify({'contrasenia': usuarioRst.randomContrasenia })
    else:
        return make_response(jsonify({'message': 'El e-mail ingresado no es válido'}),400)

def resetPsw(data):
    #Buscar el usuario del token
    #
    #Verificar que el token no expiro
    return True