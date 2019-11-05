from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlResgistrarActiv
from app.uses_cases.moduloActividad.registrarActividad import postRegistrarActiv, getRegistrarActiv, putRegistrarActiv, deleteRegistrarActiv, getRegistrarActivCod ,getParametrosFull
from app.api.helperApi.hlResponse import ResponseException, notCheck
from app.api.shared.tokenHandler import token_required

registrarActiv = urlResgistrarActiv

@registrarActiv.route('')
class RegistrarActivHandler(Resource):
    @token_required
    def post(data,currentUser):
        return postRegistrarActiv(data,currentUser)

    @token_required
    def get(data,currentUser):
        return getRegistrarActiv()


@registrarActiv.route('/<int:codActivDetalle>')
class RegistrarActivHandler(Resource):
    @token_required
    def get(data,currentUser,codActivDetalle):
        return getRegistrarActivCod(codActivDetalle)
        

    @token_required
    def put(data,currentUser,codActivDetalle):
        return putRegistrarActiv(data,currentUser,codActivDetalle)
        

    @token_required
    def delete(data,currentUser,codActivDetalle):
        return deleteRegistrarActiv(data,codActivDetalle)

@registrarActiv.route('/parametros/<int:codActividad>')
class RegistrarActivHandler(Resource):
    @token_required
    def get(data,currentUser,codActividad):
        return getParametrosFull(codActividad)
      