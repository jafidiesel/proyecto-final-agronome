#definiciones de las rutas
from flask_restplus import Namespace

#modulo de configuraciones"
URL_MC = 'api/configuracion/'
urlNomenclador = Namespace(URL_MC + 'nomenclador')
urlParametro = Namespace(URL_MC + 'parametro')

#modulo de recursos
URL_MC = 'api/recurso/'

