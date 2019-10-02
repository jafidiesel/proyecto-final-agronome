from app.model.modelImport import *

class Usuario(db.Model):
    __tablename__ = 'usuario'
    cod = db.Column('cod_usuario',Integer,primary_key = True,index = True)
    codPublic = db.Column('cod_public_usuario', String(40), nullable = False)
    usuario = db.Column('usuario', String(80), nullable = False, unique = True)
    nombre = db.Column('nombre_usuario', String(80), nullable = False)
    apellido = db.Column('apellido_usuario', String(80), nullable = False)
    email = db.Column('email_usuario', String, nullable = False, unique = True)
    contraseniaUsuario = db.Column('contrasenia_usuario', String(80), nullable= False)
    fchCrea = db.Column('fchCrea_usuario', DateTime)
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
            fchCrea = json.get('fchCrea'),
            isActiv = json.get('isActiv')
            )
        return usuario

    