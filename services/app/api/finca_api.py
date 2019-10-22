from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlFinca
from app.uses_cases.moduloGestionFinca.gestionarFinca import postFinca, getFincaCod , getFinca
from app.api.shared.tokenHandler import token_required

finca = urlFinca

@finca.route('')
class FincaHandler(Resource):
    @token_required
    def post(data,currentUser):
        return postFinca(data)
    @token_required
    def get(data,currentUser):
        return getFinca()

@finca.route('/<int:codFinca>')
class FincaHandler(Resource):
    @token_required
    def get(data,currentUser,codFinca):
        return getFincaCod(codFinca)
