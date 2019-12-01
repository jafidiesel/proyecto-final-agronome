from flask import jsonify, request
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlPlanificacion, urlParcelas
from app.uses_cases.moduloPlanificacion.iniciarPlanificacion import getParcelas
from app.uses_cases.moduloPlanificacion.gestionarPlanificacion import postPlanificacion,getPlanificaciones
from app.api.shared.tokenHandler import token_required


planificacion = urlPlanificacion
parcelas = urlParcelas

@parcelas.route('/<int:cod>')
class ParcelasInicialHandler(Resource):
    @token_required
    def get(data,currentUser,cod):
        return getParcelas(cod) 

@planificacion.route('')
class PlanificacionHandler(Resource):
    @token_required
    def post(data,currentUser):
        return postPlanificacion(data,currentUser)
       
@planificacion.route('/consultar')
class PlanificacionHandler(Resource):
    @token_required
    def post(data,currentUser):
        return getPlanificaciones(data,currentUser)
