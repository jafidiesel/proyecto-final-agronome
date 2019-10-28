from app.model.hlmodel import Plan, PlanParam
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod


def createPlan(planJson, currentUser):
    codTipoPlan = planJson.get('codTipoPlan')
    fchPlan = planJson.get('fchPlan')
    parametroList = planJson.get('parametro')

    plan = Plan(fchPlan = fchPlan)
    tipoPlan = getNomencladoCod('tipoPlan', codTipoPlan)
    plan.tipoPlan = tipoPlan
    plan.usuario = currentUser

    for parametro in parametroList:
        codParametro = parametro.get('codParam')
        valor = parametro.get('valor')
        planParam =PlanParam(valor = valor)
        parametroObj = getNomencladoCod('parametro',codParametro)
        planParam.param = parametroObj

        plan.paramList.append(planParam)

    return plan

