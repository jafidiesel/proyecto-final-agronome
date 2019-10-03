from app.model.modelImport import *
from datetime import datetime

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
            fchCrea = datetime.strptime(json.get('fchCrea'),'%d/%m/%Y').date(),
            isActiv = json.get('isActiv')
            )
        return usuario

    def toJson(self):
        return {
            'usuario': self.usuario,
            'contraseniaUsuario' : self.contraseniaUsuario,
            'nombre' : self.nombre,
            'apellido' : self.apellido,
            'email' : self.email,
            'fchCrea' : self.fchCrea.strftime('%d/%m/%Y'),
            'isActiv' : self.isActiv
        }
    