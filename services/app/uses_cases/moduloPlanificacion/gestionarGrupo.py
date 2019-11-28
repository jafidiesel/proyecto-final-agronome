from flask import jsonify,make_response,json
from app.model.hlmodel import Planificacion,Finca,Usuario, GrupoPlanificacion, TipoPlanificacion, EstadoPlanificacion
from app.repositorio.hlDb import saveEntidadSinCommit, selectByCod,Commit, selectAll, Rollback
from app.api.helperApi.hlResponse import ResponseException, ResponseOk,ResponseOkmsg
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca
from app.uses_cases.moduloPlanificacion.iniciarPlanificacion import getPlanificacionInicial

#{codGrupo,codFinca}
def getPlanificaciones(data,currentUser):
    #Filtrar por Finca
    fincaRst = selectFincaCod(data.get('codFinca'))
    planificacionLista = fincaRst.planificacionList

    #Buscar grupo
    grupoPlanificacionRst = selectByCod(GrupoPlanificacion, data.get('codGrupo'))
    planificacionesRst = grupoPlanificacionRst.planificacion
    #Verificar que el grupo es de la finca pasada como parametro
    
    #Por cada planificacion leer codigo y tipo
    for planificacionElemento in planificacionesRst:
        if planificacionElemento.tipoPlanificacion == 'inicial':
            getPlanificacionInicial(planificacionElemento.cod)
        elif planificacionElemento.tipoPlanificacion == 'supervisada':
            pass
        elif planificacionElemento.tipoPlanificacion == 'final':
            pass

#Cabecera
##Agregar  isCancelado
def getAll(currentUser,codFinca):
    try:
        #Buscar Finca
        fincaRst = selectFincaCod(codFinca)
        #Buscar Planificaciones asociadas a la finca
        #planificacionLista = fincaRst.planificacionList
        grupoPlanificacionRstList = fincaRst.grupoPlanificacionList

        if not grupoPlanificacionRstList:
            message = json.dumps({'message': 'La finca no posee planificaciones'})   
            return make_response(jsonify(message),400)
        elif grupoPlanificacionRstList:            
            #Armado Dto 
            dtoGeneral = []
            for grupoRst in grupoPlanificacionRstList:
                planificacionLista = grupoRst.planificaciones
                dtoGrupo = []
                dtoGrupo.append(grupoRst)
                dtoPlanificacionesList = []
                for planificacionRst in planificacionLista:                        
                    dtoPlanificacion = []                 
                    dtoDatosPlanificacion = []
                    tipoPlanificacionRst = planificacionRst.tipoPlanificacion
                    estadoPlanificacionRst = planificacionRst.estadoPlanificacion
                    usuarioPlanificacionRst = planificacionRst.usuario
                    #Armado DTO
                    dtoPlanificacion.append(planificacionRst)
                    dtoDatosPlanificacion.append(tipoPlanificacionRst)
                    dtoDatosPlanificacion.append(estadoPlanificacionRst)        
                    dtoDatosPlanificacion.append(usuarioPlanificacionRst)  
                    dtoPlanificacion.append(dtoDatosPlanificacion)
                    dtoPlanificacionesList.append(dtoPlanificacion)      
                    dtoGrupo.append(dtoPlanificacionesList)  
                    dtoGeneral.append(dtoGrupo)

        return jsonify(getDTO(dtoGeneral))
    except Exception as e:
        return ResponseException(e)

def getDTO(dataRst):
    dtoGeneral = []
    for elementGeneral in dataRst:
        
        dictGrupo = elementGeneral.__getitem__(0).__dict__
        dictGrupo.pop('_sa_instance_state', None)
        planificacion = elementGeneral.__getitem__(1)
        for elementoGrupo in elementGeneral.__getitem__(1):
            dataPlanificacion = elementoGrupo.__getitem__(0)
            dictPlanificacion = dataPlanificacion.__dict__
            dictPlanificacion.pop('_sa_instance_state', None)
            dictElementData = dict(cod = dataPlanificacion.cod, comentarioPlanificacion = dataPlanificacion.comentarioPlanificacion, fchPlanificacion = dataPlanificacion.fchPlanificacion)            
            dictGrupo['planificacion'] = dictElementData
            for elementPlanificacion in elementoGrupo.__getitem__(1):
                
                dictElementP = elementPlanificacion.__dict__
                print('ELEMENTOS')
                dictElementP.pop('_sa_instance_state', None)

                if 'rol' in dictElementP:
                    dictElementP.pop('rol', None)
                if elementPlanificacion.nombre == 'inicial' or elementPlanificacion.nombre == 'supervisada' or elementPlanificacion.nombre == 'final':
                    dictElementData['tipoPlanificacion'] = dictElementP                    
                if elementPlanificacion.nombre == 'en curso' or elementPlanificacion.nombre == 'finalizada':
                    dictElementData['estadoPlanificacion']= dictElementP
                if 'usuario'in dictElementP:
                    dictUsuario = dict(nombre = elementPlanificacion.nombre, apellido = elementPlanificacion.apellido, usuario = elementPlanificacion.usuario)
                    dictElementData['usuario'] = dictUsuario
                 
        dtoGeneral.append(dictGrupo)
    return dtoGeneral
