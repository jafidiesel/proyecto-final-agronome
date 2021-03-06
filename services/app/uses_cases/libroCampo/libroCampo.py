from app.model.hlmodel import LibroCampo
from app.uses_cases.libroCampo.hlLibroCampoToDict import libroCampoListFullToDict
from app.uses_cases.moduloRecomendacion.registrarRecomendacion import recomendacionActividad
from app.repositorio.repositorioLibroCampo import selectLibroCod
from app.repositorio.repositorioGestionarFinca import selectFincaCod
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.repositorio.hlDb import saveEntidadSinCommit, Commit, Rollback

from app.api.helperApi.hlResponse import ResponseException, ResponseOk, ResponseOkmsg
import datetime

def consultarLibroCampo(data):
    try:
        dtoLibroCampoList = hlLibroCampoList(data)
        return dtoLibroCampoList
    except Exception as e:
        return ResponseException(e)

def finalizarLibroCampo(data):
    try:
        codLibroCampo = data.get('codLibroCampo')
        fchFinAux = datetime.datetime.now()
        libroCampo = selectLibroCod(codLibroCampo)
        
        if libroCampo == None:
            raise Exception('N','No se encuentra un libro de campo con codLibroCampo ' + str(codLibroCampo))
        
        fchIni = libroCampo.fchIni
        fchFin = libroCampo.fchFin
        
        if fchFin != None:
            raise Exception('N','El libro de campo se encuentra finalizado')
        print(fchIni)
        if fchIni > fchFinAux:
            raise Exception('N','El libro de campo se no se puede finalizar, ya que su fecha de inicio es mayor a la fecha actual')

        libroCampo.fchFin = fchFinAux

        hlFinUltimaPlanif(libroCampo.grupoPlanificacion) ##finaliza la ulitma planif


        Commit()
        return ResponseOkmsg('Libro de campo finalizado correctamente')
    except Exception as e:
        Rollback()
        return ResponseException(e)


def recomendacionLibroCampo(data):
    try:
        dtoLibroCampoList = hlLibroCampoList(data)
        dtoResultList = []
        for dtoLibroCampo in dtoLibroCampoList:
            dtoResult = dtoLibroCampo
            codLibroCampo = dtoLibroCampo.get('codLibroCampo')
            dtoJsonAux = dict(
                codLibroCampo = codLibroCampo
            )

            dtoActividadRecomendacion = recomendacionActividad(dtoJsonAux)

            actvidadesARecomendar = dtoActividadRecomendacion.get('actvidadesARecomendar')
            actividadesRecomendadas = dtoActividadRecomendacion.get('actividadesRecomendadas')

            cantARE = len(actvidadesARecomendar)
            cantRE  = len(actividadesRecomendadas)

            dtoResult['actvidadesARecomendar'] = cantARE
            dtoResult['actividadesRecomendadas'] = cantRE
            
            dtoResultList.append(dtoResult)
        return dtoResultList
    except Exception as e:
        return ResponseException(e)


def createLibroCampo(nombreLibroCampo,finca,grupoPlanificacion,cultivo):
    try:
        libroCampo = LibroCampo(nombreLibroCampo = nombreLibroCampo)

        #asociaciones, en caso de que no me manden el objeto hay que buscarlo por cod y asociarlo
        libroCampo.cultivo = cultivo
        libroCampo.grupoPlanificacion = grupoPlanificacion
        finca.libroCampoList.append(libroCampo)
        saveEntidadSinCommit(finca)
        saveEntidadSinCommit(libroCampo)             
        Commit()

        return ResponseOkmsg('Libro de campo ' + nombreLibroCampo +'creado correctamente')
    except Exception as e:
        return ResponseException(e)


def hlLibroCampoList(data):
    codFinca = data.get('codFinca')
    finca = selectFincaCod(codFinca)
    if not finca:
        raise Exception('N','No se encuentra ninguna finca')
    
    libroCampoList = finca.libroCampoList
    if len(libroCampoList) == 0:
        raise Exception('N','La finca ' + finca.nombreFinca + ' no posee libros de campo')

    dtoLibroCampoList = libroCampoListFullToDict(libroCampoList)
    return dtoLibroCampoList


def hlFinUltimaPlanif(grupoPlanificacion):
    planifList = grupoPlanificacion.planificaciones
    cant = len(planifList) - 1 #ya que empieza a contar desde el cero 
    planificación = planifList[cant]
    estadoFinalizado = getNomencladoCod('estadoPlanificacion',2)
    planificación.estadoPlanificacion = estadoFinalizado
    saveEntidadSinCommit(planificación)
    return 