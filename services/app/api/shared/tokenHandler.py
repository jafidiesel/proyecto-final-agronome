from functools import wraps
from flask import jsonify, request, make_response
import jwt
from app.model.hlmodel import Usuario
import json
from flask_restplus import Resource

def token_required(f):
    @wraps(f)
    def decorated(*args, **kargs):
        print(kargs)
        print(request.headers.items)
        print(request.headers.get('Authorization'))
        
        token = None
        if 'Authorization' in request.headers.keys():
            token = get_token(request.headers.get('Authorization')) 
            
        if not token:
            message = json.dumps({'message': 'Token is missing'})   
            return make_response(jsonify(message),400)
        try:
            data = jwt.decode(token,'AgronomeKey')
            currentUser = Usuario.query.filter(Usuario.usuario == data.get('user')).first()   
            payload = request.json 
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({'message':'Sesion caducada. Por favor, inicie sesion nuevamente'}),400)
        except jwt.InvalidTokenError:
            return make_response(jsonify({'message':'Token invalido.Por favor, inicie sesion nuevamente'}),400)
        except:
            return make_response(jsonify({'message': 'Usuario no encontrado'}),400)      
        return f(payload,currentUser, **kargs)
    return decorated

PREFIX = 'Bearer'

def get_token(header):
    print('HEADER')
    print(header)
    bearer, _, token = header.partition(' ')
    if bearer != PREFIX:
        raise ValueError('Invalid token')
    return token
