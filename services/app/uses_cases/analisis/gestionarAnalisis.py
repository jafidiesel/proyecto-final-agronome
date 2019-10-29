from app.repositorio.hlDb import saveEntidadSinCommit, Commit
from app.uses_cases.analisis.hlAnalisis import createAnalisis
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.repositorio.repositorioGestionarAnalisis import selectAnalisisCod
from app.uses_cases.hlToDict import analisisFullToDicc, parametroListFullToDict
def postAnalisis(data,currentUser):
    try:
        analisisList=data.get('analisis')
        
        for analisisJson in analisisList:
            analisis = createAnalisis(analisisJson,currentUser)
            saveEntidadSinCommit(analisis)

        Commit() 
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)

def getAnalisisCod(data,codAnalisis):
    try:
        analisis = selectAnalisisCod(codAnalisis)
        if not analisis:
            raise Exception('N','No existe el analisis con codigo: ' + str(codAnalisis))
        dtoAnalisis = analisisFullToDicc(analisis)
        return dtoAnalisis
    except Exception as e:
        return ResponseException(e)

def getParamAnalisisFull(data,codTipoAnalisis):
    try:
        tipoAnalisis = getNomencladoCod('tipoAnalisis',codTipoAnalisis)
        paramListObj = tipoAnalisis.tipoAnalisisParamList
        dtoParametroFull = parametroListFullToDict(paramListObj)

        return (dict(parametros=dtoParametroFull))
    except Exception as e:
        return ResponseException(e)