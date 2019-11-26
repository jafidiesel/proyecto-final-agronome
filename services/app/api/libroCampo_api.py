from app.api.helperApi.hlUrl import urlLibroCampo
from flask_restplus import Resource
from app.uses_cases.libroCampo.libroCampo import consultarLibroCampo, finalizarLibroCampo, recomendacionLibroCampo
from app.api.shared.tokenHandler import token_required

libroCampo = urlLibroCampo

@libroCampo.route('')
class libroCampoHandler(Resource):
    @token_required
    def post(data,currentUser):
        return consultarLibroCampo(data)


@libroCampo.route('/finalizar')
class libroCampoHandler(Resource):
    @token_required
    def post(data,currentUser):
        return finalizarLibroCampo(data)


@libroCampo.route('/recomendacion')
class libroCampoHandler(Resource):
    @token_required
    def post(data,currentUser):
        return recomendacionLibroCampo(data)