from app.model.modelImport import *

class Rol(db.Model):
    __tablename__ = 'rol'
    codRol = db.Column('cod_rol',  Integer,primary_key = True,index = True)
    nombreRol = db.Column('nombre_rol', String(60), nullable = False,  unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

    def __init__(self, nombreRol, isActiv):
        self.nombreRol = nombreRol
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        rol = Rol(
            nombreRol=json.get('nombreRol'),
            isActiv=json.get('isActiv')
            )
        return rol

    def to_json(self):
        return {
            'codRol': self.codRol,
            'nombreRol': self.nombreRol,
            'isActiv': self.isActiv
        }