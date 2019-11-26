from app.model.hlmodel import LibroCampo
from app.uses_cases.libroCampo.hlLibroCampoToDict import libroCampoListFullToDict
from app.repositorio.repositorioLibroCampo import selectLibroCod
from app.repositorio.repositorioGestionarFinca import selectFincaCod
from app.repositorio.hlDb import saveEntidadSinCommit, Commit
from app.api.helperApi.hlResponse import ResponseException, ResponseOk, ResponseOkmsg
import datetime
def getLibroCampo(data):
    try:
        codFinca = data.get('codFinca')

        finca = selectFincaCod(codFinca)
        if not finca:
            raise Exception('N','No se encuentra finca con codFinca ' + str(codFinca))

        libroCampoList = finca.libroCampoList

        dtoLibroCampoList = libroCampoListFullToDict(libroCampoList)

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
        Commit()
        return ResponseOkmsg('Libro de campo finalizado correctamente')
    except Exception as e:
        return ResponseException(e)


def createLibroCampo(nombreLibroCampo,finca,grupoPlanificacion,cultivo):
    try:
        libroCampo = LibroCampo(nombreLibroCampo = nombreLibroCampo)

        #asociaciones, en caso de que no me manden el objeto hay que buscarlo por cod y asociarlo
        libroCampo.cultivo = cultivo
        libroCampo.grupoPlanificacion = grupoPlanificacion
        saveEntidadSinCommit(libroCampo)
        Commit()

        return ResponseOkmsg('Libro de campo ' + nombreLibroCampo +'creado correctamente')
    except Exception as e:
        return ResponseException(e)
