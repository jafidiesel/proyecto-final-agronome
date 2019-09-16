from app.model.modelImport import *

class TipoAnalisisParam(db.Model):
    __tablename__ = 'tipo_analisis_param'
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codParametro = db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'),index = True, primary_key=True)
    codTipoAnalisisParam = db.Column('fk_cod_tipo_analisis',Integer,ForeignKey('tipo_analisis.cod_tipo_analisis'),index = True, primary_key=True)
    
    def __init__(self,isActiv,codParam,codTipoAnalisis):
        self.isActiv = isActiv
        self.codParametro = codParam
        self.codTipoAnalisisParam = codTipoAnalisis

    @staticmethod
    def from_json(json):
        tipoAnalisisParam = TipoAnalisisParam(
            isActiv=json.get('isActiv')
            )
        return tipoAnalisisParam

    def to_json(self):
        return {
            'isActiv': self.isActiv
        }