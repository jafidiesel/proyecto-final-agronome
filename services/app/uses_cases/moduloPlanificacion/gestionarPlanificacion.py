from app.model.hlmodel import Planificacion, GrupoPlanificacion , Cultivo, GrupoCuadro, CuadroCultivo
from app.repositorio.hlDb import saveEntidadSinCommit, Commit
from app.repositorio.repositorioPlanificacion import getPlanifByCod, getParcelaByCod, getCuadroByCod
from app.repositorio.repositorioGestionarFinca import selectFincaCod
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
from app.api.helperApi.hlResponse import ResponseException, ResponseOk, ResponseOkmsg
import datetime

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