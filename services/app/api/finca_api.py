from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlFinca
from app.uses_cases.moduloGestionFinca.gestionarFinca import postFinca, getFincaCod , getFinca, putFinca
from app.api.shared.tokenHandler import token_required

finca = urlFinca

@finca.route('')
class FincaHandler(Resource):
    @token_required
    def post(data,currentUser):
        return postFinca(data,currentUser)
    @token_required
    def get(data,currentUser):
        return getFinca()

@finca.route('/<int:codFinca>')
class FincaHandler(Resource):
    @token_required
    def get(data,currentUser,codFinca):
        return getFincaCod(codFinca)

    @token_required
    def put(data,currentUser,codFinca):
        return putFinca(data,codFinca)
