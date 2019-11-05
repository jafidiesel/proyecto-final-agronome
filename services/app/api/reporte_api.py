from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlReporte
from app.uses_cases.moduloReporte.generarReporte import actividadGfBar, recomendacionGfPie,actividadDualGfBar, actividadOptionGfPie
from app.api.shared.tokenHandler import token_required


reporte = urlReporte
#Todos tienen que ser post porque pueden enviar cosas que sirvan al reporte
@reporte.route('/actividadGfBar')
class ReporteHandler(Resource):
    @token_required
    def post(data,currentUser):
        return actividadGfBar(data,currentUser)


@reporte.route('/recomendacionGfPie')
class ReporteHandler(Resource):
    @token_required
    def post(data,currentUser):
        return recomendacionGfPie(data,currentUser)


@reporte.route('/actividadDualGfBar')
class ReporteHandler(Resource):
    @token_required
    def post(data,currentUser):
        return actividadDualGfBar(data,currentUser)

@reporte.route('/actividadOptionGfPie')
class ReporteHandler(Resource):
    @token_required
    def post(data,currentUser):
        return actividadOptionGfPie(data,currentUser)