from app.repositorio.hlDb import Rollback,saveEntidadSinCommit,selectActiveByName,saveEntidad, selectAll, selectByCod, updateEntidad, selectByisActiv,Commit
from app.model.hlmodel import Cultivo,TipoCultivo,TipoPlanificacion,Planificacion,GrupoPlanificacion,Finca, Parcela, Cuadro, EstadoPlanificacion, GrupoCuadro, CuadroCultivo, Cuadro
from app.uses_cases.moduloPlanificacion.shared.sharedFunctions import tipoCultivoListToDict
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca
from app.repositorio.repositorioPlanificacion import getCuadroByCod, getParcelaByCod
from flask import jsonify,make_response
from app.api.helperApi.hlResponse import ResponseException, ResponseOk


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
    #Buscar Finca
    fincaRst = selectFincaCod(codFincaJson)
    if not fincaRst: 
        raise Exception('N','No existe finca con código ' + str(codFincaJson))
    #Buscar Parcelas asociadas
    parcelasRstList = fincaRst.parcelaList
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
        
    #Leer instancias Planificación asociadas a Finca instanciada.
    planificacionListRst = fincaRst.planificacionList
    if not planificacionListRst:
        return dtoGeneral
    else:
        dtoGeneralOcupada = []
        parcelasTmp = [] #Para agrupar las parcelas iguales que estan presentes en varias planificaciones
        for planificacionRst in planificacionListRst:
            if (planificacionRst.estadoPlanificacion.nombre == "en curso" ):
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
                print('Condicion')
                print(x)
            
            if datoParcelaGeneral.__getitem__(0) not in parcelasTmp:
                dtoGeneralLibre.append(datoParcelaGeneral)               
            
        return dtoGeneralLibre
        
def iniciarPlanificacion(data):
    parcelaLibreList = getParcelasLibres(data)
    dtoParcelasLibres = []
    if not parcelaLibreList:
        return make_response(jsonify({'message:':'No existen cuadros libres'}),400)
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
            #dtoParcelaAux['cuadros'] = dtoCuadrosLibre
            dtoParcelasLibres.append(dtoParcelaAux)
        dtoParcelas = dict(parcelas = dtoParcelasLibres)
        return jsonify(dtoParcelas)


def crearPlanificacionInicial(data,currentUser):
    try:

        #Crear instancia GrupoPlanificacion 
        fincaJson = data.get("codFinca")
        nombreGrupoJson = data.get("nombreGrupo")
        comentarioJson = data.get("comentario")
        datosCultivosJsonList = data.get("cultivos")
        #parcelaListJson = data.get("parcelas")
        grupoPlanificacion = GrupoPlanificacion(nombreGrupoPlanificacion = nombreGrupoJson)
        #Buscar entidades asociadas a la Planificacion
        estadoPlanificacionRst = selectActiveByName(EstadoPlanificacion, "en curso")
        tipoPlanificacionRst = selectActiveByName(TipoPlanificacion, "inicial")
        #Crear instancia Planificacion
        planificacionInicial = Planificacion(comentarioPlanificacion = comentarioJson )
        planificacionInicial.tipoPlanificacion = tipoPlanificacionRst
        planificacionInicial.estadoPlanificacion = estadoPlanificacionRst
        fincaRst = Finca.query.filter(Finca.codFinca == fincaJson).one()
        planificacionInicial.usuario = currentUser
        saveEntidadSinCommit(planificacionInicial)
        #Asociar GrupoPlanificacion con Planificacion
        grupoPlanificacion.planificacion.append(planificacionInicial)
        saveEntidadSinCommit(grupoPlanificacion)

        #Por cada cultivo ingresado
        
        for datosCultivoJson in datosCultivosJsonList:
            tipoCultivoRst = selectActiveByName(TipoCultivo,datosCultivoJson.get("nombreTipoCultivo"))
            print(tipoCultivoRst)
            cultivoObj = Cultivo(cantidadCultivo = datosCultivoJson.get("cantidadCultivo"), produccionEsperada = datosCultivoJson.get("produccionEsperada"),variedadCultivo=datosCultivoJson.get("variedadCultivo"),cicloUnico=datosCultivoJson.get("cicloUnico"))
            saveEntidadSinCommit(cultivoObj)
            cultivoObj.tipoCultivoR = tipoCultivoRst
            for parcelaJson in datosCultivoJson.get("parcelas"):
                parcelaRst = getParcelaByCod(parcelaJson.get('codParcela'))
                grupoCuadro = GrupoCuadro()
                saveEntidadSinCommit(grupoCuadro)
                grupoCuadro.parcela = parcelaRst
                planificacionInicial.grupoCuadroList.append(grupoCuadro)
                for cuadroJson in parcelaJson.get('cuadros'):
                    cuadroRst = getCuadroByCod(cuadroJson.get('codCuadro'))
                    cuadroCultivo = CuadroCultivo()
                    saveEntidadSinCommit(cuadroCultivo)
                    cuadroCultivo.cultivo = cultivoObj
                    cuadroCultivo.cuadro = cuadroRst
                    grupoCuadro.cuadroCultivoList.append(cuadroCultivo)
        
        #Agregar los save correspodientes
        
        fincaRst.planificacionList.append(planificacionInicial) 
        saveEntidadSinCommit(fincaRst)
        Commit()
        return ResponseOk()
    except Exception as e:
        Rollback()
        return ResponseException(e)

def getPlanificacionInicial():
    pass

def getPlanificacionesIniciales():
    pass



        