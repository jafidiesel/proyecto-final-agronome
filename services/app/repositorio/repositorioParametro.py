from app.extensions import db
from app.repositorio.hlDb import Commit
from app.model.hlmodel import ParametroOpcion

def selectAllByParamCod(codParam):
    objectList = ParametroOpcion.query.filter(ParametroOpcion.codParametro == codParam).all()
    print(objectList)
    return objectList