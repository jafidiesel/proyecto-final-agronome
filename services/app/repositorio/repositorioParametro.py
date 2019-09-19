from app.extensions import db
from app.repositorio.hlDb import Commit
from app.model.hlmodel import ParametroOpcion


def selectAllByParamCod(codParam):
    objectList = ParametroOpcion.query.filter(ParametroOpcion.codParametro == codParam).all()
    return objectList

def selectActiveByName(entidad,valor):
    obj = entidad.query.filter(entidad.nombre == valor).filter(entidad.isActiv == True).first()
    return obj

def selectByValue(entidad, valor):
    objList = entidad.query.filter(entidad.codTipoParametro == valor).filter(entidad.isActiv == True).all()
    return objList

def selectAllActiveByParamCod(valor):
    objectList = ParametroOpcion.query.filter(ParametroOpcion.codParametro == valor).filter(ParametroOpcion.isActiv == True).all()
    return objectList
