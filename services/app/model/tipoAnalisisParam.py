from app.model.modelImport import *

class TipoAnalisisParam(db.Model):
    __tablename__ = 'tipo_analisis_param'
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codParametro = db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'),index = True, primary_key=True)
    codTipoAnalisis = db.Column('fk_cod_tipo_analisis',Integer,ForeignKey('tipo_analisis.cod_tipo_analisis'),index = True, primary_key=True)
    
    tipoAnalisis = relationship("TipoAnalisis", backref="tipoAnalisisParamList") #n->1
    parametro = relationship("Parametro", backref="paramTipoAnalisisList") #n->1
    
    
    #def __init__(self,isActiv,codParam,codTipoAnalisis):
    #    self.isActiv = isActiv
    #    self.codParametro = codParam
    #    self.codTipoAnalisis = codTipoAnalisis

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