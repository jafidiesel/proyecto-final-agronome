from flask import jsonify, request
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlGrupoPlanificacion
from app.uses_cases.moduloPlanificacion.gestionarGrupo import getPlanificaciones, getAll
from app.api.shared.tokenHandler import token_required


grupoPlanificacion = urlGrupoPlanificacion

#Se obtienen los grupos por Finca
@grupoPlanificacion.route('/<int:cod>')
class GrupoPlanificacionHandler(Resource):
    @token_required
    def get(data,currentUser,cod):
        return getAll(currentUser,cod)
    
@grupoPlanificacion.route('')
class GrupoPlanificacionHandler(Resource):
    @token_required
    def post(data,currentUser):
        return getPlanificaciones(data,currentUser)

       

