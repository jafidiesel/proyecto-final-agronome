from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlActividad
from app.uses_cases.moduloActividad.registrarActividad import registrarActivDetalle, consultarActivDetalle, putActivDetalle, deleteActivDetalle, getActivDetalle ,getParametrosFull
from app.api.helperApi.hlResponse import ResponseException, notCheck
from app.api.shared.tokenHandler import token_required

actividad = urlActividad

@actividad.route('/registrar')
class RegistrarActivHandler(Resource):
    @token_required
    def post(data,currentUser):
        return registrarActivDetalle(data,currentUser)

@actividad.route('/consultar')
class RegistrarActivHandler(Resource):
    @token_required
    def post(data,currentUser):
        return consultarActivDetalle(data)


@actividad.route('/<int:codActivDetalle>')
class RegistrarActivHandler(Resource):
    @token_required
    def get(data,currentUser,codActivDetalle):
        return getActivDetalle(codActivDetalle)
        

    @token_required
    def put(data,currentUser,codActivDetalle):
        return putActivDetalle(data,currentUser,codActivDetalle)
        

    @token_required
    def delete(data,currentUser,codActivDetalle):
        return deleteActivDetalle(data,codActivDetalle)

@actividad.route('/parametros/<int:codActividad>')
class RegistrarActivHandler(Resource):
    @token_required
    def get(data,currentUser,codActividad):
        return getParametrosFull(codActividad)
      