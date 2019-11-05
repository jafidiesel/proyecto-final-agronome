from app.extensions import db
from app.model.hlmodel import Plan



def selectPlanCod(codPlan):
    plan = Plan.query.filter(Plan.codPlan == codPlan).first()
    return plan