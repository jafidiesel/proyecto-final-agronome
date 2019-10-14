from app.repositorio.hlDb import saveEntidadSinCommit,Commit
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.model.hlmodel import RecomendacionDetalle, RecomDetalleParam, Parametro
from app.repositorio.repositorioRegistrarActividad import selectActivDetalleCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk

def postRegistrarRecom(data):
    try:
        codRecom = data.get('codRecomendacion')
        codActivDetalle = data.get('codActividadDetalle')
        obs = data.get('observacion')
        parametros = data.get('parametros')
        fch = data.get('fchRecomDetalle')
        
        recomendacion = getNomencladoCod('recomendacion',codRecom)
        activDetalle = selectActivDetalleCod(codActivDetalle)
        ##creacion del detalle recomendacion
        detalleRecom = RecomendacionDetalle(observacion = obs,fchRecomDetalle = fch)
        
        ##asociacion de recomendacion
        detalleRecom.recomendacion = recomendacion
        ##asociación de activ detalle 
        activDetalle.recomendacionDetalle = detalleRecom

        for param in parametros:
            codParam = param.get('codParam')
            valor = param.get('valor')
            parametro = getNomencladoCod('parametro',codParam)

            recomDetalleParam = RecomDetalleParam(valor = valor )
            recomDetalleParam.param = parametro
            detalleRecom.paramList.append(recomDetalleParam)

        
        saveEntidadSinCommit(detalleRecom)  
        Commit()
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)