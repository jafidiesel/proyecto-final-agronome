from app.repositorio.hlDb import selectActiveByName,saveEntidad, selectAll, selectByCod, updateEntidad, selectByisActiv,Commit
from app.model.hlmodel import Cultivo,TipoCultivo,TipoPlanificacion,Planificacion,GrupoPlanificacion,Finca, Parcela, Cuadro, EstadoPlanificacion, GrupoCuadro, CuadroCultivo, Cuadro
from app.uses_cases.moduloPlanificacion.shared.sharedFunctions import tipoCultivoListToDict
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca
from app.repositorio.repositorioPlanificacion import getCuadroByCod, getParcelaByCod
from flask import jsonify

#{'codFinca': cod }
#
#
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
    for parcelasRst in parcelasRstList:
        dtoParcela = []
        dtoParcela.append(parcelasRst)
        dtoParcela.append(parcelasRst.cuadroList)
        dtoGeneral.append(dtoParcela)  
    
    #Leer instancias Planificación asociadas a Finca instanciada.
    dtoParcPlan = []
    dtoGeneralPlan = []
    dtoCuadroPlan = []
    planificacionListRst = fincaRst.planificacionList
    if not planificacionListRst:
        return dtoGeneral
    else:
        for planificacionRst in planificacionListRst:
            if (planificacionRst.estadoPlanificacion.nombre == "en curso" ):
                for grupoCuadro in planificacionRst.grupoCuadroList:
                    parcelaGrupo = grupoCuadro.parcela
                    #Armar dto con encabezado parcela y cuerpo cuadro
                    for cuadroCultivo in grupoCuadro.cuadroCultivoList:
                        cuadroGrupo = cuadroCultivo.cuadro
                        dtoCuadroPlan.append(cuadroGrupo)
                    
                    dtoParcela.append(parcelaGrupo)
                    dtoParcela.append(dtoCuadroPlan)

        
def iniciarPlanificacion(data):
    parcelaLibreList = getParcelasLibres(data)
    dtoParcelasLibres = []
    for parcelaLibre in parcelaLibreList:        
        dtoCuadrosLibre = []
        for cuadroLibre in parcelaLibre.__getitem__(1):
            #parcelaDto.pop('_sa_instance_state', None) 
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
    #Crear instancia GrupoPlanificacion 
    nombreGrupoJson = data.get("nombreGrupo")
    comentarioJson = data.get("comentario")
    datosCultivosJsonList = data.get("cultivo")
    parcelaListJson = data.get("parcelas")
    grupoPlanificacion = GrupoPlanificacion(nombreGrupoPlanificacion = nombreGrupoJson)
    #Buscar entidades asociadas a la Planificacion
    estadoPlanificacionRst = selectActiveByName(EstadoPlanificacion, data.get("en curso"))
    tipoPlanificacionRst = selectActiveByName(TipoPlanificacion, data.get("inicial"))
    #Crear instancia Planificacion
    planificacionInicial = Planificacion(comentarioPlanificacion = comentarioJson )
    planificacionInicial.tipoPlanificacion = tipoPlanificacionRst
    planificacionInicial.estadoPlanificacion = estadoPlanificacionRst
    #Asociar GrupoPlanificacion con Planificacion
    grupoPlanificacion.planificacion.append(planificacionInicial)
    #Por cada cultivo ingresado
    for datosCultivoJson in datosCultivosJsonList:
        tipoCultivoRst = selectActiveByName(TipoCultivo,datosCultivoJson.get("nombreTipoCultivo"))
        cultivoObj = Cultivo(cantidadCultivo = datosCultivoJson.get("cantidadCultivo"), produccionEsperada = datosCultivoJson.get("produccionEsperada"),variedadCultivo=datosCultivoJson.get("variedadCultivo"),cicloUnico=datosCultivoJson.get("cicloUnico"))
        cultivoObj.tipoCultivo.append(tipoCultivoRst)
        for parcelaJson in parcelaListJson:
            parcelaRst = getParcelaByCod(parcelaJson.get('codParcela'))
            grupoCuadro = GrupoCuadro()
            grupoCuadro.parcela = parcelaRst
            for cuadroJson in parcelaJson.get('cuadros'):
                cuadroRst = getCuadroByCod(cuadroJson.get('codCuadro'))
                cuadroCultivo = CuadroCultivo()
                cuadroCultivo.cultivo = cultivoObj
                cuadroCultivo.cuadro = cuadroRst
                grupoCuadro.cuadroCultivoList.append(cuadroRst)
    
    planificacionInicial.usuario = currentUser
    #Agregar los save correspodientes
    Commit()

        