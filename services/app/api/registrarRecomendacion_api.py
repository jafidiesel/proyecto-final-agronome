from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlRegistrarRecom
from app.uses_cases.moduloRecomendacion.registrarRecomendacion import postRegistrarRecom, recomendacionActividad, getRecomDetalle, getParametrosRecomFull
from app.api.shared.tokenHandler import token_required


registrarRecom = urlRegistrarRecom

@registrarRecom.route('/registrar')
class RegistrarRecomHandler(Resource):
    @token_required
    def post(data,currentUser):
        return postRegistrarRecom(data,currentUser)


@registrarRecom.route('/<int:codRecomDetalle>')  
class RegistrarRecomHandler(Resource):
    @token_required
    def get(data,currentUser,codRecomDetalle):
        return getRecomDetalle(codRecomDetalle)




@registrarRecom.route('/actividad')
class RegistrarRecomActivHandler(Resource):
    @token_required
    def get(data,currentUser): #aca del usaurio puedo sacar las fincas
        return recomendacionActividad(currentUser)


@registrarRecom.route('/parametros/<int:codRecomendacion>')
class RegistrarRecomParamHAndler(Resource):
    @token_required
    def get(data,currentUser,codRecomendacion):
        return getParametrosRecomFull(codRecomendacion)