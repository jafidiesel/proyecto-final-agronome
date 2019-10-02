class SessionUser():
    __tablename__ = 'sessionUser'
    cod = db.Column('cod_sessionUser',Integer,primary_key = True,index = True)
    codPublic = db.Column('cod_public_sessionUser', String(40), nullable = False)
    usuario = db.Column('usuario', String(80), nullable = False, unique = True)
    token = db.Column('token_sessionUser', String(120), nullable = False)
    
