from app.repositorio.hlDb import Rollback,saveEntidadSinCommit,selectActiveByName,saveEntidad, selectAll, selectByCod, updateEntidad, selectByisActiv,Commit
from app.model.hlmodel import Cultivo,TipoCultivo,TipoPlanificacion,Planificacion,GrupoPlanificacion,Finca, Parcela, Cuadro, EstadoPlanificacion, GrupoCuadro, CuadroCultivo, Cuadro
from app.uses_cases.moduloPlanificacion.shared.sharedFunctions import tipoCultivoListToDict
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca
from app.repositorio.repositorioPlanificacion import getCuadroByCod, getParcelaByCod
from flask import jsonify,make_response
from app.api.helperApi.hlResponse import ResponseException, ResponseOk


def getParcelasLibres(data):    
    #Extraer Finca de Json
    codFincaJson = data
    #Buscar Finca
    fincaRst = selectFincaCod(codFincaJson)
    if not fincaRst: 
            raise Exception('N','No existe finca con código ' + str(codFincaJson))
    #Buscar Parcelas asociadas
    parcelasRstList = fincaRst.parcelaList
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
        print('DTO')
        return dtoGeneral
    else:
        dtoGeneralPlan = []
        dtoCuadroTmp = []
        parcelasList = [] #Para agrupar las parcelas iguales que estan presentes en varias planificaciones
        for planificacionRst in planificacionListRst:
            dtoPlanificacion = []            
            if (planificacionRst.estadoPlanificacion.nombre == "en curso" ):
                for grupoCuadro in planificacionRst.grupoCuadroList:
                    parcelaGrupo = grupoCuadro.parcela
                    #Verficar si la parcela ya existe en la lista
                    if not parcelaGrupo in parcelasList:
                        parcelasList.append(parcelaGrupo)
                        #Armar dto con encabezado parcela y cuerpo cuadro
                        for cuadroCultivo in grupoCuadro.cuadroCultivoList:
                            cuadroGrupo = cuadroCultivo.cuadro
                            dtoCuadroTmp.append(cuadroGrupo)                        
                        parcelasList.append(dtoCuadroTmp)
                        dtoPlanificacion.append(parcelasList)
                    else:
                        #Agregar los cuadros a la parcela correspondiente
                        pass

            dtoGeneralPlan.append(dtoPlanificacion)
        
        #Comparacion de listas para extraer los items que no se repiten
        dtoGeneralLibre = []
        print('DTO GENERAL')
        print(dtoGeneral)
        print('DTO GENERAL 2')
        print(dtoGeneralPlan)
        for datosDtoGeneral in dtoGeneral:
            parcelaDto = datosDtoGeneral.__getitem__(0)
            for datosDtoGeneralPlan in dtoGeneralPlan:
                dtoParcelaLibre = []
                for datosParcela in datosDtoGeneralPlan:
                    parcelaOcupada = datosParcela.__getitem__(0)
                    #Se extraen los cuadros no repetidos
                    if (parcelaDto.codParcela == parcelaOcupada.codParcela):
                        cuadros1 = datosDtoGeneral.__getitem__(1)
                        cuadros2 = datosParcela.__getitem__(1)                        
                        cuadrosNoRepetidos =set(cuadros1) - set(cuadros2)
                        if cuadrosNoRepetidos:
                            dtoParcelaLibre.append(parcelaDto)
                            print(dtoParcelaLibre)
                            dtoParcelaLibre.append(list(cuadrosNoRepetidos))
                            print(dtoParcelaLibre)
                    else:
                        dtoParcelaLibre.append(datosDtoGeneral)
            
                dtoGeneralLibre.append(dtoParcelaLibre)
        print('DTO COMPARATIVO')
        print(dtoGeneralLibre)
        return dtoGeneralLibre      
        
def iniciarPlanificacion(data):
    parcelaLibreList = getParcelasLibres(data)
    dtoParcelasLibres = []
    if not parcelaLibreList:
        return make_response(jsonify({'message:':'No existen cuadros libres'}),202)
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


        