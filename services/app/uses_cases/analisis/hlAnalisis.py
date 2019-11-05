from app.model.hlmodel import Analisis, AnalisisParam
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod

def createAnalisis(analisisJson, currentUser):
    ##ParmIn: analisis en json y el usuario actual
    #print('create analisis')
    #print('analisisJson')
    codTipoAnalisis = analisisJson.get('codTipoAnalisis')
    fchAnalisis = analisisJson.get('fchAnalisis')
    parametroList = analisisJson.get('parametro')
    
    analisis = Analisis(fchAnalisis = fchAnalisis)
    tipoAnalisis = getNomencladoCod('tipoAnalisis',codTipoAnalisis)
    analisis.tipoAnalisis = tipoAnalisis #asociacion de tipo analisis
    analisis.usuario = currentUser

    for parametro in parametroList:
        codParametro = parametro.get('codParam')
        valor = parametro.get('valor')
        analisisParm =AnalisisParam(valor = valor)
        parametroObj = getNomencladoCod('parametro',codParametro)
        analisisParm.param = parametroObj

        analisis.paramList.append(analisisParm)

    #saveEntidadSinCommit(analisis) si lago falla descomentar pero da igual
    return analisis