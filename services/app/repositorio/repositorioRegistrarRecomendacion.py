from app.extensions import db
from app.model.hlmodel import ActividadDetalle, Actividad , RecomendacionDetalle


def selectRecomCod(codRecomDetalle): 
    objeto = RecomendacionDetalle.query.filter(RecomendacionDetalle.codRecomDetalle==codRecomDetalle).first()
    return objeto


def selectRecomenActiv(): ## tiene que venir el libro de campo
    codFitosanitaria = 5
    codCatastrofe = 3
    actividadFitosanitaria = Actividad.query.filter(Actividad.cod==codFitosanitaria).first()
    actividadCatastrofe = Actividad.query.filter(Actividad.cod==codCatastrofe).first()
    
    objetos = ActividadDetalle.query.filter(ActividadDetalle.isEliminado==False).filter(ActividadDetalle.actividad == actividadFitosanitaria or ActividadDetalle.actividad == actividadFitosanitaria==actividadCatastrofe).all()
    
    return  objetos     


