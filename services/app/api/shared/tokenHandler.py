from functools import wraps
from flask import jsonify, request, make_response
import jwt
from app.model.hlmodel import Usuario
import json

def token_required(f):
    @wraps(f)
    def decorated(*args, **kargs):
        print(request.headers.get('Authorization'))
        token = None
        if 'Authorization' in request.headers.keys():
            token = get_token(request.headers.get('Authorization')) 
            
        if not token:
            message = json.dumps({'message': 'Token is missing'})   
            return jsonify(message)
        try:
            data = jwt.decode(token,'AgronomeKey')
            currentUser = Usuario.query.filter(Usuario.usuario == data.get('user')).first()    
        except jwt.ExpiredSignatureError:
            return jsonify({'message':'Sesion caducada. Por favor, inicie sesion nuevamente'})
        except jwt.InvalidTokenError:
            return jsonify({'message':'Token invalido.Por favor, inicie sesion nuevamente'})
        except:
            return jsonify({'message': 'Usuario no encontrado'})      
        return f(currentUser, *args, **kargs)
    return decorated

PREFIX = 'Bearer'

def get_token(header):
    print('HEADER')
    print(header)
    bearer, _, token = header.partition(' ')
    if bearer != PREFIX:
        raise ValueError('Invalid token')
    return token
