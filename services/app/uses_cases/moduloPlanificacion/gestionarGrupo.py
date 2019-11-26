from flask import jsonify,make_response
from app.model.hlmodel import Planificacion,Finca,Usuario, GrupoPlanificacion, TipoPlanificacion, EstadoPlanificacion
from app.repositorio.hlDb import saveEntidadSinCommit, selectByCod,Commit, selectAll, Rollback
from app.api.helperApi.hlResponse import ResponseException, ResponseOk,ResponseOkmsg
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca

def getGrupoById():
    pass

def getAll(currentUser,codFinca):
    #Buscar Finca
    fincaRst = selectFincaCod(codFinca)
    #Buscar Planificaciones asociadas a la finca
    planificacionLista = fincaRst.planificacionList
    #Armado Dto 
    dtoGeneral = []
    gruposTmp = []
    for planificacionRst in planificacionLista:
        dtoGrupo = []
        grupoPlanificacionRst = planificacionRst.grupoPlanificacion
        if not gruposTmp or (grupoPlanificacionRst not in gruposTmp) :
            gruposTmp.append(grupoPlanificacionRst)
            dtoGrupo.append(grupoPlanificacionRst)
            dtoPlanificacion = []
            dtoPlanificacion.append(planificacionRst)
            tipoPlanificacionRst = planificacionRst.tipoPlanificacion
            estadoPlanificacionRst = planificacionRst.estadoPlanificacion
            usuarioPlanificacionRst = planificacionRst.usuario
            dtoPlanificacion.append(tipoPlanificacionRst)
            dtoPlanificacion.append(estadoPlanificacionRst)        
            dtoPlanificacion.append(usuarioPlanificacionRst)        
            dtoGrupo.append(dtoPlanificacion)  
            dtoGeneral.append(dtoGrupo)
        else:
            if grupoPlanificacionRst in gruposTmp:
                for arrayGrupo in dtoGeneral:
                    if (grupoPlanificacionRst == arrayGrupo.__getitem__(0)):
                        dtoPlanificacion = []
                        dtoPlanificacion.append(planificacionRst)
                        tipoPlanificacionRst = planificacionRst.tipoPlanificacion
                        estadoPlanificacionRst = planificacionRst.estadoPlanificacion
                        usuarioPlanificacionRst = planificacionRst.usuario
                        dtoPlanificacion = []
                        dtoPlanificacion.append(planificacionRst)
                        tipoPlanificacionRst = planificacionRst.tipoPlanificacion
                        estadoPlanificacionRst = planificacionRst.estadoPlanificacion
                        usuarioPlanificacionRst = planificacionRst.usuario    
                        dtoPlanificacion.append(tipoPlanificacionRst)
                        dtoPlanificacion.append(estadoPlanificacionRst)        
                        dtoPlanificacion.append(usuarioPlanificacionRst)                            
                        arrayGrupo.append(dtoPlanificacion)                    
            
    print(dtoGeneral)
    #Devolver JSON: limpiar dto
    
    return True
