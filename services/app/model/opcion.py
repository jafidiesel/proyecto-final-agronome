from app.model.modelImport import *

class Opcion(db.Model):
    __tablenombreOpcion__ = 'opcion'
    cod = db.Column('cod_opcion',Integer, primary_key = True, index=True)
    nombre = db.Column('nombre_opcion',String(60), nullable=False,unique=True)
    isActiv = db.Column('is_activ',Boolean,nullable=True)
    #Relaciones OneToMany lado Many
    #parametroOpcion = relationship("ParametroOpcion")

    #nombreNomenclador = "opcion"


    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv
    

    @staticmethod
    def from_json(json):
        opcion = Opcion(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return opcion

    def to_json(self):
        return {
            'id': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }
