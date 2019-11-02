from flask import jsonify, request
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlPlanificacion
from app.uses_cases.moduloPlanificacion.iniciarPlanificacion import iniciarPlanificacion

planificacion = urlPlanificacion

@planificacion.route('/<int:cod>')
class PlanificacionInicialHandler(Resource):
    def get(self,cod):
        return iniciarPlanificacion(cod) 
       

