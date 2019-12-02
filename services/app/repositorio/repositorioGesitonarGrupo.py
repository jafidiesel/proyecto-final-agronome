from app.extensions import db
from app.model.hlmodel import GrupoPlanificacion



def selectGrupoPlanifCod(codGrupo):
    objeto = GrupoPlanificacion.query.filter(GrupoPlanificacion.cod == codGrupo).first()
    return objeto