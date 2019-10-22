from app.api.helperApi.hlResponse import ResponseException
from app.model.hlmodel import Finca, Parcela, Cuadro
from app.repositorio.hlDb import saveEntidadSinCommit, Commit
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca
from app.api.helperApi.hlResponse import ResponseException, ResponseOk

def postFinca(data):
    try:
        nombreFinca =data.get('nombre')
        superficie = data.get('superficie')
        parcelaList = data.get('parcelas')
        calle = data.get('calle')
        nro = data.get('nro')
        localidad = data.get('localidad')
        provincia = data.get('provincia')

        isActiv = True
       
        finca = Finca(nombreFinca = nombreFinca, superficie = superficie ,isActiv = isActiv, calle=calle, nro=nro, localidad=localidad, provincia = provincia)
        
        for parcelaItem in parcelaList:
            nombreParcela = parcelaItem.get('nombre')
            superficieParcela = parcelaItem.get('superficie')
            filas = parcelaItem.get('filas')
            columnas = parcelaItem.get('columnas')

            parcela = Parcela(nombrePacela = nombreParcela, superficieParcela=superficieParcela, filas =filas,columnas=columnas)

            #Cuadros
            for i in range(1,(filas+1)):
                for j in range(1,(columnas+1)):
                    nombreCuadro = nombreParcela + str(i) + str(j)
                    cuadro = Cuadro(nombreCuadro=nombreCuadro)    

                    parcela.cuadroList.append(cuadro) #asociacion de parcela -> cuadro

            finca.parcelaList.append(parcela) #asociacion de finca -> parcela
        
        saveEntidadSinCommit(finca)
        Commit()

        return ResponseOk()
    except Exception as e:
        return ResponseException(e)

def getFinca():
    fincaList = selectFinca()
    dtoFincaList = []

    for finca in fincaList:
        dtoFincaAux = fincaToDicc(finca)
        dtoFincaList.append(dtoFincaAux)

    return dict(finca=dtoFincaList)

def getFincaCod(codFinca):
    try:    
        finca = selectFincaCod(codFinca)
        if not finca: 
            raise Exception('N','No existe finca con código ' + str(codFinca))

        dtoFinca = fincaToDicc(finca)
        parcelaList = finca.parcelaList
        dtoParcelaList = []

        for parcela in parcelaList:
            dtoParcelaAux = dict(codParcela = parcela.codParcela, nombre = parcela.nombrePacela, superficie = str(parcela.superficieParcela) + ' m', filas= parcela.filas, columnas = parcela.columnas, cantCuadros = parcela.filas * parcela.columnas)

            cuadroList = parcela.cuadroList
            dtoCuadroList = []
            for cuadro in cuadroList:
                dtoCuadroAux = dict(codCuadro = cuadro.codCuadro, nombreCuadro = cuadro.nombreCuadro)    
                dtoCuadroList.append(dtoCuadroAux)

            dtoParcelaAux['cuadros'] = dtoCuadroList
            dtoParcelaList.append(dtoParcelaAux)

        dtoFinca['parcelas'] = dtoParcelaList

        return (dict(finca=dtoFinca))       
    except Exception as e:
        return ResponseException(e)



def fincaToDicc(finca):
    calle = finca.calle
    nro = finca.nro
    localidad = finca.localidad
    provincia = finca.provincia
    urlMaps = adapterUrl(calle,nro,localidad,provincia)

    dtoFinca = dict(codFinca = finca.codFinca, nombre = finca.nombreFinca, superficie = finca.superficie, isActiv = finca.isActiv, calle= calle, nro = nro, localidad=localidad, provincia=provincia, urlMaps = urlMaps)
    return dtoFinca


def adapterUrl(calle,nro,localidad,provincia):
    urlMaps = 'https://www.google.com.ar/maps/place/' + calle + '+' + str(nro) + '+' + localidad + '+' + provincia
    urlMaps = urlMaps.replace(' ','+')
    return urlMaps
