from app.model.modelImport import *

class TipoPlanParam(db.Model):
    __tablename__ = 'tipo_plan_param'
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codParametro = db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'),index = True, primary_key = True)
    codTipoPlan = db.Column('fk_cod_tipo_plan',Integer,ForeignKey('tipo_plan.cod_tipo_plan'),index = True, primary_key = True)

    def __init__(self,isActiv,codParam,codTipoPlan):
        self.isActiv = isActiv
        self.codParametro = codParam
        self.codTipoPlan = codTipoPlan

    @staticmethod
    def from_json(json):
        tipoPlanParam = TipoPlanParam(
            isActiv=json.get('isActiv')
            )
        return tipoPlanParam

    def to_json(self):
        return {
            'isActiv': self.isActiv
        }