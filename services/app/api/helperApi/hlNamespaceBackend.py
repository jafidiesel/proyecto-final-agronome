from app.api.nomenclador_api import nomenclador
from app.api.parametro_api import parametro
from app.api.entidadInterm_api import entidadInterm
from app.api.registrarActividad_api import registrarActiv
from app.api.usuario_api import users
from app.api.login_api import loginUser

NAMESPACES = [
    nomenclador,
    parametro,
    entidadInterm,
    registrarActiv,
    users,
    loginUser
]