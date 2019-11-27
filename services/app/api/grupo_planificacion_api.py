from flask import jsonify, request
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlGrupoPlanificacion
from app.uses_cases.moduloPlanificacion.gestionarGrupo import getGrupoById, getAll
from app.api.shared.tokenHandler import token_required


grupoPlanificacion = urlGrupoPlanificacion

#Se obtienen los grupos por Finca
@grupoPlanificacion.route('/<int:cod>')
class GrupoPlanificacionHandler(Resource):
    @token_required
    def get(data,currentUser,cod):
        return getAll(currentUser,cod)
       
