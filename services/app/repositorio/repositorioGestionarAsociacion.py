from app.extensions import db
from app.model.hlmodel import ActividadParametro, RecomendacionParametro, TipoAnalisisParam, TipoPlanParam, Parametro



modelos = { 
    "actividadParametro":ActividadParametro,
    "recomendacionParametro":RecomendacionParametro,
    "tipoAnalisisParam":TipoAnalisisParam,
    "tipoPlanParam": TipoPlanParam
    }

def cantAsociaciones(entidad,entidadInterm):
    if entidadInterm=='actividadParametro':
        cantidad = ActividadParametro.query.filter(ActividadParametro.actividad==entidad).filter(ActividadParametro.isActiv==True).count()
    else:
        if entidad == 'recomendacionParametro': 
            cantidad = RecomendacionParametro.query.filter(RecomendacionParametro.recomendacion==entidad).filter(ActividadParametro.isActiv==True).count()
        else:
            if entidad == 'tipoAnalisisParam':
                cantidad = TipoAnalisisParam.query.filter(TipoAnalisisParam.tipoAnalisis==entidad).filter(ActividadParametro.isActiv==True).count() 
            else:
                if entidad == 'tipoAnalisisParam':
                    cantidad = TipoPlanParam.query.filter(TipoPlanParam.tipoPlan==entidad).filter(ActividadParametro.isActiv==True).count()  
    return cantidad