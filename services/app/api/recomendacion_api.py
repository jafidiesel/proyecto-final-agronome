from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlRecomendacion
from app.uses_cases.moduloRecomendacion.registrarRecomendacion import postRegistrarRecom, recomendacionActividad, getRecomDetalle, getParametrosRecomFull
from app.api.shared.tokenHandler import token_required


recomendacion = urlRecomendacion

@recomendacion.route('/registrar')
class RegistrarRecomHandler(Resource):
    @token_required
    def post(data,currentUser):
        return postRegistrarRecom(data,currentUser)


@recomendacion.route('/<int:codRecomDetalle>')  
class RegistrarRecomHandler(Resource):
    @token_required
    def get(data,currentUser,codRecomDetalle):
        return getRecomDetalle(codRecomDetalle)


@recomendacion.route('/actividad')
class RegistrarRecomActivHandler(Resource):
    @token_required
    def post(data,currentUser):
        return recomendacionActividad(data)


@recomendacion.route('/parametros/<int:codRecomendacion>')
class RegistrarRecomParamHAndler(Resource):
    @token_required
    def get(data,currentUser,codRecomendacion):
        return getParametrosRecomFull(codRecomendacion)