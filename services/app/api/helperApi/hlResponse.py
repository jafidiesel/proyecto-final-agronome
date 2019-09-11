from flask import make_response


StatusOk= {
"postEntidadIntermMSG":"Se ha creado correctamente la entidad intermedia"
}


server = 'Agronome'
contentType = 'application/json'


def ResponseException(e):
    messages=e.args
    message = messages[0]
    count = len(e.args)
    cause = str(e.__cause__)

    if count==1: ##exception automaticas
        if cause=='None':
            ExceptionResp=dict(flag='N',messages='revisar ' + message)
        else:
            ExceptionResp=dict(flag='N',messages=message)
    else: ##exception generadas
        ExceptionResp=dict(flag='N',messages=messages[1])

    response= make_response(ExceptionResp,400)
    response.headers['Server'] = server
    response.headers['Content-Type'] = contentType
    return response

def ResponseOk(clave):
    flag= 'S'
    messageOk = StatusOk[clave]
    msgResponse = dict(flag=flag,messages= messageOk)
    #msgResponse = 'okaa'
    response= make_response(msgResponse,200)
    response.headers['Server'] = server
    response.headers['Content-Type'] = contentType
    return response

