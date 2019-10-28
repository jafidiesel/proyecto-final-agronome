from app.repositorio.hlDb import saveEntidadSinCommit, Commit
from app.uses_cases.analisis.hlAnalisis import createAnalisis
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.repositorio.repositorioGestionarAnalisis import selectAnalisisCod
from app.uses_cases.hlToDict import analisisFullToDicc
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