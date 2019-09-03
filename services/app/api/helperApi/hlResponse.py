from flask import make_response

server = 'Agronome'
contentType = 'application/json'


def ResponseException(e):
    cause = str(e.__cause__)
    if cause=='None':
        cause= 'no existe el tipoNomenclador'
    message = '"message":"{' + cause + '}"'
    response= make_response(message,400)
    response.headers['Server'] = server
    response.headers['Content-Type'] = contentType
    return response
