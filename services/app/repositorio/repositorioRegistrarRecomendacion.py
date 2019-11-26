from app.extensions import db
from app.model.hlmodel import ActividadDetalle, Actividad , RecomendacionDetalle
from app.repositorio.repositorioLibroCampo import selectLibroCod

def selectRecomCod(codRecomDetalle): 
    objeto = RecomendacionDetalle.query.filter(RecomendacionDetalle.codRecomDetalle==codRecomDetalle).first()
    return objeto


def selectRecomenActiv(codLibroCampo):
    codFitosanitaria = 8
    codCatastrofe = 7
    libroCampo = selectLibroCod(codLibroCampo) 

    actividadFitosanitaria = Actividad.query.filter(Actividad.cod==codFitosanitaria).first()
    actividadCatastrofe = Actividad.query.filter(Actividad.cod==codCatastrofe).first()

    objetos = ActividadDetalle.query.filter(ActividadDetalle.isEliminado==False).filter(ActividadDetalle.actividad == actividadCatastrofe).filter(ActividadDetalle.libroCampoActivDetalle == libroCampo).order_by(ActividadDetalle.fchActivDetalle).all()

    auxObj = ActividadDetalle.query.filter(ActividadDetalle.isEliminado==False).filter(ActividadDetalle.actividad == actividadFitosanitaria).filter(ActividadDetalle.libroCampoActivDetalle == libroCampo).order_by(ActividadDetalle.fchActivDetalle).all()

    objetos.extend(auxObj) #union de las 2 listas
    return  objetos     


