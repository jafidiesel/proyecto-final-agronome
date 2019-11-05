from functools import wraps
from flask import request
import jwt
from app.model.hlmodel import Usuario
# import json
#from flask_restplus import Resource
from app.uses_cases.moduloSeguridad.checkUrl import checkUrl
from app.api.helperApi.hlResponse import ResponseException, notCheck

def token_required(f):
    @wraps(f)
    def decorated(*args, **kargs):
        payload = request.json
        token = None
        if 'Authorization' in request.headers.keys():
            token = get_token(request.headers.get('Authorization')) 
            
        if not token:
            return notCheck('Token is Empty')
        try:
            data = jwt.decode(token,'AgronomeKey')
            currentUser = Usuario.query.filter(Usuario.usuario == data.get('user')).first()   
            payload = request.json 
            #control de permisos
            isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
            if not isCheck:
                raise Exception('N','No posee permisos para realizar esta acción')

        #manejo de exceptiones del token
        except jwt.ExpiredSignatureError:
            return notCheck('Sesion caducada. Por favor, inicie sesion nuevamente')

        except jwt.InvalidTokenError:
            return notCheck('Token invalido.Por favor, inicie sesion nuevamente')

        #manejo de la exeption del control de permisos    
        except Exception as e:
            return ResponseException(e)       
        #return f(data,currentUser, *args, **kargs)
        return f(payload,currentUser,**kargs)
    return decorated

PREFIX = 'Bearer'

def get_token(header):
    #print('HEADER')
    #print(header)
    bearer, _, token = header.partition(' ')
    if bearer != PREFIX:
        raise ValueError('Invalid token')
    return token


                    
