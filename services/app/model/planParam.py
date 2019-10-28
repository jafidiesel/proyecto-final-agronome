from app.model.modelImport import *

class PlanParam(db.Model):
    __tablename__ = 'plan_param'

    codPlan = db.Column('fk_cod_plan', Integer, ForeignKey('plan.cod_plan'), primary_key = True)
    codParametro = db.Column('fk_cod_parametro', Integer, ForeignKey('parametro.cod_parametro') , primary_key = True)

    valor = db.Column('valor', String,nullable = False)
    param = relationship('Parametro')