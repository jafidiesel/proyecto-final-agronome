from flask import jsonify
from app.extensions import db

def saveEntidad(entidad):
    db.session.add(entidad)
    db.session.commit()
    return jsonify(entidad.to_json())


def selectAll(entidad):
    objList=entidad.query.all()
    return jsonify([obj.to_json() for obj in objList])



#esto solo funciona con codOpcion, para que funcione con todos hay que buscar la manera de armar 
#armar la condicpon dinamicamente o ponerle a todas las entidades cod como primary
#o seguir investigando como hace una dinamica
def selectCod(entidad,cod):
    obj = entidad.query.filter(entidad.codOpcion==cod).first()
    return jsonify(obj.to_json())