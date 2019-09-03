from app.model.modelImport import *

class Parametro(db.Model):
    __tablename__ = 'parametro'
    codParametro = db.Column('cod_parametro',Integer,primary_key = True,index = True)
    nombreParametro = db.Column('nombre_parametro', String(32), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codTipoParametro = db.Column('fk_cod_tipo_parametro',Integer,ForeignKey('tipo_parametro.cod_tipo_parametro'),index = True)
    codTipoDato = db.Column('fk_cod_tipo_dato',Integer,ForeignKey('tipo_dato.cod_tipo_dato'),index = True)
    #Relaciones OneToMany lado One
    parametroOpcion = relationship("ParametroOpcion")
    actividadParametro = relationship("ActividadParametro")
    recomendacionParametro = relationship("RecomendacionParametro")
    tipoPlanParam = relationship("TipoPlanParam")
    tipoAnalisisParam = relationship("TipoAnalisisParam")

    def __init__(self, nombreParametro, isActiv):
        self.nombreParametro = nombreParametro
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        parametro = Parametro(
            nombreParametro=json.get('nombreParametro'),
            isActiv=json.get('isActiv')
            )
        return parametro

    def to_json(self):
        return {
            'codParametro': self.codParametro,
            'nombreParametro': self.nombreParametro,
            'isActiv': self.isActiv
        }