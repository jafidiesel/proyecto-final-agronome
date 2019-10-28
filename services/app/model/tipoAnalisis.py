from app.model.modelImport import *

class TipoAnalisis(db.Model):
    __tablename__ = 'tipo_analisis'
    cod = db.Column('cod_tipo_analisis',  Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_tipo_analisis',String(80), nullable = False,  unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    #Relaciones OneToMany lado Many
    #tipoAnalisisParam = relationship("TipoAnalisisParam") # aca no va comentario de franco
    nombreNomenclador = "tipoAnalisis"


    

    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoAnalisis = TipoAnalisis(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return tipoAnalisis

    def to_json(self):
        return {
            'cod': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }