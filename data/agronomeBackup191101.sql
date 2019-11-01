--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.14
-- Dumped by pg_dump version 9.6.14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: activ_detalle_param; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.activ_detalle_param (
    fk_cod_activ_detalle integer NOT NULL,
    fk_cod_parametro integer NOT NULL,
    valor character varying
);


ALTER TABLE public.activ_detalle_param OWNER TO postgres;

--
-- Name: actividad; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actividad (
    cod_actividad integer NOT NULL,
    nombre_actividad character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.actividad OWNER TO postgres;

--
-- Name: actividad_cod_actividad_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actividad_cod_actividad_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actividad_cod_actividad_seq OWNER TO postgres;

--
-- Name: actividad_cod_actividad_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actividad_cod_actividad_seq OWNED BY public.actividad.cod_actividad;


--
-- Name: actividad_detalle; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actividad_detalle (
    cod_activ_detalle integer NOT NULL,
    fch_activ_detalle timestamp without time zone,
    observacion character varying(1024),
    is_eliminado boolean NOT NULL,
    fk_cod_actividad integer NOT NULL,
    fk_cod_recom_detalle integer,
    fk_cod_usuario integer NOT NULL
);


ALTER TABLE public.actividad_detalle OWNER TO postgres;

--
-- Name: actividad_detalle_cod_activ_detalle_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actividad_detalle_cod_activ_detalle_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actividad_detalle_cod_activ_detalle_seq OWNER TO postgres;

--
-- Name: actividad_detalle_cod_activ_detalle_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actividad_detalle_cod_activ_detalle_seq OWNED BY public.actividad_detalle.cod_activ_detalle;


--
-- Name: actividad_parametro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actividad_parametro (
    is_activ boolean NOT NULL,
    fk_cod_parametro integer NOT NULL,
    fk_cod_actividad integer NOT NULL
);


ALTER TABLE public.actividad_parametro OWNER TO postgres;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: analisis; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.analisis (
    cod_analisis integer NOT NULL,
    fch_analisis timestamp without time zone,
    fk_cod_tipo_analisis integer NOT NULL,
    fk_cod_usuario integer NOT NULL,
    fk_cod_recom_detalle integer,
    fk_cod_grupo_cuadro integer
);


ALTER TABLE public.analisis OWNER TO postgres;

--
-- Name: analisis_cod_analisis_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.analisis_cod_analisis_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.analisis_cod_analisis_seq OWNER TO postgres;

--
-- Name: analisis_cod_analisis_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.analisis_cod_analisis_seq OWNED BY public.analisis.cod_analisis;


--
-- Name: analisis_param; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.analisis_param (
    fk_cod_analisis integer NOT NULL,
    fk_cod_parametro integer NOT NULL,
    valor character varying
);


ALTER TABLE public.analisis_param OWNER TO postgres;

--
-- Name: cuadro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cuadro (
    cod_cuadro integer NOT NULL,
    nombre_cuadro character varying(256) NOT NULL,
    fk_cod_parcela integer NOT NULL
);


ALTER TABLE public.cuadro OWNER TO postgres;

--
-- Name: cuadro_cod_cuadro_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cuadro_cod_cuadro_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cuadro_cod_cuadro_seq OWNER TO postgres;

--
-- Name: cuadro_cod_cuadro_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cuadro_cod_cuadro_seq OWNED BY public.cuadro.cod_cuadro;


--
-- Name: cuadro_cultivo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cuadro_cultivo (
    cod_cuadro_cultivo integer NOT NULL,
    fch_ini timestamp without time zone,
    fch_fin timestamp without time zone,
    fk_cod_grupo_cuadro integer,
    fk_cod_cultivo integer,
    fk_cod_cuadro integer
);


ALTER TABLE public.cuadro_cultivo OWNER TO postgres;

--
-- Name: cuadro_cultivo_cod_cuadro_cultivo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cuadro_cultivo_cod_cuadro_cultivo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cuadro_cultivo_cod_cuadro_cultivo_seq OWNER TO postgres;

--
-- Name: cuadro_cultivo_cod_cuadro_cultivo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cuadro_cultivo_cod_cuadro_cultivo_seq OWNED BY public.cuadro_cultivo.cod_cuadro_cultivo;


--
-- Name: cultivo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cultivo (
    cod_cultivo integer NOT NULL,
    cantidad_cultivo integer NOT NULL,
    produccion_esperada double precision NOT NULL,
    variedad_cultivo character varying(120) NOT NULL,
    ciclo_unico boolean NOT NULL,
    fk_cod_tipo_cultivo integer,
    fk_cod_estado_planificacion integer
);


ALTER TABLE public.cultivo OWNER TO postgres;

--
-- Name: cultivo_cod_cultivo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cultivo_cod_cultivo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cultivo_cod_cultivo_seq OWNER TO postgres;

--
-- Name: cultivo_cod_cultivo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cultivo_cod_cultivo_seq OWNED BY public.cultivo.cod_cultivo;


--
-- Name: estado_planificacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estado_planificacion (
    cod_estado_planificacion integer NOT NULL,
    nombre_estado_planificacion character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.estado_planificacion OWNER TO postgres;

--
-- Name: estado_planificacion_cod_estado_planificacion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.estado_planificacion_cod_estado_planificacion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.estado_planificacion_cod_estado_planificacion_seq OWNER TO postgres;

--
-- Name: estado_planificacion_cod_estado_planificacion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.estado_planificacion_cod_estado_planificacion_seq OWNED BY public.estado_planificacion.cod_estado_planificacion;


--
-- Name: finca; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.finca (
    cod_finca integer NOT NULL,
    nombre_finca character varying(256) NOT NULL,
    superficie double precision NOT NULL,
    is_activ boolean NOT NULL,
    calle_finca character varying(256),
    nro_finca integer,
    localidad_finca character varying(50),
    provincia_finca character varying(50)
);


ALTER TABLE public.finca OWNER TO postgres;

--
-- Name: finca_cod_finca_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.finca_cod_finca_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.finca_cod_finca_seq OWNER TO postgres;

--
-- Name: finca_cod_finca_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.finca_cod_finca_seq OWNED BY public.finca.cod_finca;


--
-- Name: finca_usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.finca_usuario (
    fk_cod_finca integer NOT NULL,
    fk_cod_usuario integer NOT NULL,
    fch_ini timestamp without time zone,
    fch_fin timestamp without time zone,
    is_activ boolean NOT NULL
);


ALTER TABLE public.finca_usuario OWNER TO postgres;

--
-- Name: grupo_cuadro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.grupo_cuadro (
    cod_grupo_cuadro integer NOT NULL,
    fk_cod_parcela integer,
    fk_cod_planificacion integer
);


ALTER TABLE public.grupo_cuadro OWNER TO postgres;

--
-- Name: grupo_cuadro_cod_grupo_cuadro_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.grupo_cuadro_cod_grupo_cuadro_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.grupo_cuadro_cod_grupo_cuadro_seq OWNER TO postgres;

--
-- Name: grupo_cuadro_cod_grupo_cuadro_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.grupo_cuadro_cod_grupo_cuadro_seq OWNED BY public.grupo_cuadro.cod_grupo_cuadro;


--
-- Name: grupo_planificacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.grupo_planificacion (
    cod_grupo_planificacion integer NOT NULL,
    fch_creacion timestamp without time zone,
    comentario_planificacion character varying(120) NOT NULL
);


ALTER TABLE public.grupo_planificacion OWNER TO postgres;

--
-- Name: grupo_planificacion_cod_grupo_planificacion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.grupo_planificacion_cod_grupo_planificacion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.grupo_planificacion_cod_grupo_planificacion_seq OWNER TO postgres;

--
-- Name: grupo_planificacion_cod_grupo_planificacion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.grupo_planificacion_cod_grupo_planificacion_seq OWNED BY public.grupo_planificacion.cod_grupo_planificacion;


--
-- Name: img_activ_detalle; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.img_activ_detalle (
    cod_img integer NOT NULL,
    descrip_img character varying(256),
    img_base64 character varying(999999) NOT NULL,
    fk_cod_activ_detalle integer NOT NULL
);


ALTER TABLE public.img_activ_detalle OWNER TO postgres;

--
-- Name: img_activ_detalle_cod_img_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.img_activ_detalle_cod_img_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.img_activ_detalle_cod_img_seq OWNER TO postgres;

--
-- Name: img_activ_detalle_cod_img_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.img_activ_detalle_cod_img_seq OWNED BY public.img_activ_detalle.cod_img;


--
-- Name: opcion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.opcion (
    cod_opcion integer NOT NULL,
    nombre_opcion character varying(80) NOT NULL,
    is_activ boolean
);


ALTER TABLE public.opcion OWNER TO postgres;

--
-- Name: opcion_cod_opcion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.opcion_cod_opcion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.opcion_cod_opcion_seq OWNER TO postgres;

--
-- Name: opcion_cod_opcion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.opcion_cod_opcion_seq OWNED BY public.opcion.cod_opcion;


--
-- Name: parametro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parametro (
    cod_parametro integer NOT NULL,
    nombre_parametro character varying(80) NOT NULL,
    is_activ boolean NOT NULL,
    fk_cod_tipo_parametro integer,
    fk_cod_tipo_dato integer
);


ALTER TABLE public.parametro OWNER TO postgres;

--
-- Name: parametro_cod_parametro_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parametro_cod_parametro_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parametro_cod_parametro_seq OWNER TO postgres;

--
-- Name: parametro_cod_parametro_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parametro_cod_parametro_seq OWNED BY public.parametro.cod_parametro;


--
-- Name: parametro_opcion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parametro_opcion (
    is_activ boolean NOT NULL,
    fk_cod_parametro integer NOT NULL,
    fk_cod_opcion integer NOT NULL
);


ALTER TABLE public.parametro_opcion OWNER TO postgres;

--
-- Name: parcela; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parcela (
    cod_parcela integer NOT NULL,
    nombre_parcela character varying(256) NOT NULL,
    superficie_parcela double precision NOT NULL,
    filas integer NOT NULL,
    columnas integer NOT NULL,
    fk_cod_finca integer NOT NULL
);


ALTER TABLE public.parcela OWNER TO postgres;

--
-- Name: parcela_cod_parcela_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.parcela_cod_parcela_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parcela_cod_parcela_seq OWNER TO postgres;

--
-- Name: parcela_cod_parcela_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.parcela_cod_parcela_seq OWNED BY public.parcela.cod_parcela;


--
-- Name: permiso; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.permiso (
    cod_permiso integer NOT NULL,
    nombre_permiso character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.permiso OWNER TO postgres;

--
-- Name: permiso_cod_permiso_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.permiso_cod_permiso_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.permiso_cod_permiso_seq OWNER TO postgres;

--
-- Name: permiso_cod_permiso_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.permiso_cod_permiso_seq OWNED BY public.permiso.cod_permiso;


--
-- Name: plan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.plan (
    cod_plan integer NOT NULL,
    fch_plan timestamp without time zone,
    fk_cod_tipo_plan integer NOT NULL,
    fk_cod_usuario integer NOT NULL,
    fk_cod_grupo_cuadro integer
);


ALTER TABLE public.plan OWNER TO postgres;

--
-- Name: plan_cod_plan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.plan_cod_plan_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.plan_cod_plan_seq OWNER TO postgres;

--
-- Name: plan_cod_plan_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.plan_cod_plan_seq OWNED BY public.plan.cod_plan;


--
-- Name: plan_param; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.plan_param (
    fk_cod_plan integer NOT NULL,
    fk_cod_parametro integer NOT NULL,
    valor character varying NOT NULL
);


ALTER TABLE public.plan_param OWNER TO postgres;

--
-- Name: planificacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.planificacion (
    cod_planificacion integer NOT NULL,
    fch_planificacion timestamp without time zone,
    comentario_planificacion text,
    fk_cod_tipo_planificacion integer,
    fk_cod_estado_planificacion integer,
    fk_cod_finca integer,
    fk_cod_grupo_planificacion integer,
    fk_cod_usuario integer NOT NULL
);


ALTER TABLE public.planificacion OWNER TO postgres;

--
-- Name: planificacion_cod_planificacion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.planificacion_cod_planificacion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planificacion_cod_planificacion_seq OWNER TO postgres;

--
-- Name: planificacion_cod_planificacion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.planificacion_cod_planificacion_seq OWNED BY public.planificacion.cod_planificacion;


--
-- Name: recom_detalle_param; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recom_detalle_param (
    fk_cod_recom_detalle integer NOT NULL,
    fk_cod_parametro integer NOT NULL,
    valor character varying
);


ALTER TABLE public.recom_detalle_param OWNER TO postgres;

--
-- Name: recomendacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recomendacion (
    cod_recomendacion integer NOT NULL,
    nombre_recomendacion character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.recomendacion OWNER TO postgres;

--
-- Name: recomendacion_cod_recomendacion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recomendacion_cod_recomendacion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recomendacion_cod_recomendacion_seq OWNER TO postgres;

--
-- Name: recomendacion_cod_recomendacion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recomendacion_cod_recomendacion_seq OWNED BY public.recomendacion.cod_recomendacion;


--
-- Name: recomendacion_detalle; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recomendacion_detalle (
    cod_recom_detalle integer NOT NULL,
    fch_recom_detalle timestamp without time zone,
    observacion character varying(1024),
    is_eliminado boolean NOT NULL,
    is_aplicada boolean,
    fk_cod_recomendacion integer NOT NULL,
    fk_cod_usuario integer NOT NULL
);


ALTER TABLE public.recomendacion_detalle OWNER TO postgres;

--
-- Name: recomendacion_detalle_cod_recom_detalle_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recomendacion_detalle_cod_recom_detalle_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recomendacion_detalle_cod_recom_detalle_seq OWNER TO postgres;

--
-- Name: recomendacion_detalle_cod_recom_detalle_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recomendacion_detalle_cod_recom_detalle_seq OWNED BY public.recomendacion_detalle.cod_recom_detalle;


--
-- Name: recomendacion_parametro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recomendacion_parametro (
    is_activ boolean NOT NULL,
    fk_cod_parametro integer NOT NULL,
    fk_cod_recomendacion integer NOT NULL
);


ALTER TABLE public.recomendacion_parametro OWNER TO postgres;

--
-- Name: recurso; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recurso (
    cod_recurso integer NOT NULL,
    nombre_recurso character varying(80) NOT NULL,
    is_activ boolean NOT NULL,
    fk_tipo_recurso integer
);


ALTER TABLE public.recurso OWNER TO postgres;

--
-- Name: recurso_cod_recurso_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recurso_cod_recurso_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recurso_cod_recurso_seq OWNER TO postgres;

--
-- Name: recurso_cod_recurso_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recurso_cod_recurso_seq OWNED BY public.recurso.cod_recurso;


--
-- Name: rol; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rol (
    cod_rol integer NOT NULL,
    nombre_rol character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.rol OWNER TO postgres;

--
-- Name: rol_cod_rol_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rol_cod_rol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rol_cod_rol_seq OWNER TO postgres;

--
-- Name: rol_cod_rol_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rol_cod_rol_seq OWNED BY public.rol.cod_rol;


--
-- Name: sessionUser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."sessionUser" (
    "cod_sessionUser" integer NOT NULL,
    "cod_public_sessionUser" character varying(40) NOT NULL,
    usuario character varying(80) NOT NULL,
    "token_sessionUser" character varying(500) NOT NULL,
    rol_usuario character varying(80) NOT NULL
);


ALTER TABLE public."sessionUser" OWNER TO postgres;

--
-- Name: sessionUser_cod_sessionUser_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."sessionUser_cod_sessionUser_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."sessionUser_cod_sessionUser_seq" OWNER TO postgres;

--
-- Name: sessionUser_cod_sessionUser_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."sessionUser_cod_sessionUser_seq" OWNED BY public."sessionUser"."cod_sessionUser";


--
-- Name: tipo_analisis; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_analisis (
    cod_tipo_analisis integer NOT NULL,
    nombre_tipo_analisis character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.tipo_analisis OWNER TO postgres;

--
-- Name: tipo_analisis_cod_tipo_analisis_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_analisis_cod_tipo_analisis_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_analisis_cod_tipo_analisis_seq OWNER TO postgres;

--
-- Name: tipo_analisis_cod_tipo_analisis_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_analisis_cod_tipo_analisis_seq OWNED BY public.tipo_analisis.cod_tipo_analisis;


--
-- Name: tipo_analisis_param; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_analisis_param (
    is_activ boolean NOT NULL,
    fk_cod_parametro integer NOT NULL,
    fk_cod_tipo_analisis integer NOT NULL
);


ALTER TABLE public.tipo_analisis_param OWNER TO postgres;

--
-- Name: tipo_cultivo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_cultivo (
    cod_tipo_cultivo integer NOT NULL,
    nombre_tipo_cultivo character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.tipo_cultivo OWNER TO postgres;

--
-- Name: tipo_cultivo_cod_tipo_cultivo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_cultivo_cod_tipo_cultivo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_cultivo_cod_tipo_cultivo_seq OWNER TO postgres;

--
-- Name: tipo_cultivo_cod_tipo_cultivo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_cultivo_cod_tipo_cultivo_seq OWNED BY public.tipo_cultivo.cod_tipo_cultivo;


--
-- Name: tipo_dato; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_dato (
    cod_tipo_dato integer NOT NULL,
    nombre_tipo_dato character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.tipo_dato OWNER TO postgres;

--
-- Name: tipo_dato_cod_tipo_dato_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_dato_cod_tipo_dato_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_dato_cod_tipo_dato_seq OWNER TO postgres;

--
-- Name: tipo_dato_cod_tipo_dato_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_dato_cod_tipo_dato_seq OWNED BY public.tipo_dato.cod_tipo_dato;


--
-- Name: tipo_parametro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_parametro (
    cod_tipo_parametro integer NOT NULL,
    nombre_tipo_parametro character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.tipo_parametro OWNER TO postgres;

--
-- Name: tipo_parametro_cod_tipo_parametro_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_parametro_cod_tipo_parametro_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_parametro_cod_tipo_parametro_seq OWNER TO postgres;

--
-- Name: tipo_parametro_cod_tipo_parametro_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_parametro_cod_tipo_parametro_seq OWNED BY public.tipo_parametro.cod_tipo_parametro;


--
-- Name: tipo_plan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_plan (
    cod_tipo_plan integer NOT NULL,
    nombre_tipo_plan character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.tipo_plan OWNER TO postgres;

--
-- Name: tipo_plan_cod_tipo_plan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_plan_cod_tipo_plan_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_plan_cod_tipo_plan_seq OWNER TO postgres;

--
-- Name: tipo_plan_cod_tipo_plan_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_plan_cod_tipo_plan_seq OWNED BY public.tipo_plan.cod_tipo_plan;


--
-- Name: tipo_plan_param; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_plan_param (
    is_activ boolean NOT NULL,
    fk_cod_parametro integer NOT NULL,
    fk_cod_tipo_plan integer NOT NULL
);


ALTER TABLE public.tipo_plan_param OWNER TO postgres;

--
-- Name: tipo_planificacion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_planificacion (
    cod_tipo_planificacion integer NOT NULL,
    nombre_tipo_planificacion character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.tipo_planificacion OWNER TO postgres;

--
-- Name: tipo_planificacion_cod_tipo_planificacion_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_planificacion_cod_tipo_planificacion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_planificacion_cod_tipo_planificacion_seq OWNER TO postgres;

--
-- Name: tipo_planificacion_cod_tipo_planificacion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_planificacion_cod_tipo_planificacion_seq OWNED BY public.tipo_planificacion.cod_tipo_planificacion;


--
-- Name: tipo_recurso; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_recurso (
    cod_tipo_recurso integer NOT NULL,
    nombre_tipo_recurso character varying(80) NOT NULL,
    is_activ boolean NOT NULL
);


ALTER TABLE public.tipo_recurso OWNER TO postgres;

--
-- Name: tipo_recurso_cod_tipo_recurso_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_recurso_cod_tipo_recurso_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_recurso_cod_tipo_recurso_seq OWNER TO postgres;

--
-- Name: tipo_recurso_cod_tipo_recurso_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_recurso_cod_tipo_recurso_seq OWNED BY public.tipo_recurso.cod_tipo_recurso;


--
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    cod_usuario_private integer NOT NULL,
    cod_usuario character varying(40) NOT NULL,
    usuario character varying(80) NOT NULL,
    nombre_usuario character varying(80) NOT NULL,
    apellido_usuario character varying(80) NOT NULL,
    email_usuario character varying NOT NULL,
    contrasenia_usuario character varying(80) NOT NULL,
    "fchCrea_usuario" date,
    random_contrasenia_usuario character varying(80),
    is_recuperar boolean,
    fk_cod_rol integer,
    is_activ boolean NOT NULL
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- Name: usuario_cod_usuario_private_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuario_cod_usuario_private_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usuario_cod_usuario_private_seq OWNER TO postgres;

--
-- Name: usuario_cod_usuario_private_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuario_cod_usuario_private_seq OWNED BY public.usuario.cod_usuario_private;


--
-- Name: actividad cod_actividad; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad ALTER COLUMN cod_actividad SET DEFAULT nextval('public.actividad_cod_actividad_seq'::regclass);


--
-- Name: actividad_detalle cod_activ_detalle; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad_detalle ALTER COLUMN cod_activ_detalle SET DEFAULT nextval('public.actividad_detalle_cod_activ_detalle_seq'::regclass);


--
-- Name: analisis cod_analisis; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.analisis ALTER COLUMN cod_analisis SET DEFAULT nextval('public.analisis_cod_analisis_seq'::regclass);


--
-- Name: cuadro cod_cuadro; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cuadro ALTER COLUMN cod_cuadro SET DEFAULT nextval('public.cuadro_cod_cuadro_seq'::regclass);


--
-- Name: cuadro_cultivo cod_cuadro_cultivo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cuadro_cultivo ALTER COLUMN cod_cuadro_cultivo SET DEFAULT nextval('public.cuadro_cultivo_cod_cuadro_cultivo_seq'::regclass);


--
-- Name: cultivo cod_cultivo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cultivo ALTER COLUMN cod_cultivo SET DEFAULT nextval('public.cultivo_cod_cultivo_seq'::regclass);


--
-- Name: estado_planificacion cod_estado_planificacion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estado_planificacion ALTER COLUMN cod_estado_planificacion SET DEFAULT nextval('public.estado_planificacion_cod_estado_planificacion_seq'::regclass);


--
-- Name: finca cod_finca; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.finca ALTER COLUMN cod_finca SET DEFAULT nextval('public.finca_cod_finca_seq'::regclass);


--
-- Name: grupo_cuadro cod_grupo_cuadro; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_cuadro ALTER COLUMN cod_grupo_cuadro SET DEFAULT nextval('public.grupo_cuadro_cod_grupo_cuadro_seq'::regclass);


--
-- Name: grupo_planificacion cod_grupo_planificacion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_planificacion ALTER COLUMN cod_grupo_planificacion SET DEFAULT nextval('public.grupo_planificacion_cod_grupo_planificacion_seq'::regclass);


--
-- Name: img_activ_detalle cod_img; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.img_activ_detalle ALTER COLUMN cod_img SET DEFAULT nextval('public.img_activ_detalle_cod_img_seq'::regclass);


--
-- Name: opcion cod_opcion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opcion ALTER COLUMN cod_opcion SET DEFAULT nextval('public.opcion_cod_opcion_seq'::regclass);


--
-- Name: parametro cod_parametro; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parametro ALTER COLUMN cod_parametro SET DEFAULT nextval('public.parametro_cod_parametro_seq'::regclass);


--
-- Name: parcela cod_parcela; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parcela ALTER COLUMN cod_parcela SET DEFAULT nextval('public.parcela_cod_parcela_seq'::regclass);


--
-- Name: permiso cod_permiso; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permiso ALTER COLUMN cod_permiso SET DEFAULT nextval('public.permiso_cod_permiso_seq'::regclass);


--
-- Name: plan cod_plan; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plan ALTER COLUMN cod_plan SET DEFAULT nextval('public.plan_cod_plan_seq'::regclass);


--
-- Name: planificacion cod_planificacion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planificacion ALTER COLUMN cod_planificacion SET DEFAULT nextval('public.planificacion_cod_planificacion_seq'::regclass);


--
-- Name: recomendacion cod_recomendacion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion ALTER COLUMN cod_recomendacion SET DEFAULT nextval('public.recomendacion_cod_recomendacion_seq'::regclass);


--
-- Name: recomendacion_detalle cod_recom_detalle; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion_detalle ALTER COLUMN cod_recom_detalle SET DEFAULT nextval('public.recomendacion_detalle_cod_recom_detalle_seq'::regclass);


--
-- Name: recurso cod_recurso; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recurso ALTER COLUMN cod_recurso SET DEFAULT nextval('public.recurso_cod_recurso_seq'::regclass);


--
-- Name: rol cod_rol; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rol ALTER COLUMN cod_rol SET DEFAULT nextval('public.rol_cod_rol_seq'::regclass);


--
-- Name: sessionUser cod_sessionUser; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sessionUser" ALTER COLUMN "cod_sessionUser" SET DEFAULT nextval('public."sessionUser_cod_sessionUser_seq"'::regclass);


--
-- Name: tipo_analisis cod_tipo_analisis; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_analisis ALTER COLUMN cod_tipo_analisis SET DEFAULT nextval('public.tipo_analisis_cod_tipo_analisis_seq'::regclass);


--
-- Name: tipo_cultivo cod_tipo_cultivo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_cultivo ALTER COLUMN cod_tipo_cultivo SET DEFAULT nextval('public.tipo_cultivo_cod_tipo_cultivo_seq'::regclass);


--
-- Name: tipo_dato cod_tipo_dato; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_dato ALTER COLUMN cod_tipo_dato SET DEFAULT nextval('public.tipo_dato_cod_tipo_dato_seq'::regclass);


--
-- Name: tipo_parametro cod_tipo_parametro; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_parametro ALTER COLUMN cod_tipo_parametro SET DEFAULT nextval('public.tipo_parametro_cod_tipo_parametro_seq'::regclass);


--
-- Name: tipo_plan cod_tipo_plan; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_plan ALTER COLUMN cod_tipo_plan SET DEFAULT nextval('public.tipo_plan_cod_tipo_plan_seq'::regclass);


--
-- Name: tipo_planificacion cod_tipo_planificacion; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_planificacion ALTER COLUMN cod_tipo_planificacion SET DEFAULT nextval('public.tipo_planificacion_cod_tipo_planificacion_seq'::regclass);


--
-- Name: tipo_recurso cod_tipo_recurso; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_recurso ALTER COLUMN cod_tipo_recurso SET DEFAULT nextval('public.tipo_recurso_cod_tipo_recurso_seq'::regclass);


--
-- Name: usuario cod_usuario_private; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN cod_usuario_private SET DEFAULT nextval('public.usuario_cod_usuario_private_seq'::regclass);


--
-- Data for Name: activ_detalle_param; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.activ_detalle_param (fk_cod_activ_detalle, fk_cod_parametro, valor) FROM stdin;
\.


--
-- Data for Name: actividad; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actividad (cod_actividad, nombre_actividad, is_activ) FROM stdin;
1	riego	t
2	siembra	t
3	fertilización	t
7	detección catastrofe	t
8	detección fitosanitaria	t
4	preparación suelo	t
6	cosecha	t
5	tratamiento fitosanitario	t
9	fertirrigación	t
\.


--
-- Name: actividad_cod_actividad_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actividad_cod_actividad_seq', 9, true);


--
-- Data for Name: actividad_detalle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actividad_detalle (cod_activ_detalle, fch_activ_detalle, observacion, is_eliminado, fk_cod_actividad, fk_cod_recom_detalle, fk_cod_usuario) FROM stdin;
\.


--
-- Name: actividad_detalle_cod_activ_detalle_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actividad_detalle_cod_activ_detalle_seq', 1, true);


--
-- Data for Name: actividad_parametro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actividad_parametro (is_activ, fk_cod_parametro, fk_cod_actividad) FROM stdin;
t	45	1
t	46	1
t	47	1
t	48	1
t	49	1
t	50	2
t	51	2
t	52	2
t	53	2
t	54	2
t	55	2
t	56	3
t	57	3
t	58	3
t	59	3
t	60	3
t	61	4
t	62	4
t	63	4
t	64	5
t	65	5
t	66	5
t	67	5
t	68	5
t	69	5
t	59	5
t	70	5
t	71	6
t	72	6
t	73	7
t	74	8
t	75	9
t	76	9
t	77	9
t	78	9
t	79	9
t	80	9
t	81	9
t	82	9
t	49	9
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
87bc280ec04a
\.


--
-- Data for Name: analisis; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.analisis (cod_analisis, fch_analisis, fk_cod_tipo_analisis, fk_cod_usuario, fk_cod_recom_detalle, fk_cod_grupo_cuadro) FROM stdin;
\.


--
-- Name: analisis_cod_analisis_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.analisis_cod_analisis_seq', 21, true);


--
-- Data for Name: analisis_param; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.analisis_param (fk_cod_analisis, fk_cod_parametro, valor) FROM stdin;
\.


--
-- Data for Name: cuadro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cuadro (cod_cuadro, nombre_cuadro, fk_cod_parcela) FROM stdin;
32	A11	6
33	A12	6
34	A21	6
35	A22	6
36	A31	6
37	A32	6
38	A41	6
39	A42	6
40	B11	7
41	B21	7
42	B31	7
43	B41	7
44	B51	7
45	B61	7
46	B71	7
47	A11	8
48	A12	8
49	A21	8
50	A22	8
51	A31	8
52	A32	8
53	A41	8
54	A42	8
55	B11	9
56	B21	9
57	B31	9
58	B41	9
59	B51	9
60	B61	9
61	B71	9
62	A11	10
63	A12	10
64	A21	10
65	A22	10
66	A31	10
67	A32	10
68	A41	10
69	A42	10
70	B11	11
71	B21	11
72	B31	11
73	B41	11
74	B51	11
75	B61	11
76	B71	11
160	A11	60
176	A11	63
177	A12	63
178	A21	63
179	A22	63
77	A11	12
78	A12	12
79	A21	12
80	A22	12
81	A31	12
82	A32	12
83	A41	12
84	A42	12
85	B11	13
86	B21	13
87	B31	13
88	B41	13
89	B51	13
90	B61	13
91	B71	13
92	A11	14
93	A12	14
94	A21	14
95	A22	14
96	A31	14
97	A32	14
98	A41	14
99	A42	14
100	B11	15
101	B21	15
102	B31	15
103	B41	15
104	B51	15
105	B61	15
106	B71	15
180	A31	63
181	A32	63
182	A41	63
183	A42	63
184	B11	64
185	B21	64
186	B31	64
187	B41	64
188	B51	64
189	B61	64
190	B71	64
191	A11	65
192	A12	65
193	A13	65
194	A14	65
195	A21	65
196	A22	65
197	A23	65
198	A24	65
199	B11	66
200	B12	66
201	B13	66
202	B14	66
203	B15	66
204	B16	66
205	B17	66
206	c11	67
207	c12	67
208	c21	67
209	c22	67
210	A11	68
211	A12	68
212	A13	68
213	A21	68
214	A22	68
215	A23	68
\.


--
-- Name: cuadro_cod_cuadro_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cuadro_cod_cuadro_seq', 215, true);


--
-- Data for Name: cuadro_cultivo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cuadro_cultivo (cod_cuadro_cultivo, fch_ini, fch_fin, fk_cod_grupo_cuadro, fk_cod_cultivo, fk_cod_cuadro) FROM stdin;
\.


--
-- Name: cuadro_cultivo_cod_cuadro_cultivo_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cuadro_cultivo_cod_cuadro_cultivo_seq', 1, false);


--
-- Data for Name: cultivo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cultivo (cod_cultivo, cantidad_cultivo, produccion_esperada, variedad_cultivo, ciclo_unico, fk_cod_tipo_cultivo, fk_cod_estado_planificacion) FROM stdin;
\.


--
-- Name: cultivo_cod_cultivo_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cultivo_cod_cultivo_seq', 1, false);


--
-- Data for Name: estado_planificacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estado_planificacion (cod_estado_planificacion, nombre_estado_planificacion, is_activ) FROM stdin;
\.


--
-- Name: estado_planificacion_cod_estado_planificacion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.estado_planificacion_cod_estado_planificacion_seq', 1, false);


--
-- Data for Name: finca; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.finca (cod_finca, nombre_finca, superficie, is_activ, calle_finca, nro_finca, localidad_finca, provincia_finca) FROM stdin;
4	3 huertas qweqwe con usuario	12341	t	Alvarez	2024	Las heras	Mendoza
5	3 huertas qweqwe con usuario	12341	t	Alvarez	2024	Las heras	Mendoza
6	3 huertas qweqwe con usuario	12341	t	Alvarez	2024	Las heras	Mendoza
7	3 huertas qweqwe con usuario	12341	t	Alvarez	2024	Las heras	Mendoza
8	3 huertas qweqwe con usuario	12341	t	Alvarez	2024	Las heras	Mendoza
2	nueva finca ya no quiero mas	12341	t	Alvarez	2024	Las heras	Mendoza
3	lepraaa	12341	t	Alvarez	2024	Las heras	Mendoza
9	nueva finca 4 Huertas	12341	t	Alvarez	2024	Las heras	Mendoza
10	nueva finca 5 Huertas	12341	t	Alvarez	2024	Las heras	Mendoza
11	nueva finca de prueba	1234123	t	mazza	199	 Las Heras	Mendoza
\.


--
-- Name: finca_cod_finca_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.finca_cod_finca_seq', 11, true);


--
-- Data for Name: finca_usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.finca_usuario (fk_cod_finca, fk_cod_usuario, fch_ini, fch_fin, is_activ) FROM stdin;
9	2	2019-10-26 00:31:34.527149	\N	t
11	10	2019-10-30 19:03:22.347794	\N	t
\.


--
-- Data for Name: grupo_cuadro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.grupo_cuadro (cod_grupo_cuadro, fk_cod_parcela, fk_cod_planificacion) FROM stdin;
\.


--
-- Name: grupo_cuadro_cod_grupo_cuadro_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.grupo_cuadro_cod_grupo_cuadro_seq', 1, false);


--
-- Data for Name: grupo_planificacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.grupo_planificacion (cod_grupo_planificacion, fch_creacion, comentario_planificacion) FROM stdin;
\.


--
-- Name: grupo_planificacion_cod_grupo_planificacion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.grupo_planificacion_cod_grupo_planificacion_seq', 1, false);


--
-- Data for Name: img_activ_detalle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.img_activ_detalle (cod_img, descrip_img, img_base64, fk_cod_activ_detalle) FROM stdin;
\.


--
-- Name: img_activ_detalle_cod_img_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.img_activ_detalle_cod_img_seq', 22, true);


--
-- Data for Name: opcion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.opcion (cod_opcion, nombre_opcion, is_activ) FROM stdin;
1	semilla	t
2	plantin	t
3	fertilizante	t
4	abono	t
5	goteo	t
6	aspersion	t
\.


--
-- Name: opcion_cod_opcion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.opcion_cod_opcion_seq', 6, true);


--
-- Data for Name: parametro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.parametro (cod_parametro, nombre_parametro, is_activ, fk_cod_tipo_parametro, fk_cod_tipo_dato) FROM stdin;
1	dosis total recomendada	t	3	3
2	tipo de producto 	t	3	1
4	producto recomendado	t	3	1
3	fósforo dispobile (P%)	t	3	3
7	potasio disponible (K%)	t	3	3
6	nitrógeno disponible (N%)	t	3	3
8	cantidad total anual	t	3	3
9	hora recomendada de riego	t	3	5
10	frecuencia de riego	t	3	1
11	nro de muestras	t	4	2
12	profundidad de muestreo	t	4	3
13	proporción de limos	t	4	3
14	textura del suelo	t	4	1
15	temperatura	t	4	3
16	materia orgánica oxidable	t	4	3
17	nivel de P (fósforo)	t	4	3
18	tamaño de la muestra final	t	4	3
19	proporción de arcilla	t	4	3
20	proporción de arena	t	4	3
21	humedad	t	4	3
22	pH	t	4	3
23	conductividad eléctrica	t	4	3
24	fuente de riego	t	4	1
25	calcio mg/l	t	4	3
26	sodio mg/l	t	4	3
27	bicarbonatos mg/l	t	4	3
28	sulfato mg/l	t	4	3
29	nitrato - nitrógeno	t	4	3
30	fosfato - fósforo	t	4	3
31	boro	t	4	3
32	temperatura del agua	t	4	3
33	temperatura del aire	t	4	3
35	sales totales g/l	t	4	3
36	magnesiomg/l	t	4	3
37	carbonatos mg/l	t	4	3
38	cloro mg/l	t	4	3
39	dureza total	t	4	3
40	amonio - nitrógeno	t	4	3
41	potasio	t	4	3
42	acidez	t	4	3
43	relación de absorción de sodio	t	4	3
44	humedad del aire	t	4	3
34	tipo de riego	t	4	6
5	ámbito	t	3	6
45	tipo de riego	t	1	6
46	fuente de riego	t	1	1
47	caudal M3/h	t	1	3
48	total M3/h	t	1	3
49	pH	t	1	3
50	tipo de siembra	t	1	6
51	cultivo y variedad a plantar	t	1	1
52	marco de plantación (distancia entre las plantas)	t	1	3
53	fecha estimada de recolección	t	1	7
54	cantidad de plantas por m2	t	1	2
55	profundidad (cm)	t	1	3
56	fertilizante/Abono (nombre)	t	1	1
57	marca	t	1	1
58	dosis	t	1	3
59	unidades (Ámbito) unidad de medida de la dosis	t	1	3
60	dosis	t	1	2
61	actividad	t	1	6
62	profundidad (Cm)	t	1	3
63	velocidad (Km/h)	t	1	3
64	es objeto de asesoramiento	t	1	6
65	nro de recomendación	t	1	2
66	enfermedad o Plaga	t	1	6
67	producto	t	1	1
68	marca	t	1	1
69	dosis	t	1	3
70	plazo de seguridad	t	1	5
71	producción cosechada (cantidad)	t	1	3
72	finalización de cultivo	t	1	6
73	posible enfermedad o Plaga	t	1	6
74	nombre de catástrofe	t	1	1
75	equipo fertirrigación	t	1	1
76	nombre fertilizante	t	1	1
77	sulfato de potasio	t	1	3
78	sulfato amónico	t	1	3
79	sulfato magnesio	t	1	3
80	fosfato M potasio	t	1	3
81	tiempo de riego	t	1	5
82	conductividad eléctrica	t	1	3
83	plazo de seguridad	t	2	2
84	dosis recomendada	t	2	3
85	cantidad total recomendada	t	2	3
86	plazo máximo de aplicación	t	2	7
87	plazo mínimo de reentrada	t	2	7
88	compuesto	t	2	1
89	producto recomendado	t	2	1
90	enfermedad o plaga	t	2	6
91	nombre de catástrofe	t	2	1
\.


--
-- Name: parametro_cod_parametro_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.parametro_cod_parametro_seq', 91, true);


--
-- Data for Name: parametro_opcion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.parametro_opcion (is_activ, fk_cod_parametro, fk_cod_opcion) FROM stdin;
t	50	1
t	50	2
\.


--
-- Data for Name: parcela; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.parcela (cod_parcela, nombre_parcela, superficie_parcela, filas, columnas, fk_cod_finca) FROM stdin;
6	A	123.3	4	2	4
7	B	12097.299999999999	7	1	4
8	A	123.3	4	2	5
9	B	12097.299999999999	7	1	5
10	A	123.3	4	2	6
11	B	12097.299999999999	7	1	6
12	A	123.3	4	2	7
13	B	12097.299999999999	7	1	7
14	A	123.3	4	2	8
15	B	12097.299999999999	7	1	8
60	A	123.3	1	1	3
63	A	123.3	4	2	10
64	B	12097.299999999999	7	1	10
65	A	123.3	2	4	9
66	B	12097.299999999999	1	7	9
67	c	22	2	2	9
68	A	123	2	3	11
\.


--
-- Name: parcela_cod_parcela_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.parcela_cod_parcela_seq', 68, true);


--
-- Data for Name: permiso; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.permiso (cod_permiso, nombre_permiso, is_activ) FROM stdin;
\.


--
-- Name: permiso_cod_permiso_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.permiso_cod_permiso_seq', 1, false);


--
-- Data for Name: plan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.plan (cod_plan, fch_plan, fk_cod_tipo_plan, fk_cod_usuario, fk_cod_grupo_cuadro) FROM stdin;
3	2019-10-27 23:58:54	1	1	\N
4	2019-10-27 23:58:54	2	1	\N
\.


--
-- Name: plan_cod_plan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.plan_cod_plan_seq', 4, true);


--
-- Data for Name: plan_param; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.plan_param (fk_cod_plan, fk_cod_parametro, valor) FROM stdin;
\.


--
-- Data for Name: planificacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.planificacion (cod_planificacion, fch_planificacion, comentario_planificacion, fk_cod_tipo_planificacion, fk_cod_estado_planificacion, fk_cod_finca, fk_cod_grupo_planificacion, fk_cod_usuario) FROM stdin;
\.


--
-- Name: planificacion_cod_planificacion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.planificacion_cod_planificacion_seq', 1, false);


--
-- Data for Name: recom_detalle_param; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recom_detalle_param (fk_cod_recom_detalle, fk_cod_parametro, valor) FROM stdin;
\.


--
-- Data for Name: recomendacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recomendacion (cod_recomendacion, nombre_recomendacion, is_activ) FROM stdin;
1	recomendación fitosanitaria	t
2	recomendación catástrofe	t
\.


--
-- Name: recomendacion_cod_recomendacion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recomendacion_cod_recomendacion_seq', 2, true);


--
-- Data for Name: recomendacion_detalle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recomendacion_detalle (cod_recom_detalle, fch_recom_detalle, observacion, is_eliminado, is_aplicada, fk_cod_recomendacion, fk_cod_usuario) FROM stdin;
9	2019-10-13 19:35:54	Se aconseja que todo se deje como esta ING AGRONOMO	f	f	1	1
25	2019-10-13 19:35:54	Se aconseja que todo se deje como esta ING AGRONOMO	f	f	1	1
26	2019-10-13 19:35:54	Se aconseja que todo se deje como esta ING AGRONOMO	f	f	1	1
27	2019-10-13 19:35:54	Se aconseja que todo se deje como esta ING AGRONOMO	f	f	1	3
28	2019-10-13 19:35:54	Se aconseja que todo se deje como esta ING AGRONOMO	f	f	1	3
\.


--
-- Name: recomendacion_detalle_cod_recom_detalle_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recomendacion_detalle_cod_recom_detalle_seq', 28, true);


--
-- Data for Name: recomendacion_parametro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recomendacion_parametro (is_activ, fk_cod_parametro, fk_cod_recomendacion) FROM stdin;
t	83	1
t	84	1
t	85	1
t	86	1
t	87	1
t	88	1
t	89	1
t	90	1
t	91	2
\.


--
-- Data for Name: recurso; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recurso (cod_recurso, nombre_recurso, is_activ, fk_tipo_recurso) FROM stdin;
\.


--
-- Name: recurso_cod_recurso_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recurso_cod_recurso_seq', 1, false);


--
-- Data for Name: rol; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rol (cod_rol, nombre_rol, is_activ) FROM stdin;
1	administrador	t
2	encargadofinca	t
3	ingeniero	t
4	supervisor	t
\.


--
-- Name: rol_cod_rol_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.rol_cod_rol_seq', 3, true);


--
-- Data for Name: sessionUser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."sessionUser" ("cod_sessionUser", "cod_public_sessionUser", usuario, "token_sessionUser", rol_usuario) FROM stdin;
5	6eafa182-8f5e-485b-8b68-bca1d689ae1b	pepito	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f69634756776158527649697769636d3973496a6f696157356e5a5735705a584a7649697769616e5270496a6f695a4755334d545532595759744e57497a4f5330304d47466a4c5467324f5451744d5451794e6d49305a5752694d7a5579496977695a586877496a6f784e5463784f4441324d546b7766512e35524873304c386b4b4f7861686c71384d47306656614b584e694f6f4871754259516f5450654d63364e55	encargadofinca
4	ad2a4ea8-1def-4616-9473-af7efb06ba7a	prueba	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f69616d466d61534973496e4a7662434936496e4e3163475679646d6c7a623349694c434a7164476b694f694a69596d4a6a4f544e6b4d4330354d4459324c5451794f4749744f57597a4e79316a4d44686c4e325668596a426a4d6a416966512e5f492d7157346c6e6448526d714856666a335a737143756b4644334f6b763559455f58504f774d35505367	encargadofinca
6	7d9f914e-cf49-485e-9bc8-22cb0dec1ccc	nedamo	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f69626d566b5957317649697769636d3973496a6f695a57356a59584a6e595752765a6d6c75593245694c434a7164476b694f694931593252684d54526a5a6930795a6d59794c54526d5a44457459544a695a5330335a546c6c5a546c69596d49344d6d4d694c434a6c654841694f6a45314e7a457a4e5459304e6a64392e5857675463595633387a6730384a5832334d32726654586b4a4b417930364a6461554f445830357536566b	encargadofinca
1	1	admin	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f6959575274615734694c434a79623277694f694a685a473170626d6c7a64484a685a47397949697769616e5270496a6f694e544d314e4755795a4467744e3259354d7930304d6a497a4c574a6a5a5445744e6a45324d6d55334f57466b4d546779496e302e7a5674477941495734434736753367444741517a7a6c612d31557874784a4a7476374475496f4238334a77	administrador
2	5102c661-d783-4dfb-a32e-d5f4f1fc319e	melisa	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f696257567361584e6849697769636d3973496a6f695a57356a59584a6e595752765a6d6c75593245694c434a7164476b694f694a69595463334f44526d4d7930774d7a51304c54526c596d4d745954457a4e79307a5a5746695954426a4e446330596a496966512e6e53574b52474a554f38702d7478486f354a6a693779746f5674616c42717248364a4a5767425868666d59	encargadofinca
7	1a225bf5-8d73-47ba-b95c-b3a51477f0da	otra	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f696233527959534973496e4a7662434936496d5675593246795a32466b62325a70626d4e6849697769616e5270496a6f6959325a695a6a686c4e6a6b744e5745775a5330304f54426d4c546c6a4e4445744d47466b4d54526d596d5a6b4d574535496e302e3743754a4f77386275645256555a657047484e42575f657163346a5a38442d6b6b33354d4e6c4b59574759	encargadofinca
3	f6e8acbb-fec8-4c9d-ae7f-4402e94b4a7e	jafi	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f695a6e4a68626d4e7649697769636d3973496a6f696157356e5a5735705a584a7649697769616e5270496a6f69597a67324f4451784e446374595756694d4330304f574d324c5467314f546774595445335a446b7a4e7a566a4e446c69496e302e486d5a6b6439346567796c354e446e303844567a6d7577746c32486e70306a725336343252596357666b45	administrador
\.


--
-- Name: sessionUser_cod_sessionUser_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."sessionUser_cod_sessionUser_seq"', 7, true);


--
-- Data for Name: tipo_analisis; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_analisis (cod_tipo_analisis, nombre_tipo_analisis, is_activ) FROM stdin;
1	análisis de agua	t
2	análisis de suelo	t
\.


--
-- Name: tipo_analisis_cod_tipo_analisis_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_analisis_cod_tipo_analisis_seq', 14, true);


--
-- Data for Name: tipo_analisis_param; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_analisis_param (is_activ, fk_cod_parametro, fk_cod_tipo_analisis) FROM stdin;
t	11	2
t	12	2
t	13	2
t	14	2
t	15	2
t	16	2
t	17	2
t	18	2
t	19	2
t	20	2
t	21	2
t	22	2
t	23	2
t	23	1
t	24	1
t	25	1
t	26	1
t	27	1
t	28	1
t	29	1
t	30	1
t	31	1
t	32	1
t	33	1
t	34	1
t	35	1
t	36	1
t	37	1
t	38	1
t	39	1
t	40	1
t	41	1
t	42	1
t	43	1
t	44	1
\.


--
-- Data for Name: tipo_cultivo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_cultivo (cod_tipo_cultivo, nombre_tipo_cultivo, is_activ) FROM stdin;
\.


--
-- Name: tipo_cultivo_cod_tipo_cultivo_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_cultivo_cod_tipo_cultivo_seq', 1, false);


--
-- Data for Name: tipo_dato; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_dato (cod_tipo_dato, nombre_tipo_dato, is_activ) FROM stdin;
1	string	t
2	int	t
3	double	t
4	datetime	t
5	time	t
6	combo	t
7	date	t
\.


--
-- Name: tipo_dato_cod_tipo_dato_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_dato_cod_tipo_dato_seq', 7, true);


--
-- Data for Name: tipo_parametro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_parametro (cod_tipo_parametro, nombre_tipo_parametro, is_activ) FROM stdin;
1	actividad	t
2	recomendacion	t
3	plan	t
4	analisis	t
\.


--
-- Name: tipo_parametro_cod_tipo_parametro_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_parametro_cod_tipo_parametro_seq', 4, true);


--
-- Data for Name: tipo_plan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_plan (cod_tipo_plan, nombre_tipo_plan, is_activ) FROM stdin;
1	plan de riego	t
2	plan de fertilización	t
\.


--
-- Name: tipo_plan_cod_tipo_plan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_plan_cod_tipo_plan_seq', 1, false);


--
-- Data for Name: tipo_plan_param; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_plan_param (is_activ, fk_cod_parametro, fk_cod_tipo_plan) FROM stdin;
t	1	2
t	2	2
t	3	2
t	4	2
t	5	2
t	6	2
t	7	2
t	8	1
t	9	1
t	5	1
t	10	1
\.


--
-- Data for Name: tipo_planificacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_planificacion (cod_tipo_planificacion, nombre_tipo_planificacion, is_activ) FROM stdin;
1	inicial	t
2	supervisada	t
3	final	t
\.


--
-- Name: tipo_planificacion_cod_tipo_planificacion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_planificacion_cod_tipo_planificacion_seq', 3, true);


--
-- Data for Name: tipo_recurso; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_recurso (cod_tipo_recurso, nombre_tipo_recurso, is_activ) FROM stdin;
\.


--
-- Name: tipo_recurso_cod_tipo_recurso_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_recurso_cod_tipo_recurso_seq', 1, false);


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (cod_usuario_private, cod_usuario, usuario, nombre_usuario, apellido_usuario, email_usuario, contrasenia_usuario, "fchCrea_usuario", random_contrasenia_usuario, is_recuperar, fk_cod_rol, is_activ) FROM stdin;
1	1	admin	admin	admin	admin@gmail.com	1234567	2019-10-12	\N	\N	1	t
2	5102c661-d783-4dfb-a32e-d5f4f1fc319e	melisa	melisa	sosa	meli@gmail.com	1234567	2019-10-11	\N	\N	2	t
3	f6e8acbb-fec8-4c9d-ae7f-4402e94b4a7e	franco	franco	sanchez	csir@gmail.com	1234567	2019-10-15	\N	\N	3	t
4	ad2a4ea8-1def-4616-9473-af7efb06ba7a	jafi	javier	bravin	prueba@gmil.com	1234567	2019-10-15	\N	\N	4	f
9	1278eeab-b303-47a0-b914-d2a9f5e1618b	franco2	fran	san	franco@gmail.com	12345678	2019-10-30	\N	\N	1	t
10	1a225bf5-8d73-47ba-b95c-b3a51477f0da	otra	otra	otra	otra@gmail.com	12345678	2019-10-30	\N	\N	2	t
\.


--
-- Name: usuario_cod_usuario_private_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_cod_usuario_private_seq', 10, true);


--
-- Name: activ_detalle_param activ_detalle_param_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activ_detalle_param
    ADD CONSTRAINT activ_detalle_param_pkey PRIMARY KEY (fk_cod_activ_detalle, fk_cod_parametro);


--
-- Name: actividad_detalle actividad_detalle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad_detalle
    ADD CONSTRAINT actividad_detalle_pkey PRIMARY KEY (cod_activ_detalle);


--
-- Name: actividad actividad_nombre_actividad_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad
    ADD CONSTRAINT actividad_nombre_actividad_key UNIQUE (nombre_actividad);


--
-- Name: actividad_parametro actividad_parametro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad_parametro
    ADD CONSTRAINT actividad_parametro_pkey PRIMARY KEY (fk_cod_parametro, fk_cod_actividad);


--
-- Name: actividad actividad_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad
    ADD CONSTRAINT actividad_pkey PRIMARY KEY (cod_actividad);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: analisis_param analisis_param_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.analisis_param
    ADD CONSTRAINT analisis_param_pkey PRIMARY KEY (fk_cod_analisis, fk_cod_parametro);


--
-- Name: analisis analisis_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.analisis
    ADD CONSTRAINT analisis_pkey PRIMARY KEY (cod_analisis);


--
-- Name: cuadro_cultivo cuadro_cultivo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cuadro_cultivo
    ADD CONSTRAINT cuadro_cultivo_pkey PRIMARY KEY (cod_cuadro_cultivo);


--
-- Name: cuadro cuadro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cuadro
    ADD CONSTRAINT cuadro_pkey PRIMARY KEY (cod_cuadro);


--
-- Name: cultivo cultivo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cultivo
    ADD CONSTRAINT cultivo_pkey PRIMARY KEY (cod_cultivo);


--
-- Name: estado_planificacion estado_planificacion_nombre_estado_planificacion_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estado_planificacion
    ADD CONSTRAINT estado_planificacion_nombre_estado_planificacion_key UNIQUE (nombre_estado_planificacion);


--
-- Name: estado_planificacion estado_planificacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estado_planificacion
    ADD CONSTRAINT estado_planificacion_pkey PRIMARY KEY (cod_estado_planificacion);


--
-- Name: finca finca_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.finca
    ADD CONSTRAINT finca_pkey PRIMARY KEY (cod_finca);


--
-- Name: finca_usuario finca_usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.finca_usuario
    ADD CONSTRAINT finca_usuario_pkey PRIMARY KEY (fk_cod_finca, fk_cod_usuario);


--
-- Name: grupo_cuadro grupo_cuadro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_cuadro
    ADD CONSTRAINT grupo_cuadro_pkey PRIMARY KEY (cod_grupo_cuadro);


--
-- Name: grupo_planificacion grupo_planificacion_comentario_planificacion_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_planificacion
    ADD CONSTRAINT grupo_planificacion_comentario_planificacion_key UNIQUE (comentario_planificacion);


--
-- Name: grupo_planificacion grupo_planificacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_planificacion
    ADD CONSTRAINT grupo_planificacion_pkey PRIMARY KEY (cod_grupo_planificacion);


--
-- Name: img_activ_detalle img_activ_detalle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.img_activ_detalle
    ADD CONSTRAINT img_activ_detalle_pkey PRIMARY KEY (cod_img);


--
-- Name: opcion opcion_nombre_opcion_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opcion
    ADD CONSTRAINT opcion_nombre_opcion_key UNIQUE (nombre_opcion);


--
-- Name: opcion opcion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opcion
    ADD CONSTRAINT opcion_pkey PRIMARY KEY (cod_opcion);


--
-- Name: parametro_opcion parametro_opcion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parametro_opcion
    ADD CONSTRAINT parametro_opcion_pkey PRIMARY KEY (fk_cod_parametro, fk_cod_opcion);


--
-- Name: parametro parametro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parametro
    ADD CONSTRAINT parametro_pkey PRIMARY KEY (cod_parametro);


--
-- Name: parcela parcela_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parcela
    ADD CONSTRAINT parcela_pkey PRIMARY KEY (cod_parcela);


--
-- Name: permiso permiso_nombre_permiso_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permiso
    ADD CONSTRAINT permiso_nombre_permiso_key UNIQUE (nombre_permiso);


--
-- Name: permiso permiso_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permiso
    ADD CONSTRAINT permiso_pkey PRIMARY KEY (cod_permiso);


--
-- Name: plan_param plan_param_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plan_param
    ADD CONSTRAINT plan_param_pkey PRIMARY KEY (fk_cod_plan, fk_cod_parametro);


--
-- Name: plan plan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plan
    ADD CONSTRAINT plan_pkey PRIMARY KEY (cod_plan);


--
-- Name: planificacion planificacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planificacion
    ADD CONSTRAINT planificacion_pkey PRIMARY KEY (cod_planificacion);


--
-- Name: recom_detalle_param recom_detalle_param_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recom_detalle_param
    ADD CONSTRAINT recom_detalle_param_pkey PRIMARY KEY (fk_cod_recom_detalle, fk_cod_parametro);


--
-- Name: recomendacion_detalle recomendacion_detalle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion_detalle
    ADD CONSTRAINT recomendacion_detalle_pkey PRIMARY KEY (cod_recom_detalle);


--
-- Name: recomendacion recomendacion_nombre_recomendacion_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion
    ADD CONSTRAINT recomendacion_nombre_recomendacion_key UNIQUE (nombre_recomendacion);


--
-- Name: recomendacion_parametro recomendacion_parametro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion_parametro
    ADD CONSTRAINT recomendacion_parametro_pkey PRIMARY KEY (fk_cod_parametro, fk_cod_recomendacion);


--
-- Name: recomendacion recomendacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion
    ADD CONSTRAINT recomendacion_pkey PRIMARY KEY (cod_recomendacion);


--
-- Name: recurso recurso_nombre_recurso_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recurso
    ADD CONSTRAINT recurso_nombre_recurso_key UNIQUE (nombre_recurso);


--
-- Name: recurso recurso_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recurso
    ADD CONSTRAINT recurso_pkey PRIMARY KEY (cod_recurso);


--
-- Name: rol rol_nombre_rol_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rol
    ADD CONSTRAINT rol_nombre_rol_key UNIQUE (nombre_rol);


--
-- Name: rol rol_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rol
    ADD CONSTRAINT rol_pkey PRIMARY KEY (cod_rol);


--
-- Name: sessionUser sessionUser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sessionUser"
    ADD CONSTRAINT "sessionUser_pkey" PRIMARY KEY ("cod_sessionUser");


--
-- Name: sessionUser sessionUser_usuario_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."sessionUser"
    ADD CONSTRAINT "sessionUser_usuario_key" UNIQUE (usuario);


--
-- Name: tipo_analisis tipo_analisis_nombre_tipo_analisis_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_analisis
    ADD CONSTRAINT tipo_analisis_nombre_tipo_analisis_key UNIQUE (nombre_tipo_analisis);


--
-- Name: tipo_analisis_param tipo_analisis_param_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_analisis_param
    ADD CONSTRAINT tipo_analisis_param_pkey PRIMARY KEY (fk_cod_parametro, fk_cod_tipo_analisis);


--
-- Name: tipo_analisis tipo_analisis_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_analisis
    ADD CONSTRAINT tipo_analisis_pkey PRIMARY KEY (cod_tipo_analisis);


--
-- Name: tipo_cultivo tipo_cultivo_nombre_tipo_cultivo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_cultivo
    ADD CONSTRAINT tipo_cultivo_nombre_tipo_cultivo_key UNIQUE (nombre_tipo_cultivo);


--
-- Name: tipo_cultivo tipo_cultivo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_cultivo
    ADD CONSTRAINT tipo_cultivo_pkey PRIMARY KEY (cod_tipo_cultivo);


--
-- Name: tipo_dato tipo_dato_nombre_tipo_dato_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_dato
    ADD CONSTRAINT tipo_dato_nombre_tipo_dato_key UNIQUE (nombre_tipo_dato);


--
-- Name: tipo_dato tipo_dato_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_dato
    ADD CONSTRAINT tipo_dato_pkey PRIMARY KEY (cod_tipo_dato);


--
-- Name: tipo_parametro tipo_parametro_nombre_tipo_parametro_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_parametro
    ADD CONSTRAINT tipo_parametro_nombre_tipo_parametro_key UNIQUE (nombre_tipo_parametro);


--
-- Name: tipo_parametro tipo_parametro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_parametro
    ADD CONSTRAINT tipo_parametro_pkey PRIMARY KEY (cod_tipo_parametro);


--
-- Name: tipo_plan tipo_plan_nombre_tipo_plan_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_plan
    ADD CONSTRAINT tipo_plan_nombre_tipo_plan_key UNIQUE (nombre_tipo_plan);


--
-- Name: tipo_plan_param tipo_plan_param_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_plan_param
    ADD CONSTRAINT tipo_plan_param_pkey PRIMARY KEY (fk_cod_parametro, fk_cod_tipo_plan);


--
-- Name: tipo_plan tipo_plan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_plan
    ADD CONSTRAINT tipo_plan_pkey PRIMARY KEY (cod_tipo_plan);


--
-- Name: tipo_planificacion tipo_planificacion_nombre_tipo_planificacion_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_planificacion
    ADD CONSTRAINT tipo_planificacion_nombre_tipo_planificacion_key UNIQUE (nombre_tipo_planificacion);


--
-- Name: tipo_planificacion tipo_planificacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_planificacion
    ADD CONSTRAINT tipo_planificacion_pkey PRIMARY KEY (cod_tipo_planificacion);


--
-- Name: tipo_recurso tipo_recurso_nombre_tipo_recurso_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_recurso
    ADD CONSTRAINT tipo_recurso_nombre_tipo_recurso_key UNIQUE (nombre_tipo_recurso);


--
-- Name: tipo_recurso tipo_recurso_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_recurso
    ADD CONSTRAINT tipo_recurso_pkey PRIMARY KEY (cod_tipo_recurso);


--
-- Name: usuario usuario_email_usuario_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_email_usuario_key UNIQUE (email_usuario);


--
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (cod_usuario_private);


--
-- Name: ix_actividad_cod_actividad; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_actividad_cod_actividad ON public.actividad USING btree (cod_actividad);


--
-- Name: ix_actividad_detalle_cod_activ_detalle; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_actividad_detalle_cod_activ_detalle ON public.actividad_detalle USING btree (cod_activ_detalle);


--
-- Name: ix_actividad_detalle_fch_activ_detalle; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_actividad_detalle_fch_activ_detalle ON public.actividad_detalle USING btree (fch_activ_detalle);


--
-- Name: ix_actividad_detalle_fk_cod_recom_detalle; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_actividad_detalle_fk_cod_recom_detalle ON public.actividad_detalle USING btree (fk_cod_recom_detalle);


--
-- Name: ix_actividad_parametro_fk_cod_actividad; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_actividad_parametro_fk_cod_actividad ON public.actividad_parametro USING btree (fk_cod_actividad);


--
-- Name: ix_actividad_parametro_fk_cod_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_actividad_parametro_fk_cod_parametro ON public.actividad_parametro USING btree (fk_cod_parametro);


--
-- Name: ix_analisis_cod_analisis; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_analisis_cod_analisis ON public.analisis USING btree (cod_analisis);


--
-- Name: ix_analisis_fch_analisis; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_analisis_fch_analisis ON public.analisis USING btree (fch_analisis);


--
-- Name: ix_cuadro_cod_cuadro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cuadro_cod_cuadro ON public.cuadro USING btree (cod_cuadro);


--
-- Name: ix_cuadro_cultivo_cod_cuadro_cultivo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cuadro_cultivo_cod_cuadro_cultivo ON public.cuadro_cultivo USING btree (cod_cuadro_cultivo);


--
-- Name: ix_cuadro_cultivo_fch_fin; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cuadro_cultivo_fch_fin ON public.cuadro_cultivo USING btree (fch_fin);


--
-- Name: ix_cuadro_cultivo_fch_ini; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cuadro_cultivo_fch_ini ON public.cuadro_cultivo USING btree (fch_ini);


--
-- Name: ix_cuadro_cultivo_fk_cod_cuadro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cuadro_cultivo_fk_cod_cuadro ON public.cuadro_cultivo USING btree (fk_cod_cuadro);


--
-- Name: ix_cuadro_cultivo_fk_cod_cultivo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cuadro_cultivo_fk_cod_cultivo ON public.cuadro_cultivo USING btree (fk_cod_cultivo);


--
-- Name: ix_cuadro_cultivo_fk_cod_grupo_cuadro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cuadro_cultivo_fk_cod_grupo_cuadro ON public.cuadro_cultivo USING btree (fk_cod_grupo_cuadro);


--
-- Name: ix_cultivo_cod_cultivo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cultivo_cod_cultivo ON public.cultivo USING btree (cod_cultivo);


--
-- Name: ix_cultivo_fk_cod_estado_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cultivo_fk_cod_estado_planificacion ON public.cultivo USING btree (fk_cod_estado_planificacion);


--
-- Name: ix_cultivo_fk_cod_tipo_cultivo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cultivo_fk_cod_tipo_cultivo ON public.cultivo USING btree (fk_cod_tipo_cultivo);


--
-- Name: ix_estado_planificacion_cod_estado_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_estado_planificacion_cod_estado_planificacion ON public.estado_planificacion USING btree (cod_estado_planificacion);


--
-- Name: ix_finca_cod_finca; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_finca_cod_finca ON public.finca USING btree (cod_finca);


--
-- Name: ix_grupo_cuadro_cod_grupo_cuadro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_grupo_cuadro_cod_grupo_cuadro ON public.grupo_cuadro USING btree (cod_grupo_cuadro);


--
-- Name: ix_grupo_cuadro_fk_cod_parcela; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_grupo_cuadro_fk_cod_parcela ON public.grupo_cuadro USING btree (fk_cod_parcela);


--
-- Name: ix_grupo_cuadro_fk_cod_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_grupo_cuadro_fk_cod_planificacion ON public.grupo_cuadro USING btree (fk_cod_planificacion);


--
-- Name: ix_grupo_planificacion_cod_grupo_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_grupo_planificacion_cod_grupo_planificacion ON public.grupo_planificacion USING btree (cod_grupo_planificacion);


--
-- Name: ix_grupo_planificacion_fch_creacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_grupo_planificacion_fch_creacion ON public.grupo_planificacion USING btree (fch_creacion);


--
-- Name: ix_img_activ_detalle_cod_img; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_img_activ_detalle_cod_img ON public.img_activ_detalle USING btree (cod_img);


--
-- Name: ix_opcion_cod_opcion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_opcion_cod_opcion ON public.opcion USING btree (cod_opcion);


--
-- Name: ix_parametro_cod_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_parametro_cod_parametro ON public.parametro USING btree (cod_parametro);


--
-- Name: ix_parametro_fk_cod_tipo_dato; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_parametro_fk_cod_tipo_dato ON public.parametro USING btree (fk_cod_tipo_dato);


--
-- Name: ix_parametro_fk_cod_tipo_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_parametro_fk_cod_tipo_parametro ON public.parametro USING btree (fk_cod_tipo_parametro);


--
-- Name: ix_parametro_opcion_fk_cod_opcion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_parametro_opcion_fk_cod_opcion ON public.parametro_opcion USING btree (fk_cod_opcion);


--
-- Name: ix_parametro_opcion_fk_cod_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_parametro_opcion_fk_cod_parametro ON public.parametro_opcion USING btree (fk_cod_parametro);


--
-- Name: ix_parcela_cod_parcela; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_parcela_cod_parcela ON public.parcela USING btree (cod_parcela);


--
-- Name: ix_permiso_cod_permiso; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_permiso_cod_permiso ON public.permiso USING btree (cod_permiso);


--
-- Name: ix_plan_cod_plan; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_plan_cod_plan ON public.plan USING btree (cod_plan);


--
-- Name: ix_plan_fch_plan; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_plan_fch_plan ON public.plan USING btree (fch_plan);


--
-- Name: ix_planificacion_cod_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_planificacion_cod_planificacion ON public.planificacion USING btree (cod_planificacion);


--
-- Name: ix_planificacion_fch_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_planificacion_fch_planificacion ON public.planificacion USING btree (fch_planificacion);


--
-- Name: ix_planificacion_fk_cod_estado_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_planificacion_fk_cod_estado_planificacion ON public.planificacion USING btree (fk_cod_estado_planificacion);


--
-- Name: ix_planificacion_fk_cod_finca; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_planificacion_fk_cod_finca ON public.planificacion USING btree (fk_cod_finca);


--
-- Name: ix_planificacion_fk_cod_grupo_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_planificacion_fk_cod_grupo_planificacion ON public.planificacion USING btree (fk_cod_grupo_planificacion);


--
-- Name: ix_planificacion_fk_cod_tipo_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_planificacion_fk_cod_tipo_planificacion ON public.planificacion USING btree (fk_cod_tipo_planificacion);


--
-- Name: ix_recomendacion_cod_recomendacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_recomendacion_cod_recomendacion ON public.recomendacion USING btree (cod_recomendacion);


--
-- Name: ix_recomendacion_detalle_cod_recom_detalle; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_recomendacion_detalle_cod_recom_detalle ON public.recomendacion_detalle USING btree (cod_recom_detalle);


--
-- Name: ix_recomendacion_detalle_fch_recom_detalle; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_recomendacion_detalle_fch_recom_detalle ON public.recomendacion_detalle USING btree (fch_recom_detalle);


--
-- Name: ix_recomendacion_parametro_fk_cod_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_recomendacion_parametro_fk_cod_parametro ON public.recomendacion_parametro USING btree (fk_cod_parametro);


--
-- Name: ix_recomendacion_parametro_fk_cod_recomendacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_recomendacion_parametro_fk_cod_recomendacion ON public.recomendacion_parametro USING btree (fk_cod_recomendacion);


--
-- Name: ix_recurso_cod_recurso; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_recurso_cod_recurso ON public.recurso USING btree (cod_recurso);


--
-- Name: ix_recurso_fk_tipo_recurso; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_recurso_fk_tipo_recurso ON public.recurso USING btree (fk_tipo_recurso);


--
-- Name: ix_rol_cod_rol; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_rol_cod_rol ON public.rol USING btree (cod_rol);


--
-- Name: ix_sessionUser_cod_sessionUser; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "ix_sessionUser_cod_sessionUser" ON public."sessionUser" USING btree ("cod_sessionUser");


--
-- Name: ix_tipo_analisis_cod_tipo_analisis; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_analisis_cod_tipo_analisis ON public.tipo_analisis USING btree (cod_tipo_analisis);


--
-- Name: ix_tipo_analisis_param_fk_cod_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_analisis_param_fk_cod_parametro ON public.tipo_analisis_param USING btree (fk_cod_parametro);


--
-- Name: ix_tipo_analisis_param_fk_cod_tipo_analisis; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_analisis_param_fk_cod_tipo_analisis ON public.tipo_analisis_param USING btree (fk_cod_tipo_analisis);


--
-- Name: ix_tipo_cultivo_cod_tipo_cultivo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_cultivo_cod_tipo_cultivo ON public.tipo_cultivo USING btree (cod_tipo_cultivo);


--
-- Name: ix_tipo_dato_cod_tipo_dato; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_dato_cod_tipo_dato ON public.tipo_dato USING btree (cod_tipo_dato);


--
-- Name: ix_tipo_parametro_cod_tipo_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_parametro_cod_tipo_parametro ON public.tipo_parametro USING btree (cod_tipo_parametro);


--
-- Name: ix_tipo_plan_cod_tipo_plan; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_plan_cod_tipo_plan ON public.tipo_plan USING btree (cod_tipo_plan);


--
-- Name: ix_tipo_plan_param_fk_cod_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_plan_param_fk_cod_parametro ON public.tipo_plan_param USING btree (fk_cod_parametro);


--
-- Name: ix_tipo_plan_param_fk_cod_tipo_plan; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_plan_param_fk_cod_tipo_plan ON public.tipo_plan_param USING btree (fk_cod_tipo_plan);


--
-- Name: ix_tipo_planificacion_cod_tipo_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_planificacion_cod_tipo_planificacion ON public.tipo_planificacion USING btree (cod_tipo_planificacion);


--
-- Name: ix_tipo_recurso_cod_tipo_recurso; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_recurso_cod_tipo_recurso ON public.tipo_recurso USING btree (cod_tipo_recurso);


--
-- Name: ix_usuario_cod_usuario_private; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_usuario_cod_usuario_private ON public.usuario USING btree (cod_usuario_private);


--
-- Name: ix_usuario_fk_cod_rol; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_usuario_fk_cod_rol ON public.usuario USING btree (fk_cod_rol);


--
-- Name: ix_usuario_usuario; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_usuario_usuario ON public.usuario USING btree (usuario);


--
-- Name: activ_detalle_param activ_detalle_param_fk_cod_activ_detalle_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activ_detalle_param
    ADD CONSTRAINT activ_detalle_param_fk_cod_activ_detalle_fkey FOREIGN KEY (fk_cod_activ_detalle) REFERENCES public.actividad_detalle(cod_activ_detalle);


--
-- Name: activ_detalle_param activ_detalle_param_fk_cod_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activ_detalle_param
    ADD CONSTRAINT activ_detalle_param_fk_cod_parametro_fkey FOREIGN KEY (fk_cod_parametro) REFERENCES public.parametro(cod_parametro);


--
-- Name: actividad_detalle actividad_detalle_fk_cod_actividad_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad_detalle
    ADD CONSTRAINT actividad_detalle_fk_cod_actividad_fkey FOREIGN KEY (fk_cod_actividad) REFERENCES public.actividad(cod_actividad);


--
-- Name: actividad_detalle actividad_detalle_fk_cod_recom_detalle_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad_detalle
    ADD CONSTRAINT actividad_detalle_fk_cod_recom_detalle_fkey FOREIGN KEY (fk_cod_recom_detalle) REFERENCES public.recomendacion_detalle(cod_recom_detalle);


--
-- Name: actividad_detalle actividad_detalle_fk_cod_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad_detalle
    ADD CONSTRAINT actividad_detalle_fk_cod_usuario_fkey FOREIGN KEY (fk_cod_usuario) REFERENCES public.usuario(cod_usuario_private);


--
-- Name: actividad_parametro actividad_parametro_fk_cod_actividad_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad_parametro
    ADD CONSTRAINT actividad_parametro_fk_cod_actividad_fkey FOREIGN KEY (fk_cod_actividad) REFERENCES public.actividad(cod_actividad);


--
-- Name: actividad_parametro actividad_parametro_fk_cod_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actividad_parametro
    ADD CONSTRAINT actividad_parametro_fk_cod_parametro_fkey FOREIGN KEY (fk_cod_parametro) REFERENCES public.parametro(cod_parametro);


--
-- Name: analisis analisis_fk_cod_grupo_cuadro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.analisis
    ADD CONSTRAINT analisis_fk_cod_grupo_cuadro_fkey FOREIGN KEY (fk_cod_grupo_cuadro) REFERENCES public.grupo_cuadro(cod_grupo_cuadro);


--
-- Name: analisis analisis_fk_cod_recom_detalle_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.analisis
    ADD CONSTRAINT analisis_fk_cod_recom_detalle_fkey FOREIGN KEY (fk_cod_recom_detalle) REFERENCES public.recomendacion_detalle(cod_recom_detalle);


--
-- Name: analisis analisis_fk_cod_tipo_analisis_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.analisis
    ADD CONSTRAINT analisis_fk_cod_tipo_analisis_fkey FOREIGN KEY (fk_cod_tipo_analisis) REFERENCES public.tipo_analisis(cod_tipo_analisis);


--
-- Name: analisis analisis_fk_cod_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.analisis
    ADD CONSTRAINT analisis_fk_cod_usuario_fkey FOREIGN KEY (fk_cod_usuario) REFERENCES public.usuario(cod_usuario_private);


--
-- Name: analisis_param analisis_param_fk_cod_analisis_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.analisis_param
    ADD CONSTRAINT analisis_param_fk_cod_analisis_fkey FOREIGN KEY (fk_cod_analisis) REFERENCES public.analisis(cod_analisis);


--
-- Name: analisis_param analisis_param_fk_cod_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.analisis_param
    ADD CONSTRAINT analisis_param_fk_cod_parametro_fkey FOREIGN KEY (fk_cod_parametro) REFERENCES public.parametro(cod_parametro);


--
-- Name: cuadro_cultivo cuadro_cultivo_fk_cod_cuadro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cuadro_cultivo
    ADD CONSTRAINT cuadro_cultivo_fk_cod_cuadro_fkey FOREIGN KEY (fk_cod_cuadro) REFERENCES public.cuadro(cod_cuadro);


--
-- Name: cuadro_cultivo cuadro_cultivo_fk_cod_cultivo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cuadro_cultivo
    ADD CONSTRAINT cuadro_cultivo_fk_cod_cultivo_fkey FOREIGN KEY (fk_cod_cultivo) REFERENCES public.cultivo(cod_cultivo);


--
-- Name: cuadro_cultivo cuadro_cultivo_fk_cod_grupo_cuadro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cuadro_cultivo
    ADD CONSTRAINT cuadro_cultivo_fk_cod_grupo_cuadro_fkey FOREIGN KEY (fk_cod_grupo_cuadro) REFERENCES public.grupo_cuadro(cod_grupo_cuadro);


--
-- Name: cuadro cuadro_fk_cod_parcela_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cuadro
    ADD CONSTRAINT cuadro_fk_cod_parcela_fkey FOREIGN KEY (fk_cod_parcela) REFERENCES public.parcela(cod_parcela);


--
-- Name: cultivo cultivo_fk_cod_estado_planificacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cultivo
    ADD CONSTRAINT cultivo_fk_cod_estado_planificacion_fkey FOREIGN KEY (fk_cod_estado_planificacion) REFERENCES public.estado_planificacion(cod_estado_planificacion);


--
-- Name: cultivo cultivo_fk_cod_tipo_cultivo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cultivo
    ADD CONSTRAINT cultivo_fk_cod_tipo_cultivo_fkey FOREIGN KEY (fk_cod_tipo_cultivo) REFERENCES public.tipo_cultivo(cod_tipo_cultivo);


--
-- Name: finca_usuario finca_usuario_fk_cod_finca_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.finca_usuario
    ADD CONSTRAINT finca_usuario_fk_cod_finca_fkey FOREIGN KEY (fk_cod_finca) REFERENCES public.finca(cod_finca);


--
-- Name: finca_usuario finca_usuario_fk_cod_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.finca_usuario
    ADD CONSTRAINT finca_usuario_fk_cod_usuario_fkey FOREIGN KEY (fk_cod_usuario) REFERENCES public.usuario(cod_usuario_private);


--
-- Name: grupo_cuadro grupo_cuadro_fk_cod_parcela_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_cuadro
    ADD CONSTRAINT grupo_cuadro_fk_cod_parcela_fkey FOREIGN KEY (fk_cod_parcela) REFERENCES public.parcela(cod_parcela);


--
-- Name: grupo_cuadro grupo_cuadro_fk_cod_planificacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_cuadro
    ADD CONSTRAINT grupo_cuadro_fk_cod_planificacion_fkey FOREIGN KEY (fk_cod_planificacion) REFERENCES public.planificacion(cod_planificacion);


--
-- Name: img_activ_detalle img_activ_detalle_fk_cod_activ_detalle_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.img_activ_detalle
    ADD CONSTRAINT img_activ_detalle_fk_cod_activ_detalle_fkey FOREIGN KEY (fk_cod_activ_detalle) REFERENCES public.actividad_detalle(cod_activ_detalle);


--
-- Name: parametro parametro_fk_cod_tipo_dato_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parametro
    ADD CONSTRAINT parametro_fk_cod_tipo_dato_fkey FOREIGN KEY (fk_cod_tipo_dato) REFERENCES public.tipo_dato(cod_tipo_dato);


--
-- Name: parametro parametro_fk_cod_tipo_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parametro
    ADD CONSTRAINT parametro_fk_cod_tipo_parametro_fkey FOREIGN KEY (fk_cod_tipo_parametro) REFERENCES public.tipo_parametro(cod_tipo_parametro);


--
-- Name: parametro_opcion parametro_opcion_fk_cod_opcion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parametro_opcion
    ADD CONSTRAINT parametro_opcion_fk_cod_opcion_fkey FOREIGN KEY (fk_cod_opcion) REFERENCES public.opcion(cod_opcion);


--
-- Name: parametro_opcion parametro_opcion_fk_cod_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parametro_opcion
    ADD CONSTRAINT parametro_opcion_fk_cod_parametro_fkey FOREIGN KEY (fk_cod_parametro) REFERENCES public.parametro(cod_parametro);


--
-- Name: parcela parcela_fk_cod_finca_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parcela
    ADD CONSTRAINT parcela_fk_cod_finca_fkey FOREIGN KEY (fk_cod_finca) REFERENCES public.finca(cod_finca);


--
-- Name: plan plan_fk_cod_grupo_cuadro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plan
    ADD CONSTRAINT plan_fk_cod_grupo_cuadro_fkey FOREIGN KEY (fk_cod_grupo_cuadro) REFERENCES public.grupo_cuadro(cod_grupo_cuadro);


--
-- Name: plan plan_fk_cod_tipo_plan_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plan
    ADD CONSTRAINT plan_fk_cod_tipo_plan_fkey FOREIGN KEY (fk_cod_tipo_plan) REFERENCES public.tipo_plan(cod_tipo_plan);


--
-- Name: plan plan_fk_cod_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plan
    ADD CONSTRAINT plan_fk_cod_usuario_fkey FOREIGN KEY (fk_cod_usuario) REFERENCES public.usuario(cod_usuario_private);


--
-- Name: plan_param plan_param_fk_cod_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plan_param
    ADD CONSTRAINT plan_param_fk_cod_parametro_fkey FOREIGN KEY (fk_cod_parametro) REFERENCES public.parametro(cod_parametro);


--
-- Name: plan_param plan_param_fk_cod_plan_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plan_param
    ADD CONSTRAINT plan_param_fk_cod_plan_fkey FOREIGN KEY (fk_cod_plan) REFERENCES public.plan(cod_plan);


--
-- Name: planificacion planificacion_fk_cod_estado_planificacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planificacion
    ADD CONSTRAINT planificacion_fk_cod_estado_planificacion_fkey FOREIGN KEY (fk_cod_estado_planificacion) REFERENCES public.estado_planificacion(cod_estado_planificacion);


--
-- Name: planificacion planificacion_fk_cod_finca_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planificacion
    ADD CONSTRAINT planificacion_fk_cod_finca_fkey FOREIGN KEY (fk_cod_finca) REFERENCES public.finca(cod_finca);


--
-- Name: planificacion planificacion_fk_cod_grupo_planificacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planificacion
    ADD CONSTRAINT planificacion_fk_cod_grupo_planificacion_fkey FOREIGN KEY (fk_cod_grupo_planificacion) REFERENCES public.grupo_planificacion(cod_grupo_planificacion);


--
-- Name: planificacion planificacion_fk_cod_tipo_planificacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planificacion
    ADD CONSTRAINT planificacion_fk_cod_tipo_planificacion_fkey FOREIGN KEY (fk_cod_tipo_planificacion) REFERENCES public.tipo_planificacion(cod_tipo_planificacion);


--
-- Name: planificacion planificacion_fk_cod_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.planificacion
    ADD CONSTRAINT planificacion_fk_cod_usuario_fkey FOREIGN KEY (fk_cod_usuario) REFERENCES public.usuario(cod_usuario_private);


--
-- Name: recom_detalle_param recom_detalle_param_fk_cod_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recom_detalle_param
    ADD CONSTRAINT recom_detalle_param_fk_cod_parametro_fkey FOREIGN KEY (fk_cod_parametro) REFERENCES public.parametro(cod_parametro);


--
-- Name: recom_detalle_param recom_detalle_param_fk_cod_recom_detalle_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recom_detalle_param
    ADD CONSTRAINT recom_detalle_param_fk_cod_recom_detalle_fkey FOREIGN KEY (fk_cod_recom_detalle) REFERENCES public.recomendacion_detalle(cod_recom_detalle);


--
-- Name: recomendacion_detalle recomendacion_detalle_fk_cod_recomendacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion_detalle
    ADD CONSTRAINT recomendacion_detalle_fk_cod_recomendacion_fkey FOREIGN KEY (fk_cod_recomendacion) REFERENCES public.recomendacion(cod_recomendacion);


--
-- Name: recomendacion_detalle recomendacion_detalle_fk_cod_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion_detalle
    ADD CONSTRAINT recomendacion_detalle_fk_cod_usuario_fkey FOREIGN KEY (fk_cod_usuario) REFERENCES public.usuario(cod_usuario_private);


--
-- Name: recomendacion_parametro recomendacion_parametro_fk_cod_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion_parametro
    ADD CONSTRAINT recomendacion_parametro_fk_cod_parametro_fkey FOREIGN KEY (fk_cod_parametro) REFERENCES public.parametro(cod_parametro);


--
-- Name: recomendacion_parametro recomendacion_parametro_fk_cod_recomendacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recomendacion_parametro
    ADD CONSTRAINT recomendacion_parametro_fk_cod_recomendacion_fkey FOREIGN KEY (fk_cod_recomendacion) REFERENCES public.recomendacion(cod_recomendacion);


--
-- Name: recurso recurso_fk_tipo_recurso_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recurso
    ADD CONSTRAINT recurso_fk_tipo_recurso_fkey FOREIGN KEY (fk_tipo_recurso) REFERENCES public.tipo_recurso(cod_tipo_recurso);


--
-- Name: tipo_analisis_param tipo_analisis_param_fk_cod_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_analisis_param
    ADD CONSTRAINT tipo_analisis_param_fk_cod_parametro_fkey FOREIGN KEY (fk_cod_parametro) REFERENCES public.parametro(cod_parametro);


--
-- Name: tipo_analisis_param tipo_analisis_param_fk_cod_tipo_analisis_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_analisis_param
    ADD CONSTRAINT tipo_analisis_param_fk_cod_tipo_analisis_fkey FOREIGN KEY (fk_cod_tipo_analisis) REFERENCES public.tipo_analisis(cod_tipo_analisis);


--
-- Name: tipo_plan_param tipo_plan_param_fk_cod_parametro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_plan_param
    ADD CONSTRAINT tipo_plan_param_fk_cod_parametro_fkey FOREIGN KEY (fk_cod_parametro) REFERENCES public.parametro(cod_parametro);


--
-- Name: tipo_plan_param tipo_plan_param_fk_cod_tipo_plan_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_plan_param
    ADD CONSTRAINT tipo_plan_param_fk_cod_tipo_plan_fkey FOREIGN KEY (fk_cod_tipo_plan) REFERENCES public.tipo_plan(cod_tipo_plan);


--
-- Name: usuario usuario_fk_cod_rol_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_fk_cod_rol_fkey FOREIGN KEY (fk_cod_rol) REFERENCES public.rol(cod_rol);


--
-- PostgreSQL database dump complete
--

