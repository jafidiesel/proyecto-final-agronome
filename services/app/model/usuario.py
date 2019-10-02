from app.model.modelImport import *

class Usuario(db.Model):
    __tablename__ = 'usuario'
    cod = db.Column('cod_usuario',Integer,primary_key = True,index = True)
    codPublic = db.Column('cdo_public_usuario', String(40), nullable = False)
    nombre = db.Column('nombre_usuario', String(80), nullable = False, unique = True)
    email = db.Column('email_usuario', String, nullable = False, unique = True)
    contraseniaUsuario = db.Column('contrasenia_usuario', String(80), nullable= False)
    fchCrea = db.Column('fchCrea_usuario', DateTime)
    randomContrasenia = db.Column('random_contrasenia_usuario', String(80))
    isRecuperarContrasenia = db.Column('is_recuperar', Boolean)
    codRol = db.Column('fk_cod_rol',Integer,ForeignKey('rol.cod_rol'),index = True)


    rol = relationship('Rol', backref ='usuario')

    @staticmethod
    def from_json(json):
        usuario = Usuario(
            nombre=json.get('nombre'),
            email=json.get('email'),
            contraseniaUsuario = json.get('contraseniaUsuario'),
            fchCrea = json.get('fchCrea'),
            codPublic = "sjakldjald"
            )
        return usuario