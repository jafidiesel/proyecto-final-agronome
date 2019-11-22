from app.api.nomenclador_api import nomenclador
from app.api.parametro_api import parametro
from app.api.entidadInterm_api import entidadInterm
from app.api.registrarActividad_api import registrarActiv
from app.api.usuario_api import users
from app.api.login_api import loginUser
from app.api.finca_api import finca
from app.api.registrarRecomendacion_api import registrarRecom
from app.api.analisis_api import analisis
from app.api.plan_api import plan
from app.api.planificacion_api import planificacion
from app.api.reporte_api import  reporte
from app.api.grupo_planificacion_api import grupoPlanificacion

NAMESPACES = [
    nomenclador,
    parametro,
    entidadInterm,
    registrarActiv,
    users,
    loginUser,
    finca,
    registrarRecom,
    analisis,
    plan,
    planificacion,
    reporte,
    grupoPlanificacion
]