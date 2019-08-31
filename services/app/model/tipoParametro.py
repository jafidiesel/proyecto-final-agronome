from app.model.modelImport import *

class TipoParametro(db.Model):
    __tablename__ = 'tipo_parametro'
    cod= db.Column('cod_tipo_parametro',Integer,primary_key = True,index = True)
    nombre= db.Column('nombre_tipo_parametro', String(32), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
      
    #Relaciones OneToMany lado Many
    parametro = relationship("Parametro")

    nombreNomenclador = "tipoParametro"


    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoParametro = TipoParametro(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return tipoParametro

    def to_json(self):
        return {
            'id': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }