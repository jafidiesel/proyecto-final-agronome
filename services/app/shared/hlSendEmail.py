from app.backend import app
from flask_mail import Mail, Message


hlSubject = {
    'activate'    : 'Activación de cuenta - Agronome',
    'recoverPass' : 'Restablecer contraseña - Agronome',
    'recomendacion' : 'Nueva recomendación - Agronome',
    'actividad': 'Nueva activida - Agronome'
}

hlReponseEmail = {
    'activate'    : 'Por favor revisa tu correo electrónico para activar la cuenta',
    'recoverPass' : 'Por favor revisa tu correo electrónico',
    'recomendacion' : 'Recomendación creada exitosamente',
    'actividad': 'Recomendación creada correctamente'
}

def sendEmail(subject, userList , body, html, additionals):
        with app.app_context():
            subjectAux  =  hlSubject[subject]
            recipients  =  hlEmailListByUsers(userList)
            mail        = Mail(app)
            msg         = Message(
                            subjectAux,
                            sender = app.config.get('MAIL_USERNAME'),
                            recipients = recipients
                            )
            msg.body    = body
            
            mail.send(msg)
            response    =  hlReponseEmail[subject]

        return response
     
def hlEmailListByUsers(userList):
    dtoEmailList = []
    for user in userList:
        dtoEmailList.append(user.email)
    
    return dtoEmailList