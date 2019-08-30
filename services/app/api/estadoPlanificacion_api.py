from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlEstadoPlanificacion
from app.api.helperApi.hlDb import saveEntidad,selectAll
from app.extensions import db
from app.model.estadoPlanificacion import EstadoPlanificacion

estadoPlanificacion = urlEstadoPlanificacion

@estadoPlanificacion.route('')
class EstadoPlanificacionHandler(Resource):
    def get(self):
        return selectAll(EstadoPlanificacion)
    
    def post(self):
        data = self.api.payload
        estadoPlanificacion= EstadoPlanificacion.from_json(data)
        return saveEntidad(estadoPlanificacion)
        