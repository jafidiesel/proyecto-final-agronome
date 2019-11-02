from flask import jsonify, request
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlPlanificacion
from app.uses_cases.moduloPlanificacion.iniciarPlanificacion import iniciarPlanificacion
from app.api.shared.tokenHandler import token_required


planificacion = urlPlanificacion

@planificacion.route('/<int:cod>')
class PlanificacionInicialHandler(Resource):
    @token_required
    def get(data,currentUser):
        return iniciarPlanificacion(data) 
       

