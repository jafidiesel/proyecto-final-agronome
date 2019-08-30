from flask import jsonify
from app.extensions import db

def saveEntidad(entidad):
    db.session.add(entidad)
    db.session.commit()
    return jsonify(entidad.to_json())


def selectAll(entidad):
    objList=entidad.query.all()
    return jsonify([obj.to_json() for obj in objList])


def selectByCod(entidad,cod):
    obj = entidad.query.filter(entidad.cod==cod).first()
    return jsonify(obj.to_json())


def updateEntidad(entidad,cod,data):
    obj = entidad.query.filter(entidad.cod==cod).first()
    #print("aca estoy")
    #print(obj.)
    obj.nombre = data.get('nombre')
    obj.isActiv = data.get('isActiv')

    db.session.commit()
    return jsonify(obj.to_json())