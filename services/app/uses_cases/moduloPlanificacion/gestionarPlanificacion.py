from app.model.hlmodel import Planificacion, GrupoPlanificacion , Cultivo, GrupoCuadro, CuadroCultivo
from app.repositorio.hlDb import saveEntidadSinCommit, Commit, Rollback
from app.repositorio.repositorioPlanificacion import getPlanifByCod, getParcelaByCod, getCuadroByCod
from app.repositorio.repositorioGestionarFinca import selectFincaCod
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
from app.api.helperApi.hlResponse import ResponseException, ResponseOk, ResponseOkmsg
import datetime
from flask import jsonify,make_response

def postPlanificacion(data,currentUser):
    try:
        data = data
        #Datos Json
        action = data.get('action')
        codPlanifBefore = data.get('codPlanifBefore')
        codFinca = data.get('codFinca')
        comentarioJson = data.get('comentario')
        datosCultivosJsonList = data.get('cultivos')

        #estados planif
        estadoEncurso = getNomencladoCod('estadoPlanificacion',1)
        estadoFinalizado = getNomencladoCod('estadoPlanificacion',2)

        #tipos planifi
        tipoInicial = getNomencladoCod('tipoPlanificacion',1)
        tipoSupervisada = getNomencladoCod('tipoPlanificacion',2)
        tipoFinal = getNomencladoCod('tipoPlanificacion',3)

        #acciones
        iniciar = 'i'
        supervisar = 's'
        finalizar = 'f'
    
        #check de acciones 
        if not (action == iniciar or action == supervisar or action == finalizar):
            raise Exception('N','el action ingresado no es correcto, las action disponibles son: {}, {}, {}.'.format(iniciar,supervisar,finalizar))


        #acciones 
        if action == iniciar:
            #Creo grupo planificación 
            finca = selectFincaCod(codFinca) #se busca la finca para asociarla al grupo planificacion
            if not finca:
                raise Exception('N','No existe finca con codFinca ' + str(codFinca))

            today = datetime.datetime.now.__str__
            nombreGrupPlanif = finca.nombreFinca + str(today)
            grupPlanif = createGrupoPlanificacion(nombreGrupPlanif)
            finca.grupoPlanificacionList.append(grupPlanif)
            tipoPlanificacion = tipoInicial

        else: #supervisar o finalizar
            #cambio de estado la planificación anterior de "encurso" debe pasar a finalizada
            planifBefore = getPlanifByCod(codPlanifBefore)
            if not planifBefore:
                raise Exception('N','No existe planificación anterior con cod ' + str(codPlanifBefore))

                
            tipoPlanifBefore =  planifBefore.tipoPlanificacion   
            if action == supervisar:
                hlCheckTipoPlanifBefore(tipoPlanifBefore,tipoInicial,tipoSupervisada,codPlanifBefore)
                tipoPlanificacion = tipoSupervisada

            else: #finalizar
                hlCheckTipoPlanifBefore(tipoPlanifBefore,tipoSupervisada,tipoFinal,codPlanifBefore)
                tipoPlanificacion = tipoFinal
            planifBefore = updateEstadoPlanificacion(planifBefore,estadoFinalizado)

            grupPlanif = planifBefore.grupoPlanif #recupero grupo de la planf before
       
        ##comun
        planifNew = crearPlanificacion(comentarioJson,tipoPlanificacion,estadoEncurso,currentUser,grupPlanif)

        for cultivo in datosCultivosJsonList:
            ##Creacion del cultivo
            tipoCultivo = getNomencladoCod('tipoCultivo',cultivo.get('codTipoCultivo'))
            cultivoObj = Cultivo(
                cantidadCultivo     = cultivo.get("cantidadCultivo"), 
                produccionEsperada  = cultivo.get("produccionEsperada"),
                variedadCultivo     = cultivo.get("variedadCultivo"),
                cicloUnico          = cultivo.get("cicloUnico")
                )
            cultivoObj.tipoCultivoR = tipoCultivo

            saveEntidadSinCommit(cultivoObj) #no se si hace falta

            #creacion de grupo cuadro
            for parcelaJson in cultivo.get("parcelas"):
                parcelaRst = getParcelaByCod(parcelaJson.get('codParcela'))
                grupoCuadro = GrupoCuadro()
                #saveEntidadSinCommit(grupoCuadro)
                grupoCuadro.parcela = parcelaRst
                planifNew.grupoCuadroList.append(grupoCuadro)

                #creacion de cuadro cultivo y sus asociaciones 
                for cuadroJson in parcelaJson.get('cuadros'):
                    cuadroRst = getCuadroByCod(cuadroJson.get('codCuadro'))
                    cuadroCultivo = CuadroCultivo()
                    #saveEntidadSinCommit(cuadroCultivo)
                    cuadroCultivo.cultivo = cultivoObj
                    cuadroCultivo.cuadro = cuadroRst
                    grupoCuadro.cuadroCultivoList.append(cuadroCultivo)

                saveEntidadSinCommit(grupoCuadro)

        Commit()
        return ResponseOkmsg('Planificación ' + tipoPlanificacion.nombre + ' creada exitosamente')
    except Exception as e:
        Rollback()
        return ResponseException(e)



def crearPlanificacion(comentarioPlanificacion,tipoPlanificacion, estadoPlanificacion, usuario, grupoPlanificacion):
    planificacion = Planificacion(comentarioPlanificacion=comentarioPlanificacion)
    #asociacion de planificacion con las entidades que se relaciona 
    planificacion.tipoPlanificacion = tipoPlanificacion
    planificacion.estadoPlanificacion = estadoPlanificacion
    planificacion.usuario = usuario

    #se agrega la planificacion al grupoPlanif
    planificacion.grupoPlanif = grupoPlanificacion
    
    saveEntidadSinCommit(planificacion)
    return planificacion


def createGrupoPlanificacion(nombreGrupPlanif):
    print('voy a crear el grupo planificación')
    grupPlanif = GrupoPlanificacion(nombreGrupoPlanificacion=nombreGrupPlanif, isActiv=True)
    saveEntidadSinCommit(grupPlanif)
    print('creado')
    return grupPlanif

def updateEstadoPlanificacion(planificacion,estadoPlanificacion):
    ##control de estado (en caso que YA este al estado que se queire update )
    if not planificacion.estadoPlanificacion == estadoPlanificacion:
        planificacion.estadoPlanificacion = estadoPlanificacion
        saveEntidadSinCommit(planificacion)
        return planificacion
    else:    
        raise Exception('N','La planificacion ' + str(planificacion.cod) + ' ya se encuenta en estado ' + estadoPlanificacion.nombre)
    

def hlCheckTipoPlanifBefore(tipoActual, tipoActualEsperado, tipoNuevo, codPlanifBefore):
    #ejemplo tipo actual: inicial, tipoActualEsperado: inicial, tipoNuevo: supervisada OK
    #ejemplo tipo actual: supervisada, tipoActualEsperado: supervisada, tipoNuevo: final NOT OK
    if not tipoActual == tipoActualEsperado: 
        raise Exception('N','La planficación anterior con codPlanifBefore {},no es de tipo {}, su tipo es {}, no se puede cambiar al tipo {}.'.format(codPlanifBefore, tipoActualEsperado.nombre,tipoActual.nombre,tipoNuevo.nombre))
    return

def getPlanificaciones(data,currentUser):
    #Filtrar por Finca
    try:
        fincaRst = selectFincaCod(data.get('codFinca'))
    except Exception:
        return make_response(jsonify({'message': 'No existe la FInca consultada'}),400)

    grupoRstList = fincaRst.grupoPlanificacionList
    if not grupoRstList:
        pass
    elif grupoRstList:
        #Buscar el grupo pasado como parametro
        for grupoRst in grupoRstList:
            if (grupoRst.cod == data.get('codGrupo')):
                planificacionesRst = grupoRst.planificaciones
                #Armar dto de planificaciones
                planificacionesDtoList = []
                for planificacionRst in planificacionesRst:
                    cultivoCuadroList = []
                    planificacionDto = []
                    planificacionDto.append(planificacionRst)
                    #Leer Cuadros de la planificacion
                    grupoCuadroRstList = planificacionRst.grupoCuadroList

                    for grupoCuadroRst in grupoCuadroRstList:
                        cuadroCultivoRstList = grupoCuadroRst.cuadroCultivoList
                        for cuadroCultivoRst in cuadroCultivoRstList:
                            if cuadroCultivoRst.cultivo not in cultivoCuadroList:
                                cultivoCuadroList.append(cuadroCultivoRst.cultivo)
                    
                    for cultivoCuadro in cuadroCultivoRstList:
                        cultivoDto = []
                        cultivoDto.append(cultivoCuadro)
                        gruposList = []
                        for grupoCuadroRst in grupoCuadroRstList:
                            grupoCuadroDto = []
                            parcelaDatos = []
                            #Leer parcela
                            parcelaRst = grupoCuadroRst.parcela
                            parcelaDatos.append(parcelaRst)
                            #Armado Dto
                            grupoCuadroDto.append(grupoCuadroRst)
                            cuadroCultivoRstList = grupoCuadroRst.cuadroCultivoList
                            cuadrosList = []
                            for cuadroCultivoRst in cuadroCultivoRstList:                                                                
                                if (cuadroCultivoRst.cultivo == cultivoCuadro):
                                    cuadrosList.append(cuadroCultivoRst.cuadro)
                            parcelaDatos.append(cuadrosList)
                            grupoCuadroDto.append(parcelaDatos)
                            gruposList.append(grupoCuadroDto)
                        
                        cultivoDto.append(gruposList)
                    planificacionDto.append(cultivoDto)
                planificacionesDtoList.append(planificacionDto)
                print(planificacionesDtoList)
                return planificacionesDtoList
                
                          
def toDict(planificacionesDtoList):
    planificacionesDto = []
    for planificacionData in planificacionesDtoList:
        planificacionDto = []
        planificacionRst = planificacionData.__getitem__(0)
        for cultivoData in planificacionData.__getitem__(1):
            cultivoDto = []
            cultivoRst = cultivoData.__getitem__(0)
            grupoList = []
            for grupoData in cultivoData.__getitem__(1):
                grupoRst = grupoData.__getitem__(0)                    
                parcelaData = grupoData.__getitem__(1)
                parcelaDto = []
                parcelaRst = parcelaData.__getitem__(0)
                cuadrosDto = []
                for cuadroData in parcelaData.__getitem__(1):
                    cuadro = cuadroData.__dict__
                    cuadro.pop('_sa_instance_state', None)
                    cuadro.pop('codParcela', None)
                parcela = parcelaRst.__dict__
                parcela.pop('_sa_instance_state', None)
                parcela.pop('codFinca',None)
                parcela.pop('superficie',None)
                parcela.pop('columnas',None)
                parcela.pop('filas',None)
                parcela['cuadros'] = cuadrosDto
                parcelaDto.append(parcela)

                grupo = grupoRst.__dict__
                grupo.pop('_sa_instance_state', None)
                grupo.pop('codFinca', None)

                grupo['parcela'] = parcelaDto
                grupoList.append(grupo)
            tipoCultivoRst = cultivoRst.tipoCultivo
            tipoCultivo = tipoCultivoRst.__dict__
            cultivo = cultivoRst.__dict__
            tipoCultivo.pop('_sa_instance_state', None)
            tipoCultivo.pop('nombreNomenclador', None)
            cultivo.pop('_sa_instance_state', None)
            cultivo.pop('tipoCultivo', None)

                                
                            