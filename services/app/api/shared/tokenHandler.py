from functools import wraps
from flask import jsonify, request, make_response
import jwt
from app.model.hlmodel import Usuario
from app import app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token,'secretkey')
            currentUser = Usuario.query.filter(Usuario.cod == data.get('cod')).first()
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        
        return f(currentUser, *args, **kargs)
    return decorated

