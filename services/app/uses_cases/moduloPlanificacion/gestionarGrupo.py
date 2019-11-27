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
        dtoPlanificacion = []
        dtoPlanificacionesList = []

        grupoPlanificacionRst = planificacionRst.grupoPlanificacion
        if not gruposTmp or (grupoPlanificacionRst not in gruposTmp) :
            gruposTmp.append(grupoPlanificacionRst)
            dtoGrupo.append(grupoPlanificacionRst)
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
        else:
            if grupoPlanificacionRst in gruposTmp:
                for arrayGrupo in dtoGeneral:
                    if (grupoPlanificacionRst == arrayGrupo.__getitem__(0)):
                        dtoPlanificacion.append(planificacionRst)
                        tipoPlanificacionRst = planificacionRst.tipoPlanificacion
                        estadoPlanificacionRst = planificacionRst.estadoPlanificacion
                        usuarioPlanificacionRst = planificacionRst.usuario
                        dtoPlanificacion = []
                        dtoDatosPlanificacion = []
                        dtoPlanificacion.append(planificacionRst)
                        tipoPlanificacionRst = planificacionRst.tipoPlanificacion
                        estadoPlanificacionRst = planificacionRst.estadoPlanificacion
                        usuarioPlanificacionRst = planificacionRst.usuario    
                        dtoDatosPlanificacion.append(tipoPlanificacionRst)
                        dtoDatosPlanificacion.append(estadoPlanificacionRst)        
                        dtoDatosPlanificacion.append(usuarioPlanificacionRst)  
                        dtoPlanificacion.append(dtoDatosPlanificacion)
                        arrayGrupo.append(dtoPlanificacion)                    
            
    
    return jsonify(getDTO(dtoGeneral))

def getDTO(dataRst):
    dtoGeneral = []
    for elementGeneral in dataRst:
        dtoGrupo = []
        dictGrupo = elementGeneral.__getitem__(0).__dict__
        dictGrupo.pop('_sa_instance_state', None)

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
                    dictElementData['usuario'] = dictElementP
                    
                 
                print(dictElementData)
                

            #dictPlanificacion = dict(cod = dataPlanificacion.cod, comentarioPlanificacion = dataPlanificacion.comentarioPlanificacion, fchPlanificacion = dataPlanificacion.fchPlanificacion)            
            
        #dictGrupo = dataGrupo.__dict__
        
        dtoGeneral.append(dictGrupo)
    return dtoGeneral
