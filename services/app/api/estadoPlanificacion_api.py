from flask import jsonify
from flask_restplus import Resource, Namespace
from app.extensions import db
from app.model.estadoPlanificacion import EstadoPlanificacion

estadoPlanificacion = Namespace('estadoPlanificacion')

@estadoPlanificacion.route('')
class EstadoPlanificacionHandler(Resource):
    def get(self):
        estadosPlanificacion = EstadoPlanificacion.query.all()
        return jsonify([estadoPlanificacion.to_json() for estadoPlanificacion in estadosPlanificacion])
    
    def post(self):
        data = self.api.payload
        estadoPlanificacion= EstadoPlanificacion.from_json(data)
        db.session.add(estadoPlanificacion)
        db.session.commit()
        return jsonify(estadoPlanificacion.to_json())
        
