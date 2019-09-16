from app.model.modelImport import *

class RecomendacionParametro(db.Model):
    __tablename__ = 'recomendacion_parametro'
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codParametro = db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'),index = True, primary_key=True)
    codRecomendacion = db.Column('fk_cod_recomendacion',Integer,ForeignKey('recomendacion.cod_recomendacion'),index = True, primary_key=True)
    
    def __init__(self,isActiv,codParam,codRecomen):
        self.isActiv = isActiv
        self.codParametro = codParam
        self.codRecomendacion = codRecomen

    @staticmethod
    def from_json(json):
        recomendacionParametro = RecomendacionParametro(
            isActiv=json.get('isActiv')
            )
        return recomendacionParametro

    def to_json(self):
        return {
            'isActiv': self.isActiv

        }