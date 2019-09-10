from flask import jsonify
from app.extensions import db

def saveEntidad(entidad):
    print(db.session.add(entidad))
    print(db.session.commit())
    return entidad


def selectAll(entidad):
    objList=entidad.query.all()
    return objList

def selectByCod(entidad,cod): ##si el codigo se llama cod
    obj = entidad.query.filter(entidad.cod==cod).first()
    return obj


def updateEntidad(entidad,cod,data): ##solo update nomencladores
    obj = entidad.query.filter(entidad.cod==cod).first()
    obj.nombre = data.get('nombre')
    obj.isActiv = data.get('isActiv')
    db.session.commit()
    return obj

##se puede borrar creo
def selectByCod2(entidad,cod):
    obj = entidad.query.filter(entidad.cod==cod).first()
    return obj
