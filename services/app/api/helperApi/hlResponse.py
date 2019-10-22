from flask import make_response


server = 'Agronome'
contentType = 'application/json'
    

errors = {
"(psycopg2.errors.UniqueViolation)":"existente",
"(psycopg2.errors.ForeignKeyViolation)": "No existe la instancia que desea asignar"
}
#AGREGAR ESTOOO es cuando no existe el objeto
#error de sintaxis: 'NoneType' object has no attribute 'nombre'"
def ResponseException(e):
    messages=e.args
    message = messages[0]
    count = len(e.args)
    cause = str(e.__cause__)

    if count==1: ##exception automaticas
        if cause=='None':
            ExceptionResp=dict(flag='N',message='error de sintaxis: ' + message)
        else:
            ExceptionResp = definirCauses(message)
    else: ##exception generadas
        ExceptionResp=dict(flag=messages[0],message=messages[1])

    response= make_response(ExceptionResp,400)
    response.headers['Server'] = server
    response.headers['Content-Type'] = contentType
    return response

def ResponseOk():
    flag= 'S'
    msgResponse = dict(flag=flag)
    #msgResponse = 'okaa'
    response= make_response(msgResponse,200)
    response.headers['Server'] = server
    response.headers['Content-Type'] = contentType
    return response

def notCheck(msg):
    flag = 'N'
    #msg ='No posee permisos para realizar esta acción'
    msgResponse = dict(flag=flag, message = msg)
    response= make_response(msgResponse,404)
    response.headers['Server'] = server
    response.headers['Content-Type'] = contentType
    return response


#def notCheckmsg(msg):


def definirCauses(msg):
    msgAux = 'X' #incializo x 
    llaves=errors.keys()

    for item in llaves:
        if msg.startswith(item):
           msgAux =  errors[item] #en caso de estar en los errores lo parseo

    if msgAux =='X':
       msgAux = msg

    ExceptionResp=dict(flag='N',message=msgAux)
    return  ExceptionResp