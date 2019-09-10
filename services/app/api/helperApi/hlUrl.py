#definiciones de las rutas
from flask_restplus import Namespace

#modulo de configuraciones"
URL_MC = 'api/configuracion/'
urlNomenclador = Namespace(URL_MC + 'nomenclador')
urlParametro = Namespace(URL_MC + 'parametro')
urlActivParam = Namespace(URL_MC + 'activParam')

#modulo de recursos
URL_MR = 'api/recurso/'
urlRecurso=Namespace(URL_MR)


