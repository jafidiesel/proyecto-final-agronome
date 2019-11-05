from app.repositorio.hlDb import saveEntidadSinCommit, Commit
from app.uses_cases.plan.hlPlan import createPlan
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.repositorio.repositorioGestionarPlan import selectPlanCod
from app.uses_cases.hlToDict import planFullToDict, parametroListFullToDict
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
##OBJETO HELPER

def postPlan(data,currentUser):
    try:
        planList = data.get('plan')

        for planJson in planList:
            plan = createPlan(planJson,currentUser)
            saveEntidadSinCommit(plan)

        Commit()
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)

def getPlanCod(data,codPlan):
    try:
        plan = selectPlanCod(codPlan)
        if not plan:
            raise Exception('N','No existe el plan con codigo: ' + str(codPlan))
        dtoPlan = planFullToDict(plan)
        return dtoPlan
    except Exception as e:
        return ResponseException(e)


def getParamPlanFull(data,codTipoPlan):
    try:
        tipoPlan = getNomencladoCod('tipoPlan', codTipoPlan)
        paramListObj = tipoPlan.tipoPlanParamList
        dtoParametroFull = parametroListFullToDict(paramListObj)
        return (dict(parametros=dtoParametroFull))
    except Exception as e:
        return ResponseException(e)