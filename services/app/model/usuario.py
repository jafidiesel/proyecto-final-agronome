from app.model.modelImport import *
from datetime import datetime
import jwt
import uuid
from flask import jsonify, request, make_response
import json
class Usuario(db.Model):
    __tablename__ = 'usuario'
    codPrivate = db.Column('cod_usuario_private',Integer,primary_key = True,index = True)
    cod = db.Column('cod_usuario', String(40), nullable = False)
    usuario = db.Column('usuario', String(80), nullable = False, unique = True)
    nombre = db.Column('nombre_usuario', String(80), nullable = False)
    apellido = db.Column('apellido_usuario', String(80), nullable = False)
    email = db.Column('email_usuario', String, nullable = False, unique = True)
    contraseniaUsuario = db.Column('contrasenia_usuario', String(80), nullable= False)
    fchCrea = db.Column('fchCrea_usuario', Date)
    randomContrasenia = db.Column('random_contrasenia_usuario', String(80))
    isRecuperarContrasenia = db.Column('is_recuperar', Boolean)
    codRol = db.Column('fk_cod_rol',Integer,ForeignKey('rol.cod_rol'),index = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

    rol = relationship('Rol', backref ='usuario')
    
    @staticmethod
    def from_json(json):
        usuario = Usuario(
            usuario = json.get('usuario'),
            nombre=json.get('nombre'),
            apellido = json.get('apellido'),
            email=json.get('email'),
            contraseniaUsuario = json.get('contraseniaUsuario'),
            fchCrea = datetime.strptime(json.get('fchCrea'),'%d-%m-%Y').date(),
            isActiv = json.get('isActiv')
            )
        return usuario

    def toJson(self):
        return {
            'usuario': self.usuario,
            'cod' : self.cod,
            'nombre' : self.nombre,
            'apellido' : self.apellido,
            'email' : self.email,
            'fchCrea' : self.fchCrea.strftime('%d-%m-%Y'),
            'isActiv' : self.isActiv,
            'rol': self.rol.to_json_simple(),
        }


    def getToken(self,expirationTime): 
        payload = {'user': self.usuario,'rol': self.rol.nombre,'jti':str(uuid.uuid4()), 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expirationTime)}
        tokenRst = jwt.encode(payload, 'AgronomeKey', algorithm='HS256')
        return tokenRst

    def getResetToken(self, expirationTime):
        payload = {'user': self.usuario,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expirationTime)}
        tokenRst = jwt.encode(payload, 'AgronomeKey', algorithm='HS256')
        return tokenRst

    @staticmethod
    def verify_reset_token(token):
        token = None
        if 'Authorization' in request.headers.keys():
            token = Usuario.get_token(request.headers.get('Authorization')) 
        if not token:
            message = json.dumps({'message': 'Token is missing'})   
            return make_response(jsonify(message),400)
        try:
            data = jwt.decode(token,'AgronomeKey')
            currentUser = Usuario.query.filter(Usuario.usuario == data.get('user')).first()   
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({'message':'Sesion caducada. Por favor, inicie sesion nuevamente'}),400)
        except jwt.InvalidTokenError:
            return make_response(jsonify({'message':'Token invalido.Por favor, inicie sesion nuevamente'}),400)
        except:
            return make_response(jsonify({'message': 'Usuario no encontrado'}),400)
        return currentUser    

    @staticmethod
    def get_token(header):
        PREFIX = 'Bearer' 
        #print('HEADER')
        #print(header)
        bearer, _, token = header.partition(' ')
        if bearer != PREFIX:
            raise ValueError('Invalid token')
        return token

    

    