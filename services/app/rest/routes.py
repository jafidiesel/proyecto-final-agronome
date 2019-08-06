#https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/
from flask import Flask, render_template, request, redirect, url_for, flash
from app.models import *
import uuid, json
from flask_sqlalchemy import SQLAlchemy


#EstadoPlanificacion 
@app.route('/v1/configuracion/estadoPlanificacion', methods = ['GET'])
def getEstadoPlanificacion():
    if request.method == 'GET':
        #connex = engine.connect()
        #estado = select([EstadoPlanificacion])
        #estadoPlanificacion = connex.execute(estado).fetchone()
        return 'OK'

 #http://blog.luisrei.com/articles/flaskrest.html       
@app.route('/v1/configuracion/estadoPlanificacion', methods = ['POST'])
def setEstadoPlanificacion():
    if request.method == 'POST':
        estado_p = request.get_json()
        estado = EstadoPlanificacion( uuid.uuid1(),estado_p.get('cod_estado_planificacion'),estado_p.get('nombre_estado_planificacion'))
        db.session.add(estado) 
        db.session.commit()
        return 'OK'

