from app.model.modelImport import *

class Opcion(db.Model):
    __tablenombreOpcion__ = 'opcion'
    codOpcion = db.Column('cod_opcion',Integer, primary_key = True, index=True)
    nombreOpcion = db.Column('nombre_opcion',String(60), nullable=False,unique=True)
    isActiv = db.Column('is_activ',Boolean,nullable=True)


    def __init__(self, nombreOpcion, isActiv):
        self.nombreOpcion = nombreOpcion
        self.isActiv = isActiv
    

    @staticmethod
    def from_json(json):
        opcion = Opcion(
            nombreOpcion=json.get('nombreOpcion'),
            isActiv=json.get('isActiv')
            )
        return opcion

    def to_json(self):
        return {
            'codOpcion': self.codOpcion,
            'nombreOpcion': self.nombreOpcion,
            'isActiv': self.isActiv
        }
