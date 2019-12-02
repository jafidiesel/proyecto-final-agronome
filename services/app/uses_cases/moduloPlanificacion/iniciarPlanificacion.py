from app.repositorio.hlDb import Rollback,saveEntidadSinCommit,selectActiveByName,saveEntidad, selectAll, selectByCod, updateEntidad, selectByisActiv,Commit
from app.model.hlmodel import Cultivo,TipoCultivo,TipoPlanificacion,Planificacion,GrupoPlanificacion,Finca, Parcela, Cuadro, EstadoPlanificacion, GrupoCuadro, CuadroCultivo, Cuadro
from app.uses_cases.moduloPlanificacion.shared.sharedFunctions import tipoCultivoListToDict, planificacionToDict
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca
from app.repositorio.repositorioPlanificacion import getCuadroByCod, getParcelaByCod
from flask import jsonify,make_response,json
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict


def getParcelasLibres(data):    
    def getCuadrosLibres(elemento, datoParcelaGeneral):    
        if datoParcelaGeneral.__getitem__(0) == elemento.__getitem__(0):
            cuadrosParcelaGeneral = datoParcelaGeneral.__getitem__(1)            
            cuadrosParcelaOcupada = elemento.__getitem__(1)                 
            cuadrosNoRepetidos =set(cuadrosParcelaGeneral) - set(cuadrosParcelaOcupada)
            if cuadrosNoRepetidos:
                dtoParcelaLibre.append(datoParcelaGeneral.__getitem__(0))
                dtoParcelaLibre.append(list(cuadrosNoRepetidos))
            dtoGeneralLibre.append(dtoParcelaLibre)

    #Extraer Finca de Json
    codFincaJson = data
    print(codFincaJson)
    #Buscar Finca
    fincaRst = selectFincaCod(codFincaJson)
    if not fincaRst: 
        raise Exception('N','No existe finca con código ' + str(codFincaJson))
    #Buscar Parcelas asociadas
    parcelasRstList = fincaRst.parcelaList
    print(parcelasRstList)
    if not parcelasRstList:
        raise Exception('N',"La finca no posee parcelas configuradas")
    dtoGeneral = []
    #Dto de parcelas con sus respectivos cuadros
    #Por cada parcela, leer cuadro asociado
    for parcelaRst in parcelasRstList:
        dtoParcela = []
        dtoParcela.append(parcelaRst)
        dtoParcela.append(parcelaRst.cuadroList)
        dtoGeneral.append(dtoParcela)  
    print('Parcelas')
    print(dtoGeneral)
    #Leer instancias Grupo asociadas a Finca instanciada.
    grupoList = fincaRst.grupoPlanificacionList
    print('Grupo')
    print(grupoList)
    if not grupoList:
        return dtoGeneral
    elif grupoList:
        #Leer planificaciones asociadas al Grupo
        print(grupoList)
        #Parcelas repetidas en los grupos
        parcelasTmp = [] #Para agrupar las parcelas iguales que estan presentes en varias planificaciones
        dtoGeneralOcupada = []
        for grupoPlanificacion in grupoList:    
            planificacionListRst = grupoPlanificacion.planificaciones
            print('PLANIFICACIONES GRUPO')
            print(planificacionListRst)
                        
            #Por cada planificacion del grupo
            for planificacionRst in planificacionListRst:
                if (planificacionRst.estadoPlanificacion.cod == 1):
                    print('TIPOPLANIFICACION')
                    print(planificacionRst)
                                
                    for grupoCuadro in planificacionRst.grupoCuadroList:
                        dtoParcelaOcupada = []    
                        parcelaOcupada = grupoCuadro.parcela
                        #Lista de parcelas ocupadas vacia
                        if not parcelasTmp or (parcelaOcupada not in parcelasTmp):
                            parcelasTmp.append(parcelaOcupada)
                            dtoParcelaOcupada.append(parcelaOcupada)                            
                            cuadrosOcupados = []
                            for cuadroCultivo in grupoCuadro.cuadroCultivoList:
                                cuadroOcupado = cuadroCultivo.cuadro
                                cuadrosOcupados.append(cuadroOcupado)
                            dtoParcelaOcupada.append(cuadrosOcupados)
                            dtoGeneralOcupada.append(dtoParcelaOcupada) 
                        #Lista con elementos
                        if parcelasTmp:
                            #Si la lista no esta vacia, buscar parcela
                            if parcelaOcupada in parcelasTmp:
                                for elemento in dtoGeneralOcupada:
                                    if (parcelaOcupada == elemento.__getitem__(0)):
                                        cuadrosTmp = elemento.__getitem__(1)
                                        #Comparar los cuadros de la parcela ocupada con los cuadros de la parcela ya guardada
                                        #Cuadros de la parcela ocupada
                                        for cuadroCultivo in grupoCuadro.cuadroCultivoList:
                                            if cuadroCultivo.cuadro not in cuadrosTmp:
                                                elemento.__getitem__(1).append(cuadroCultivo.cuadro)    
            
        #Comparacion de listas para extraer los items que no se repiten
        dtoGeneralLibre = []       
    
        for datoParcelaGeneral in dtoGeneral:
            dtoParcelaLibre= []
            condition = (getCuadrosLibres(elemento,datoParcelaGeneral) for elemento in dtoGeneralOcupada if datoParcelaGeneral.__getitem__(0) in parcelasTmp)
            
            for x in condition:
                pass

            if datoParcelaGeneral.__getitem__(0) not in parcelasTmp:
                dtoGeneralLibre.append(datoParcelaGeneral)               
        print(dtoGeneralLibre)  
        return dtoGeneralLibre

        
def getParcelas(data):
    try:
        parcelaLibreList = getParcelasLibres(data)
        dtoParcelasLibres = []
        if not parcelaLibreList:
            raise Exception('N','No hay cuadros disponibles')
        if parcelaLibreList:
            for parcelaLibre in parcelaLibreList:        
                dtoCuadrosLibre = []
                for cuadroLibre in parcelaLibre.__getitem__(1):
                    cuadroDto = cuadroLibre.__dict__
                    cuadroDto.pop('_sa_instance_state', None)
                    cuadroDto.pop('codParcela', None)
                    dtoCuadrosLibre.append(cuadroDto)
                parcela = parcelaLibre.__getitem__(0)
                dtoParcelaAux = dict(codParcela = parcela.codParcela, nombre = parcela.nombrePacela, superficie = str(parcela.superficieParcela) + ' m', filas= parcela.filas, columnas = parcela.columnas, cantCuadros = parcela.filas * parcela.columnas, cuadros = dtoCuadrosLibre)
                dtoParcelasLibres.append(dtoParcelaAux)
            dtoParcelas = dict(parcelas = dtoParcelasLibres)
            return jsonify(dtoParcelas)
    except Exception as e:
        return ResponseException(e)





        