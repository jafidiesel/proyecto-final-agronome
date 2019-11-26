from app.api.helperApi.hlUrl import urlLibroCampo
from flask_restplus import Resource
from app.uses_cases.libroCampo.libroCampo import getLibroCampo, finalizarLibroCampo
from app.api.shared.tokenHandler import token_required

libroCampo = urlLibroCampo

@libroCampo.route('')
class libroCampoHandler(Resource):
    @token_required
    def post(data,currentUser):
        return getLibroCampo(data)


@libroCampo.route('/finalizar')
class libroCampoHandler(Resource):
    @token_required
    def post(data,currentUser):
        return finalizarLibroCampo(data)