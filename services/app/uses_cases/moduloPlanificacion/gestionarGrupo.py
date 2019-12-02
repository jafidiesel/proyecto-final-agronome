from flask import jsonify,make_response,json
from app.model.hlmodel import Planificacion,Finca,Usuario, GrupoPlanificacion, TipoPlanificacion, EstadoPlanificacion
from app.repositorio.hlDb import saveEntidadSinCommit, selectByCod,Commit, selectAll, Rollback
from app.api.helperApi.hlResponse import ResponseException, ResponseOk,ResponseOkmsg
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca
from app.repositorio.repositorioGesitonarGrupo import selectGrupoPlanifCod
from app.uses_cases.moduloPlanificacion.gestionarPlanificacion import hlCancelPlanif

#Cabecera
##Agregar  isCancelado
def getGrupos(currentUser,codFinca):
    try:
        #Buscar Finca
        fincaRst = selectFincaCod(codFinca)
        #Buscar Planificaciones asociadas a la finca
        grupoPlanificacionRstList = fincaRst.grupoPlanificacionList

        if not grupoPlanificacionRstList:
            raise Exception('N','La finca no posee planificaciones')
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
    try:
        dtoGeneral = []
        #Etapas
        
        for grupoObj in grupoObjList:
            ultimoTipoCod = 0
            ultimoEstadoNombre = ""
            #Obtener grupo        
            dictGrupo = grupoObj.__getitem__(0).__dict__
            dictGrupo.pop('_sa_instance_state', None) 
            #Obtener planificaciones del grupo
            for planificacionGrupo in grupoObj.__getitem__(1):
                #Obtener datos una planificacion
                dataPlanificacion = planificacionGrupo.__getitem__(0)
                #Obtener la ultima planificacion en curso del grupo --> Etapa: Inicial, supervisada, Final
                if dataPlanificacion.tipoPlanificacion.cod > ultimoTipoCod:
                    ultimoTipoCod = dataPlanificacion.tipoPlanificacion.cod
                    ultimoEstadoNombre = dataPlanificacion.estadoPlanificacion.nombre                            
            dictPlanificacion = dict(cod = ultimoTipoCod, nombre = ultimoEstadoNombre)
            dictGrupo.pop('planificaciones', None)
            dictGrupo['planificacion'] = dictPlanificacion
            dtoGeneral.append(dictGrupo)
        return dtoGeneral
    except Exception as e:
        return ResponseException(e)

def deleteGrupo(codGrupoPlanif):
    try:
        grupoPlanif = selectGrupoPlanifCod(codGrupoPlanif)
        if grupoPlanif == None:
            raise Exception('N','No existe grupo planificacion con cod ' + str(codGrupoPlanif))

        if not grupoPlanif.isActiv:
            raise Exception('N','El grupo planificación ya se encuentra cancelado')

        planifList = grupoPlanif.planificaciones
        for planif in planifList:
            hlCancelPlanif(planif)

        grupoPlanif.isActiv=False
        saveEntidadSinCommit(grupoPlanif)
        Commit()
        return ResponseOkmsg('Grupo planificación cancelado exitosamente')
    except Exception as e:
        return ResponseException(e)