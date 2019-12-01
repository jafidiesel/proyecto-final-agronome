from flask import jsonify,make_response,json
from app.model.hlmodel import Planificacion,Finca,Usuario, GrupoPlanificacion, TipoPlanificacion, EstadoPlanificacion
from app.repositorio.hlDb import saveEntidadSinCommit, selectByCod,Commit, selectAll, Rollback
from app.api.helperApi.hlResponse import ResponseException, ResponseOk,ResponseOkmsg
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca
from app.uses_cases.moduloPlanificacion.iniciarPlanificacion import getPlanificacionInicial

#{codGrupo,codFinca}

#Cabecera
##Agregar  isCancelado
def getCuadros(currentUser,codFinca):
    try:
        #Buscar Finca
        fincaRst = selectFincaCod(codFinca)
        #Buscar Planificaciones asociadas a la finca
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

def getDTO(grupoObjList):
    dtoGeneral = []
    #Etapas
    
    for grupoObj in grupoObjList:
        #Obtener grupo        
        dictGrupo = grupoObj.__getitem__(0).__dict__
        dictGrupo.pop('_sa_instance_state', None) 
        #Obtener planificaciones del grupo
        for planificacionGrupo in grupoObj.__getitem__(1):
            #Obtener datos una planificacion
            dataPlanificacion = planificacionGrupo.__getitem__(0)
            #dictGrupo['planificacion'] = dictElementData
            #Obtener la ultima planificacion en curso del grupo --> Etapa: Inicial, supervisada, Final
            if dataPlanificacion.estadoPlanificacion.nombre == 'inicial':
                ultimoEstadoCod = 0
                ultimoEstadoNombre = dataPlanificacion.estadoPlanificacion.nombre
            elif dataPlanificacion.estadoPlanificacion.nombre == 'supervisada':
                ultimoEstadoCod = 1
                ultimoEstadoNombre = dataPlanificacion.estadoPlanificacion.nombre
            elif dataPlanificacion.estadoPlanificacion.nombre == 'final':
                ultimoEstadoCod = 2
                ultimoEstadoNombre = dataPlanificacion.estadoPlanificacion.nombre
            
            dictPlanificacion = dict(cod = ultimoEstadoCod, nombre = ultimoEstadoNombre)
            dictGrupo['planificacion'] =dictPlanificacion
        dtoGeneral.append(dictGrupo)
    return dtoGeneral
