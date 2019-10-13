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
            print('TOKEN')
            print(token)
            print('EN if')
        
        if not token:
            message = json.dumps({'message': 'Token is missing'})   
            return jsonify(message, status = 401)

        try:
            print('EN TRY')
            data = jwt.decode(token,'AgronomeKey')
            print(data)
            currentUser = Usuario.query.filter(Usuario.cod == data.get('cod')).first()
        except jwt.ExpiredSignatureError:
            return 'Signature expired, Please sign in again'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please sign in again' 
        except:
            message = json.dumps({'message': 'Token is invalid'})
            return jsonify(message,status=401)
        
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
