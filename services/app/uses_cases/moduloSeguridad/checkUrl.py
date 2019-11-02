import re
from app.api.helperApi.hlUrl import URL_MC, urlResgistrarActiv,  urlUsuario, urlLogin ,urlNomenclador,urlFinca,urlRegistrarRecom , urlAnalisis, urlPlan, urlReporte
def checkUrl(method,pat,rol):
    urlAux = method + pat #armo url
    nro = re.sub("\D", "", urlAux) #busco si tiene algun numero
    url = re.sub(nro,"",urlAux)
    isCheck = False


    #Mudolo de configuración 

    #Nomencladores
    MCNOM = '/' + urlNomenclador.name
    MCNOM_GETS = 'GET' + MCNOM
    MCNOM_POST_FILTER = 'POST' + MCNOM + '/'
    isGetNomenclador = False
    isPostFilterNomenclador = False

    if url.count(MCNOM_GETS)>0:
        url = MCNOM_GETS
        isGetNomenclador = True

    if url.count(MCNOM_POST_FILTER)>0:
        url = MCNOM_POST_FILTER
        isPostFilterNomenclador = True
 
    #configuración de parametros y asociaciones
    MC = URL_MC
    if url.count(URL_MC)> 0 and not isGetNomenclador and not isPostFilterNomenclador:
        url = MC
    

    #Modulo de seguridad  
    isLogin=False 
    MSLOG = urlLogin.name #login     
    if url.count(MSLOG)>0:
        isLogin = True
        url = MSLOG

    MSUSU =  urlUsuario.name  #usuario
    if url.count(MSUSU)>0 and not isLogin: #tengo que hacer esta logica porque comparten url con el login
        url = MSUSU


    #Modulo Actividades
    MAREG = '/' + urlResgistrarActiv.name
    MAREG_POST = 'POST' + MAREG
    MAREG_GETS = 'GET' + MAREG
    MAREG_GET = MAREG_GETS  + '/'
    MAREG_PUT = 'PUT' + MAREG + '/'
    MAREG_DELETE = 'DELETE' + MAREG + '/'
    MAREG_PARAM = 'GET' + MAREG + '/parametros/'

    #Modulo de Gestion de Finca
    MGF = '/' + urlFinca.name
    MGF_POST =  'POST' + MGF 
    MGF_GETS = 'GET' + MGF
    MGF_GET = MGF_GETS  + '/'
    MGF_PUT = 'PUT' + MGF + '/'
    
    #Modulo de Recomendaciones
    MRREG = '/' + urlRegistrarRecom.name
    MRREG_POST =  'POST' + MRREG + '/registrar'
    MRRECOMACTIV_GET = 'GET' + MRREG + '/actividad' 
    MRREG_GET = 'GET' + MRREG + '/'
    MRREG_PARAM = 'GET' + MRREG + '/parametros/'
   
   
    #Helper
    #-analisis
    HLA = '/' + urlAnalisis.name
    HLA_POST = 'POST' + HLA
    HLA_GET  = 'GET' + HLA + '/'
    HLA_PARAM = 'GET' + HLA + '/parametros/'
    #-plan
    HLP = '/' + urlPlan.name
    HLP_POST = 'POST' + HLP
    HLP_GET  = 'GET' + HLP + '/'
    HLP_PARAM = 'GET' + HLP + '/parametros/'

    #MODULO DE REPORTES
    MREPOR = 'POST/' + urlReporte.name #son todos POST
    MREPOR_ACTIVBAR = MREPOR + '/actividadGfBar'
    MREPOR_RECOMPIE = MREPOR + '/recomendacionGfPie'


    #PERMISOS:
    default = (
        MSLOG,
        MCNOM_GETS,MCNOM_POST_FILTER,                 #Modulo de Configuración (Nomencladores)
        MGF_GETS, MGF_GET,                            #Modulo de finca
        MREPOR_ACTIVBAR,MREPOR_RECOMPIE                               #Modulo de reporte
        ) #todos

    administrador = (
        MC,                                           #Modulo de Confiraución (Parametros y asociaciones)
        MSUSU,                                        #Modulo de seguridad
        MAREG_POST, MAREG_GETS, MAREG_GET, MAREG_PUT, MAREG_DELETE, MAREG_PARAM, #Modulo de actividad
        MGF_POST,MGF_PUT,                             #Modulo de finca
        MRREG_POST, MRREG_GET, MRRECOMACTIV_GET, MRREG_PARAM, #Modulo de recomendaciones
        HLA_GET, HLA_POST, HLA_PARAM, HLP_POST, HLP_GET , HLP_PARAM #Helper Analisis - Plan
    ) + default
    
    encargadofinca = (
        MAREG_POST, MAREG_GETS, MAREG_GET, MAREG_PUT, MAREG_DELETE, MAREG_PARAM, #Modulo de actividad
        MGF_POST,MGF_PUT                              #Modulo de finca
         ) + default
    
    ingeniero = (  
        MAREG_GETS, MAREG_GET,                         #Modulo de actividad
        MRREG_POST, MRREG_GET, MRRECOMACTIV_GET, MRREG_PARAM, #Modulo de recomendaciones
        HLA_GET, HLA_POST, HLA_PARAM, HLP_POST, HLP_GET , HLP_PARAM #Helper Analisis - Plan
         )+ default

    supervisor = (  
        MAREG_POST, MAREG_GETS, MAREG_GET, MAREG_PUT  #Modulo de actividad
         )+ default


    #CHECK FINAL
    roles= {
    "administrador":administrador ,
    "encargadofinca":encargadofinca,
    "ingeniero":ingeniero,
    "supervisor": supervisor,
    }

    isCheck = url in roles[rol]
    #print(url)
    return isCheck
    