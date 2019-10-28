from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlAnalisis
from app.uses_cases.analisis.gestionarAnalisis import postAnalisis, getAnalisisCod
from app.api.shared.tokenHandler import token_required
## ESTE OBJETO ES UN HELPER;

analisis = urlAnalisis

@analisis.route('')
class AnalisisHandler(Resource):
    @token_required
    def post(data,currentUser):
        return postAnalisis(data,currentUser)


@analisis.route('/<int:codAnalisis>')
class AnalisisHandler(Resource):
    @token_required
    def get(data,currentUser,codAnalisis):
        return getAnalisisCod(data,codAnalisis)