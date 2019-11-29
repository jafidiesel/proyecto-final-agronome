from app.extensions import db
from app.model.hlmodel import Cuadro, Parcela, Planificacion



def getPlanifByCod(cod):
    planificacion = Planificacion.query.filter(Planificacion.cod == cod).first()
    return planificacion

def getCuadroByCod(cod):
    cuadro = Cuadro.query.filter(Cuadro.codCuadro == cod).one()
    return cuadro

def getParcelaByCod(cod):
    parcela = Parcela.query.filter(Parcela.codParcela == cod).one()
    return parcela