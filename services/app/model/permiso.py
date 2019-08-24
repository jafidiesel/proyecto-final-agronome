from app.model.modelImport import *

class Permiso(db.Model):
    __tablename__ = 'permiso'
    codPermiso = db.Column('cod_permiso',  Integer,primary_key = True,index = True)
    nombrePermiso = db.Column('nombre_permiso', String(60), nullable = False,  unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    
    def __init__(self, nombrePermiso, isActiv):
        self.nombrePermiso = nombrePermiso
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        permiso = Permiso(
            nombrePermiso=json.get('nombrePermiso'),
            isActiv=json.get('isActiv')
            )
        return permiso

    def to_json(self):
        return {
            'codPermiso': self.codPermiso,
            'nombrePermiso': self.nombrePermiso,
            'isActiv': self.isActiv
        }