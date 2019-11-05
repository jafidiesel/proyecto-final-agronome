from flask import jsonify, request
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlPlanificacionInicial
from app.uses_cases.moduloPlanificacion.iniciarPlanificacion import iniciarPlanificacion,crearPlanificacionInicial
from app.api.shared.tokenHandler import token_required


planificacion = urlPlanificacionInicial

@planificacion.route('/<int:cod>')
class PlanificacionInicialHandler(Resource):
    @token_required
    def get(data,currentUser,cod):
        return iniciarPlanificacion(cod) 

@planificacion.route('')
class PlanificacionInicialHandler(Resource):
    @token_required
    def post(data,currentUser):
        return crearPlanificacionInicial(data,currentUser)
       

