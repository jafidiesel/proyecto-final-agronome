from app.model.hlmodel import Planificacion, GrupoPlanificacion , Cultivo, GrupoCuadro, CuadroCultivo, LibroCampo
from app.repositorio.hlDb import saveEntidadSinCommit, Commit, Rollback
from app.repositorio.repositorioPlanificacion import getPlanifByCod, getParcelaByCod, getCuadroByCod, selectLibroName, selectGrupoName
from app.repositorio.repositorioGestionarFinca import selectFincaCod
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
from app.api.helperApi.hlResponse import ResponseException, ResponseOk, ResponseOkmsg
from app.uses_cases.libroCampo.libroCampo import createLibroCampo
from app.uses_cases.moduloGestionFinca.gestionarFinca import getUsersByFincaFilter
import datetime
from flask import jsonify,make_response
import string 
import random 

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
        estadoCancelar = getNomencladoCod('estadoPlanificacion',3)
        #tipos planifi
        tipoInicial = getNomencladoCod('tipoPlanificacion',1)
        tipoSupervisada = getNomencladoCod('tipoPlanificacion',2)
        tipoFinal = getNomencladoCod('tipoPlanificacion',3)

        #acciones
        iniciar = 'i'
        supervisar = 's'
        finalizar = 'f'

        #email
        body = ''

        #check de acciones 
        if not (action == iniciar or action == supervisar or action == finalizar):
            raise Exception('N','el action ingresado no es correcto, las action disponibles son: {}, {}, {}.'.format(iniciar,supervisar,finalizar))

        finca = selectFincaCod(codFinca) #se busca la finca para asociarla al grupo planificacion y para crear libro campo
        if not finca:
            raise Exception('N','No existe finca con codFinca ' + str(codFinca))

        #acciones 
        if action == iniciar:
            tipoCultivo = getNomencladoCod('tipoCultivo',datosCultivosJsonList.__getitem__(0).get('codTipoCultivo'))            
            #Comprobar que el nombre no existe
            #buscar todos los Grupos planificacion
            while True:
                nombreGrupPlanif = str(tipoCultivo.nombre) + ' ' + (str(datosCultivosJsonList.__getitem__(0).get('variedadCultivo'))) + ' ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k = 4)) 
                if not selectGrupoName(GrupoPlanificacion, nombreGrupPlanif):
                    break       
                print('Nombre repetido')

            #Creo grupo planificación 
            grupPlanif = createGrupoPlanificacion(nombreGrupPlanif)
            finca.grupoPlanificacionList.append(grupPlanif)
            tipoPlanificacion = tipoInicial

            enviaCorreo = True
            userEmail = getUsersByFincaFilter(finca,'ingeniero')
            body = 'Se ha generado una nueva planificación inicial \nPara visualizarla y supervisarla utilice el siguiente enlace:\n http://localhost:4200/planificacion/listarGrupos'
            
        else: #supervisar o finalizar
            #cambio de estado la planificación anterior de "encurso" debe pasar a finalizada
            planifBefore = getPlanifByCod(codPlanifBefore)
            if not planifBefore:
                raise Exception('N','No existe planificación anterior con cod ' + str(codPlanifBefore))

    
            tipoPlanifBefore =  planifBefore.tipoPlanificacion   
            if action == supervisar:
                hlCheckTipoPlanifBefore(tipoPlanifBefore,tipoInicial,tipoSupervisada,codPlanifBefore)
                tipoPlanificacion = tipoSupervisada
                enviaCorreo = True
                userEmail = getUsersByFincaFilter(finca,'encargadofinca')
                body = 'Se ha supervisado una planificación inicial \nPara visualizarla y finalizarla utilice el siguiente enlace:\n http://localhost:4200/planificacion/listarGrupos'

            else: #finalizar
                hlCheckTipoPlanifBefore(tipoPlanifBefore,tipoSupervisada,tipoFinal,codPlanifBefore)
                tipoPlanificacion = tipoFinal
                enviaCorreo = False

            planifBefore = updateEstadoPlanificacion(planifBefore,estadoFinalizado)

            grupPlanif = planifBefore.grupoPlanif #recupero grupo de la planf before
            
            

        ##comun
        planifNew = crearPlanificacion(comentarioJson,tipoPlanificacion,estadoEncurso,currentUser,grupPlanif)
        cultivoListRst = []
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
            cultivoListRst.append(cultivoObj)         
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
        print(grupPlanif)

        #Creacion libro de campo
        if (planifNew.tipoPlanificacion == tipoFinal):
            #finca = selectFincaCod(codFinca)
            print('esto en crear libro campo')
            for cultivo in cultivoListRst:       
                while True:        
                    nombreLibro = str(cultivo.tipoCultivoR.nombre) + ' ' + (str(cultivo.variedadCultivo)) + ' ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k = 4)) 
                    if not selectLibroName(LibroCampo, nombreLibro):
                        break
                print(nombreLibro)
                createLibroCampo(nombreLibro,finca,grupPlanif,cultivo)




        Commit()

        
        if enviaCorreo:
            userEmail = getUsersByFincaFilter(finca,'ingeniero')
            hlSendEmailPlanif(userEmail,body)          
        
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

def getPlanificaciones(data,currentUser):
    #Filtrar por Finca
    try:
        fincaRst = selectFincaCod(data.get('codFinca'))
        if not fincaRst:
            raise Exception('N','No existe la FInca consultada')
    except Exception as e:
        return ResponseException(e)
    grupoRstList = fincaRst.grupoPlanificacionList
    print(grupoRstList)
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
                
                    cultivoDto = []
                    for cultivo in cultivoCuadroList:
                        
                        cultivoDto.append(cultivo)
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
                                if (cuadroCultivoRst.cultivo == cultivo):
                                    cuadrosList.append(cuadroCultivoRst.cuadro)
                            parcelaDatos.append(cuadrosList)
                            grupoCuadroDto.append(parcelaDatos)
                            gruposList.append(grupoCuadroDto)
                        
                        cultivoDto.append(gruposList)
                    planificacionDto.append(cultivoDto)
                    planificacionesDtoList.append(planificacionDto)
                return planificacionesDtoList
                
                          
def toDict(planificacionesDtoList):
    print(planificacionesDtoList)
    planificacionesDto = {}
    for planificacionData in planificacionesDtoList:
        planificacionRst = planificacionData.__getitem__(0)
        cultivoDto = []
        cultivoRst = planificacionData.__getitem__(1).__getitem__(0)
        grupoList =[]
        for grupoData in planificacionData.__getitem__(1).__getitem__(1):         
            grupoRst = grupoData.__getitem__(0)                    
            parcelaData = grupoData.__getitem__(1)
            parcelaDto = []
            parcelaRst = parcelaData.__getitem__(0)
            cuadrosDto = []
            for cuadroData in parcelaData.__getitem__(1):
                cuadro = dict(codCuadro = cuadroData.codCuadro,nombreCuadro = cuadroData.nombreCuadro)
                cuadrosDto.append(cuadro)
            parcela = dict(codParcela = parcelaRst.codParcela, nombreParcela = parcelaRst.nombrePacela, superficieParcela = parcelaRst.superficieParcela)
            parcela['cuadros'] = cuadrosDto
            parcelaDto.append(parcela)
            grupoCuadro = dict(cod =grupoRst.cod)
            grupoCuadro['parcelas'] = parcelaDto
            grupoList.append(grupoCuadro)
            
        tipoCultivoRst = cultivoRst.tipoCultivoR
        cultivo = dict(cod =cultivoRst.cod,cantidadCultivo = cultivoRst.cantidadCultivo, produccionEsperada= cultivoRst.produccionEsperada, variedadCultivo = cultivoRst.variedadCultivo, cicloUnico = cultivoRst.cicloUnico)
        cultivo['tipoCultivo'] = dict(cod = tipoCultivoRst.cod,nombre = tipoCultivoRst.nombre)
        cultivo['grupos'] = grupoList
        cultivoDto.append(cultivo)
        
        fchP = planificacionRst.fchPlanificacion.strftime("%d-%m-%Y %H:%M:%S")
        
        
        tipoPlanificacionRst = planificacionRst.tipoPlanificacion
        estadoPlanificacionRst = planificacionRst.estadoPlanificacion
        planificacion = dict(cod = planificacionRst.cod, fchPlanificacion= fchP, comentarioPlanificacion= planificacionRst.comentarioPlanificacion)
        tipoPlanificacionData = dict(cod = tipoPlanificacionRst.cod, nombre = tipoPlanificacionRst.nombre, isActiv = tipoPlanificacionRst.isActiv)
        estadoPlanificacionData = dict(cod = estadoPlanificacionRst.cod, nombre = estadoPlanificacionRst.nombre, isActiv = estadoPlanificacionRst.isActiv)
        
        
        planificacion['estadoPlanificacion'] = estadoPlanificacionData
        planificacion['tipoPlanificacion'] = tipoPlanificacionData
        planificacion['cultivo'] = cultivoDto 

        print('TIPO PLANIFICACION')
        print(tipoPlanificacionRst.nombre)
        print(tipoPlanificacionRst.cod)
        if tipoPlanificacionRst.cod == 1:
            planificacionesDto['inicial'] = planificacion
        elif tipoPlanificacionRst.cod == 2:
            planificacionesDto['supervisada'] = planificacion
        elif tipoPlanificacionRst.cod == 3:
            planificacionesDto['final'] = planificacion 
        """planificacionesDto['inicial'] = planificacion """
    return planificacionesDto


def hlCancelPlanif(planificacion):
    estadoCancelar = getNomencladoCod('estadoPlanificacion',3)
    updateEstadoPlanificacion(planificacion,estadoCancelar)
    return



def hlSendEmailPlanif(usuario,body):
    from app.shared.hlSendEmail import sendEmail
    key = 'planificacion'
    html = ''
    additionals = []
    userList = []
    userList.append(usuario)
    sendEmail(key,userList,body,html,additionals)