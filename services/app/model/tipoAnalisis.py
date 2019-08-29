from app.model.modelImport import *

class TipoAnalisis(db.Model):
    __tablename__ = 'tipo_analisis'
    codTipoAnalisis = db.Column('cod_tipo_analisis',  Integer,primary_key = True,index = True)
    nombreTipoAnalisis = db.Column('nombre_tipo_analisis',String(60), nullable = False,  unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    #Relaciones OneToMany lado Many
    tipoAnalisisParam = relationship("TipoAnalisisParam")

    def __init__(self, nombreTipoAnalisis, isActiv):
        self.nombreTipoAnalisis = nombreTipoAnalisis
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoAnalisis = TipoAnalisis(
            nombreTipoAnalisis=json.get('nombreTipoAnalisis'),
            isActiv=json.get('isActiv')
            )
        return tipoAnalisis

    def to_json(self):
        return {
            'codTipoAnalisis': self.codTipoAnalisis,
            'nombreTipoAnalisis': self.nombreTipoAnalisis,
            'isActiv': self.isActiv
        }