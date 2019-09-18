from app.extensions import db
from app.repositorio.hlDb import Commit
from app.model.hlmodel import ParametroOpcion

def selectAllByParamCod(codParam):
    return ParametroOpcion.query.filter(ParametroOpcion.codParametro == codParam).all