
# Mapeo de clases.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.app import db

class EstadoPlanificacionEntity(db.Model):
    __tablename__ = 'estado_planificacion'
    uuid_estado_planificacion = db.Column('uuid_estado_planificacion', db.String(64), primary_key = True)
    cod_estado_planificacion = db.Column('cod_estado_planificacion', db.String(32), unique = True)
    nombre_estado_planificacion = db.Column('nombre_estado_planificacion', db.String(32), unique = True)
    is_active = db.Column('is_active', db.Boolean)



class TipoPlanificacionEntity(db.Model):
    __tablename__ = 'tipo_planificacion'
    uuid_tipo_planificacion = db.Column('uuid_tipo_planificacion', db.String(64), primary_key = True)
    cod_tipo_planificacion = db.Column('cod_tipo_planificacion', db.String(32), unique = True)
    nombre_tipo_planificacion = db.Column('nombre_tipo_planificacion', db.String(32), unique = True)
    desc_tipo_planificacion = db.Column('desc_tipo_planificacion', db.Text)
    is_active = db.Column('is_active', db.Boolean)



class OpcionEntity(db.Model):
    __tablename__ = 'opcion'
    uuid_opcion = db.Column('uuid_opcion', db.String(64), primary_key = True)
    cod_opcion = db.Column('cod_opcion', db.String(32), unique = True)
    nombre_opcion = db.Column('nombre_opcion', db.String(32), unique = True)
    is_active = db.Column('is_active', db.Boolean)


class PermisoEntity(db.Model):
    __tablename__ = 'permiso'
    uuid_permiso = db.Column('uuid_permiso', db.String(64), primary_key = True)
    cod_permiso = db.Column('cod_permiso', db.String(32), unique = True)
    nombre_permiso = db.Column('nombre_permiso', db.String(32), unique = True)
    is_active = db.Column('is_active', db.Boolean)


class RolEntity(db.Model):
    __tablename__ = 'rol'
    uuid_rol = db.Column('uuid_rol', db.String(64), primary_key = True)
    cod_rol = db.Column('cod_rol', db.String(32))
    nombre_rol = db.Column('nombre_rol', db.String(32))
    is_active = db.Column('is_active', db.Boolean)

class TipoAnalisisEntity(db.Model):
    __tablename__ = 'tipo_analisis'
    uuid_tipo_analisis = db.Column('uuid_tipo_analisis', db.String(64), primary_key = True)
    cod_tipo_analisis = db.Column('cod_tipo_analisis', db.String(32))
    nombre_tipo_analisis = db.Column('nombre_tipo_analisis', db.String(32))
    is_active = db.Column('is_active', db.Boolean)


class TipoPlanEntity(db.Model):
    __tablename__ = 'tipo_plan'
    uuid_tipo_plan = db.Column('uuid_tipo_plan', db.String(64), primary_key = True)
    cod_tipo_plan = db.Column('cod_tipo_plan', db.String(32))
    nombre_tipo_plan = db.Column('nombre_tipo_plan', db.String(32))
    is_active = db.Column('is_active', db.Boolean)


class TipoParametroEntity(db.Model):
    __tablename__ = 'tipo_parametro'
    uuid_tipo_parametro = db.Column('uuid_tipo_parametro', db.String(64), primary_key = True)
    cod_tipo_parametro = db.Column('cod_tipo_parametro', db.String(32))
    nombre_tipo_parametro = db.Column('nombre_tipo_parametro', db.String(32))
    is_active = db.Column('is_active', db.Boolean)


class TipoDatoEntity(db.Model):
    __tablename__ = 'tipo_dato'
    uuid_tipo_dato = db.Column('uuid_tipo_dato', db.String(64), primary_key = True)
    cod_tipo_dato = db.Column('cod_tipo_dato', db.String(32))
    nombre_tipo_dato = db.Column('nombre_tipo_dato', db.String(32))
    is_active = db.Column('is_active', db.Boolean)


class TipoRecursoEntity(db.Model):
    __tablename__ = 'tipo_recurso'
    uuid_tipo_recurso = db.Column('uuid_tipo_recurso', db.String(64), primary_key = True)
    cod_tipo_recurso = db.Column('cod_tipo_recurso', db.String(32))
    nombre_tipo_recurso = db.Column('nombre_recurso', db.String(32))
    is_active = db.Column('is_active', db.Boolean)


