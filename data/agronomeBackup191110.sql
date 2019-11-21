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
    random_contrasenia_usuario character varying(1024),
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
2	74	tormenta
3	45	goteo
3	46	pileta
3	47	23,2
3	49	10
4	50	plantin
4	51	tomate perita
4	52	2,2
4	53	2019-12-15
4	54	10
4	55	8
5	56	flor hoja crecimiento
5	57	fertifox
5	58	5
5	59	mm3
6	61	arada
6	62	10
6	63	9
7	65	0
7	67	Insecticida
7	68	Glacoxan Cipermetrina
7	58	3
7	59	cm3
7	70	2019-09-30
8	71	100900
9	74	granizo
11	45	goteo
11	46	pileta
11	47	10
11	48	100
11	49	3
7	66	pulgón
10	73	pulgón
8	72	no
7	64	no
1	73	desconocida
12	50	plantin
12	51	tomate perita
12	52	2,2
12	53	2019-12-15
12	55	8
13	50	plantin
13	51	tomate perita
13	52	2,2
13	53	2019-12-15
13	55	8
13	54	20
12	54	30
14	50	semilla
14	51	tomate perita
14	52	2,2
14	53	2019-12-15
14	54	99
14	55	8
32	45	aspersion
32	46	pileta
32	47	23,2
32	48	950
3	48	1231,2
15	45	aspersion
15	46	pileta
15	47	2
15	48	100.3
15	49	4
16	73	mosca blanca
17	45	goteo
17	46	pileta
17	47	10
17	48	20
17	49	2
18	45	goteo
18	47	12
18	48	32
18	49	2
18	46	pileta
19	73	trips
20	45	goteo
20	46	pileta
20	47	23,2
20	48	200
20	49	10
21	45	goteo
21	46	pileta
21	47	23,2
21	49	10
22	45	goteo
22	46	pileta
22	47	23,2
22	48	300
22	49	10
21	48	900
23	45	aspersion
23	46	pileta
23	47	23,2
23	48	300
23	49	10
24	45	aspersion
24	46	pileta
24	47	23,2
24	48	159
24	49	10
25	45	aspersion
25	46	pileta
25	47	23,2
25	48	159
25	49	10
26	45	aspersion
26	46	pileta
26	47	23,2
26	48	159
26	49	10
27	45	aspersion
27	46	pileta
27	47	23,2
27	48	169
27	49	10
28	45	aspersion
28	46	pileta
28	47	23,2
28	48	450
28	49	10
29	45	goteo
29	46	pileta
29	47	23,2
29	48	200
29	49	10
30	45	aspersion
30	46	pileta
30	47	23,2
30	48	450
30	49	10
31	45	aspersion
31	46	pileta
31	47	23,2
31	48	175
31	49	10
32	49	10
33	45	aspersion
33	46	pileta
33	47	23,2
33	48	100
33	49	10
34	45	aspersion
34	46	pileta
34	47	23,2
34	48	160
34	49	10
35	45	goteo
35	46	pileta
35	47	23,2
35	48	199
35	49	10
36	45	goteo
36	46	pileta
36	47	23,2
36	48	250
36	49	10
37	45	goteo
37	46	pileta
37	47	23,2
37	48	175
37	49	10
38	45	goteo
38	46	pileta
38	47	23,2
38	48	500
38	49	10
39	45	goteo
39	46	pileta
39	47	23,2
39	48	500
39	49	10
40	45	goteo
40	46	pileta
40	47	23,2
40	48	250
40	49	10
41	45	goteo
41	46	pileta
41	47	23,2
41	48	250
41	49	10
42	45	aspersion
42	47	120
42	48	200
42	49	4.2
42	46	Pileta
43	73	trips
\.


--
-- Data for Name: actividad; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actividad (cod_actividad, nombre_actividad, is_activ) FROM stdin;
1	riego	t
2	siembra	t
3	fertilización	t
4	preparación suelo	t
6	cosecha	t
5	tratamiento fitosanitario	t
9	fertirrigación	t
8	detección fitosanitaria	t
7	detección catastrofe	t
\.


--
-- Name: actividad_cod_actividad_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actividad_cod_actividad_seq', 9, true);


--
-- Data for Name: actividad_detalle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actividad_detalle (cod_activ_detalle, fch_activ_detalle, observacion, is_eliminado, fk_cod_actividad, fk_cod_recom_detalle, fk_cod_usuario) FROM stdin;
1	2019-10-01 10:45:00	Las hojas tienen perforaciones	f	8	\N	2
3	2019-10-09 12:30:00		f	1	\N	2
4	2019-05-09 12:30:00		f	2	\N	2
5	2019-06-09 09:30:00	Fertilización completa	f	3	\N	2
6	2019-04-20 13:30:00	Se comienza con el arado de lo determinado en la planificación	f	4	\N	2
7	2019-09-20 16:00:00	Se realizo un tratamiento preventivo para los pulgones	f	5	\N	2
10	2019-11-02 20:45:00	Las hojas tienen pulgones	f	8	\N	2
2	2019-09-29 15:30:00	Lluvia torrencial, daña varios cultivos	f	7	1	2
12	2019-06-09 13:30:00		f	2	\N	2
15	2019-11-02 13:30:00	 	f	1	\N	1
16	2019-11-05 20:45:00	Las hojas tienen un bicho blanco	f	8	\N	2
9	2019-10-29 15:30:00	granizo, pequeño	f	7	2	2
17	2019-04-04 09:45:00	 Apenas se comienza el dia se realiza el riego	f	1	\N	2
14	2019-05-09 17:30:00		f	2	\N	2
13	2019-06-16 19:30:00		f	2	\N	2
11	2019-11-02 17:30:00	ultimo riego del día	f	1	\N	1
19	2019-10-30 13:30:00	 posibles trips	f	8	3	2
20	2019-04-09 12:30:00		f	1	\N	2
21	2019-04-29 09:30:00		f	1	\N	2
22	2019-06-09 12:35:00		f	1	\N	2
23	2019-06-09 12:35:00		f	1	\N	2
24	2019-06-12 12:35:00		f	1	\N	2
25	2019-06-02 12:35:00		f	1	\N	2
26	2019-02-02 12:35:00		f	1	\N	2
27	2019-02-20 12:35:00		f	1	\N	2
28	2019-03-20 12:35:00		f	1	\N	2
29	2019-07-20 20:35:00		f	1	\N	2
30	2019-07-20 20:35:00		f	1	\N	2
31	2019-08-10 19:35:00		f	1	\N	2
32	2019-09-30 20:35:00		f	1	\N	2
33	2019-05-30 20:35:00		f	1	\N	2
34	2019-01-20 19:35:00		f	1	\N	2
35	2019-01-25 19:35:00		f	1	\N	2
36	2019-02-05 20:35:00		f	1	\N	2
37	2019-03-05 22:35:00		f	1	\N	2
38	2019-05-05 22:35:00		f	1	\N	2
39	2019-08-05 22:35:00		f	1	\N	2
40	2019-08-25 22:35:00		f	1	\N	2
41	2019-09-10 12:35:00		f	1	\N	2
18	2019-11-05 14:45:00	Riego completo	f	1	\N	2
8	2019-11-03 16:00:00	Prueba	f	6	\N	2
42	2019-04-11 13:30:00	 Se rego al mediodia.	f	1	\N	40
43	2019-11-05 13:30:00	 Se encontro muchos trips en las hojas.	f	8	4	40
\.


--
-- Name: actividad_detalle_cod_activ_detalle_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actividad_detalle_cod_activ_detalle_seq', 43, true);


--
-- Data for Name: actividad_parametro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actividad_parametro (is_activ, fk_cod_parametro, fk_cod_actividad) FROM stdin;
t	45	1
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
t	61	4
t	62	4
t	63	4
t	64	5
t	65	5
t	66	5
t	67	5
t	68	5
t	59	5
t	70	5
t	71	6
t	72	6
t	75	9
t	76	9
t	77	9
t	78	9
t	79	9
t	80	9
t	81	9
t	82	9
t	49	9
t	73	8
t	74	7
t	58	5
t	46	1
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
3dcafe72553e
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
216	A11	69
217	A12	69
218	A21	69
219	A22	69
220	A31	69
221	A32	69
222	A41	69
223	A42	69
224	B11	70
225	B21	70
226	B31	70
227	B41	70
228	B51	70
229	B61	70
230	B71	70
231	A11	71
232	A12	71
233	A21	71
234	A22	71
235	A31	71
236	A32	71
237	A41	71
238	A42	71
239	B11	72
240	B21	72
241	B31	72
242	B41	72
243	B51	72
244	B61	72
245	B71	72
246	A11	73
247	A12	73
248	Parcela 111	74
249	Parcela 112	74
250	Parcela 113	74
251	Parcela 114	74
252	Parcela 115	74
253	Parcela 116	74
254	Parcela 117	74
255	Parcela 121	74
256	Parcela 122	74
257	Parcela 123	74
258	Parcela 124	74
259	Parcela 125	74
260	Parcela 126	74
261	Parcela 127	74
262	Parcela 131	74
263	Parcela 132	74
264	Parcela 133	74
265	Parcela 134	74
266	Parcela 135	74
267	Parcela 136	74
268	Parcela 137	74
269	Parcela 141	74
270	Parcela 142	74
271	Parcela 143	74
272	Parcela 144	74
273	Parcela 145	74
274	Parcela 146	74
275	Parcela 147	74
276	Parcela 151	74
277	Parcela 152	74
278	Parcela 153	74
279	Parcela 154	74
280	Parcela 155	74
281	Parcela 156	74
282	Parcela 157	74
283	Parcela 161	74
284	Parcela 162	74
285	Parcela 163	74
286	Parcela 164	74
287	Parcela 165	74
288	Parcela 166	74
289	Parcela 167	74
290	Parcela 171	74
291	Parcela 172	74
292	Parcela 173	74
293	Parcela 174	74
294	Parcela 175	74
295	Parcela 176	74
296	Parcela 177	74
297	Parcela 181	74
298	Parcela 182	74
299	Parcela 183	74
300	Parcela 184	74
301	Parcela 185	74
302	Parcela 186	74
303	Parcela 187	74
304	Parcela 191	74
305	Parcela 192	74
306	Parcela 193	74
307	Parcela 194	74
308	Parcela 195	74
309	Parcela 196	74
310	Parcela 197	74
311	Parcela 1101	74
312	Parcela 1102	74
313	Parcela 1103	74
314	Parcela 1104	74
315	Parcela 1105	74
316	Parcela 1106	74
317	Parcela 1107	74
\.


--
-- Name: cuadro_cod_cuadro_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cuadro_cod_cuadro_seq', 317, true);


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
3	lepraaa	12341	t	Alvarez	2024	Las heras	Mendoza
10	nueva finca 5 Huertas	12341	t	Alvarez	2024	Las heras	Mendoza
11	nueva finca de prueba	1234123	t	mazza	199	 Las Heras	Mendoza
12	nuva finca fanco	12341	t	Alvarez	2024	Las heras	Mendoza
13	nuva finca fanco3	12341	t	Alvarez	2024	Las heras	Mendoza
9	4 Huertas	12341	t	Alvarez	2024	Las heras	Mendoza
14	finca de prueba	1234	t	rodriguez	273	 Capital	Mendoza
15	Tres arroyos	120000	t	rodriguez	273	 Capital	Mendoza
\.


--
-- Name: finca_cod_finca_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.finca_cod_finca_seq', 15, true);


--
-- Data for Name: finca_usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.finca_usuario (fk_cod_finca, fk_cod_usuario, fch_ini, fch_fin, is_activ) FROM stdin;
9	2	2019-10-26 00:31:34.527149	\N	t
15	40	2019-11-05 17:48:39.519688	\N	t
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
2	plantin	t
3	fertilizante	t
4	abono	t
5	goteo	t
6	aspersion	t
7	si	t
8	no	t
9	trips	t
10	pulgón	t
11	mosca blanca	t
12	araña roja	t
13	oruga	t
14	minadores de hojas	t
15	grillos, saltamontes y langostas	t
16	caracoles y babosas	t
17	cochinillas	t
18	nemátodos	t
19	mildiu	t
20	oídio	t
21	fusarium oxysporum	t
22	sclerotinia	t
23	fitóftora o phytophtora	t
24	pythium	t
25	rhizoctonia	t
26	desconocida	t
27	arada	t
28	disqueada	t
29	encanterada	t
30	colocación de riego	t
31	otra	t
1	semilla por mezcladora	t
\.


--
-- Name: opcion_cod_opcion_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.opcion_cod_opcion_seq', 31, true);


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
61	actividad	t	1	6
62	profundidad (Cm)	t	1	3
63	velocidad (Km/h)	t	1	3
64	es objeto de asesoramiento	t	1	6
65	nro de recomendación	t	1	2
66	enfermedad o Plaga	t	1	6
67	producto	t	1	1
68	marca	t	1	1
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
t	45	5
t	45	6
t	50	1
t	50	2
t	34	5
t	34	6
t	64	7
t	64	8
t	72	7
t	72	8
t	73	9
t	73	10
t	73	11
t	73	12
t	73	13
t	73	14
t	73	15
t	73	16
t	73	17
t	73	18
t	73	19
t	73	20
t	73	21
t	73	22
t	73	23
t	73	24
t	73	25
t	73	26
t	90	9
t	90	10
t	90	11
t	90	12
t	90	13
t	90	14
t	90	15
t	90	16
t	90	17
t	90	18
t	90	19
t	90	20
t	90	21
t	90	22
t	90	23
t	90	24
t	90	25
t	90	26
t	61	27
t	61	28
t	61	29
t	61	30
t	61	31
t	90	31
t	73	31
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
69	A	123.3	4	2	12
70	B	12097.299999999999	7	1	12
71	A	123.3	4	2	13
72	B	12097.299999999999	7	1	13
73	A	123	1	2	14
74	Parcela 1	1200	10	7	15
\.


--
-- Name: parcela_cod_parcela_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.parcela_cod_parcela_seq', 74, true);


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
1	91	Tormenta grado 3
2	91	granizo
3	90	trips
3	89	Herbicida
3	88	Glifosato
3	87	3 dias
3	86	10 dias
3	85	12
3	84	1
3	83	9
4	90	moscablanca
4	89	Herbicida 
4	88	Hm13
4	87	2 dias
4	86	15 días
4	85	1
4	84	2
4	83	7
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
1	2019-10-01 19:35:54	Se aconseja que el riego diario se desminuya en un 5%	f	f	2	3
2	2019-11-03 13:30:00	Llas plantas afectadas se deben arrancar para evitar afectar las otras.	f	f	2	1
3	2019-10-31 13:30:00	se debe colocar 1 vez al día en las plantas que tienen la enfermedad 	f	f	1	3
4	2019-11-05 13:30:00	 Prestar atencion al plazo de seguridad.	f	f	1	3
\.


--
-- Name: recomendacion_detalle_cod_recom_detalle_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recomendacion_detalle_cod_recom_detalle_seq', 4, true);


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
18	f6e8acbb-fec8-4c9d-ae7f-4402e94b4a7e	franco	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f695a6e4a68626d4e7649697769636d3973496a6f696157356e5a5735705a584a7649697769616e5270496a6f694d57597a4e44526b595467744e6a41315a5330305a6d45334c57457a597a4d744f4749354f544d30596d5a6a5a544d78496e302e68357937762d685943636753424630374230335f683938626d706c7548424a515048796f50626949556c34	ingeniero
16	5102c661-d783-4dfb-a32e-d5f4f1fc319e	melisa	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f696257567361584e6849697769636d3973496a6f695a57356a59584a6e595752765a6d6c75593245694c434a7164476b694f6949335a6a55795932517a4d4330315a44677a4c5452685a544d744f544e6a4d6931685a6a566c5a444d344f446b775a47516966512e4f65705a69313439677973535a4f76666c51716c4e6b384830754252364b576c486d794b443443452d5749	encargadofinca
19	ad2a4ea8-1def-4616-9473-af7efb06ba7a	jafi	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f69616d466d61534973496e4a7662434936496e4e3163475679646d6c7a623349694c434a7164476b694f694a6d4e6a6b79596d52685979316d4f5467794c5451774e4759744f44497a5979316b5a544d30596a4d305a6a4d34596a636966512e71564935325f597439436a4e56365a785749776875747474376b666a6146393775626c7737746d57334d67	supervisor
20	ac3cf02d-26f0-4dee-8e9e-81a7aadca58b	franco2	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f695a6e4a68626d4e764d694973496e4a7662434936496d5675593246795a32466b62325a70626d4e6849697769616e5270496a6f694d5451324d54466a4f574574595449314e6930304e6a63314c574a6d4e6d49744d44526859324932596a59795a44686d496e302e447459424a2d5a6854785035445436765a6b4e6d4c484e4b336e6750717671366f515258705635714c3973	encargadofinca
17	1	admin	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f6959575274615734694c434a79623277694f694a685a473170626d6c7a64484a685a47397949697769616e5270496a6f694e446b35596a4d304e6a4d744d32517a595330304d6a566a4c57466d4e5445744f44566a4f4755334e546b7a4d574a6d496e302e556e6f3753796b6941304b327179657069325874702d416955726b706f3855326c394d64794a4a54375f67	administrador
21	926f610d-f6f7-453c-9318-edc846404f7f	chechi	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f695932686c5932687049697769636d3973496a6f695a57356a59584a6e595752765a6d6c75593245694c434a7164476b694f6949324f47566c4f474d794e6930795a6d45304c5451774d3245744f546c684d6930355a6d51334f4467314d4455784d54416966512e61377559453266716a7776347a6f564769714538595a6a476c476874617235557a3571555f615164325051	encargadofinca
22	cd83db8a-981c-4bce-bf1f-2cc2742ad6bd	encargado10	\\x65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a3163325679496a6f695a57356a59584a6e595752764d5441694c434a79623277694f694a6c626d4e68636d64685a47396d6157356a59534973496d703061534936496d52684e5441344d445a694c5455794e7a59744e4759795a5330354e6a45324c5463794e3251344e6d56685a44517759694a392e4e37437251424647655a486f414956526f7a53346864734a4f775373472d464742355744466534574a7277	encargadofinca
\.


--
-- Name: sessionUser_cod_sessionUser_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."sessionUser_cod_sessionUser_seq"', 22, true);


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
4	ad2a4ea8-1def-4616-9473-af7efb06ba7a	jafi	javier	bravin	prueba@gmil.com	1234567	2019-10-15	\N	f	4	t
40	cd83db8a-981c-4bce-bf1f-2cc2742ad6bd	encargado10	juan	lopez	csirfranco@gmail.com	1234567	2019-11-05	\N	f	2	t
3	f6e8acbb-fec8-4c9d-ae7f-4402e94b4a7e	franco	franco	sanchez	csir@gmail.com	1234567	2019-10-15	\N	t	3	t
2	5102c661-d783-4dfb-a32e-d5f4f1fc319e	melisa	melisa	sosa	meli@gmail.com	1234567	2019-10-11	\N	f	2	t
1	1	admin	admin	admin	admin@gmail.com	1234567	2019-10-12	\N	f	1	t
\.


--
-- Name: usuario_cod_usuario_private_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_cod_usuario_private_seq', 40, true);


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
-- Name: tipo_cultivo tipo_cultivo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_cultivo
    ADD CONSTRAINT tipo_cultivo_pkey PRIMARY KEY (cod_tipo_cultivo);


--
-- Name: tipo_dato tipo_dato_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_dato
    ADD CONSTRAINT tipo_dato_pkey PRIMARY KEY (cod_tipo_dato);


--
-- Name: tipo_parametro tipo_parametro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_parametro
    ADD CONSTRAINT tipo_parametro_pkey PRIMARY KEY (cod_tipo_parametro);


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
-- Name: ix_actividad_nombre_actividad; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_actividad_nombre_actividad ON public.actividad USING btree (nombre_actividad);


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
-- Name: ix_cuadro_nombre_cuadro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_cuadro_nombre_cuadro ON public.cuadro USING btree (nombre_cuadro);


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
-- Name: ix_estado_planificacion_nombre_estado_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_estado_planificacion_nombre_estado_planificacion ON public.estado_planificacion USING btree (nombre_estado_planificacion);


--
-- Name: ix_finca_cod_finca; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_finca_cod_finca ON public.finca USING btree (cod_finca);


--
-- Name: ix_finca_nombre_finca; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_finca_nombre_finca ON public.finca USING btree (nombre_finca);


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
-- Name: ix_opcion_nombre_opcion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_opcion_nombre_opcion ON public.opcion USING btree (nombre_opcion);


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
-- Name: ix_parametro_nombre_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_parametro_nombre_parametro ON public.parametro USING btree (nombre_parametro);


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
-- Name: ix_parcela_nombre_parcela; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_parcela_nombre_parcela ON public.parcela USING btree (nombre_parcela);


--
-- Name: ix_permiso_cod_permiso; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_permiso_cod_permiso ON public.permiso USING btree (cod_permiso);


--
-- Name: ix_permiso_nombre_permiso; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_permiso_nombre_permiso ON public.permiso USING btree (nombre_permiso);


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
-- Name: ix_recomendacion_nombre_recomendacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_recomendacion_nombre_recomendacion ON public.recomendacion USING btree (nombre_recomendacion);


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
-- Name: ix_rol_nombre_rol; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_rol_nombre_rol ON public.rol USING btree (nombre_rol);


--
-- Name: ix_sessionUser_cod_sessionUser; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "ix_sessionUser_cod_sessionUser" ON public."sessionUser" USING btree ("cod_sessionUser");


--
-- Name: ix_tipo_analisis_cod_tipo_analisis; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_analisis_cod_tipo_analisis ON public.tipo_analisis USING btree (cod_tipo_analisis);


--
-- Name: ix_tipo_analisis_nombre_tipo_analisis; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_tipo_analisis_nombre_tipo_analisis ON public.tipo_analisis USING btree (nombre_tipo_analisis);


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
-- Name: ix_tipo_cultivo_nombre_tipo_cultivo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_tipo_cultivo_nombre_tipo_cultivo ON public.tipo_cultivo USING btree (nombre_tipo_cultivo);


--
-- Name: ix_tipo_dato_cod_tipo_dato; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_dato_cod_tipo_dato ON public.tipo_dato USING btree (cod_tipo_dato);


--
-- Name: ix_tipo_dato_nombre_tipo_dato; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_tipo_dato_nombre_tipo_dato ON public.tipo_dato USING btree (nombre_tipo_dato);


--
-- Name: ix_tipo_parametro_cod_tipo_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_parametro_cod_tipo_parametro ON public.tipo_parametro USING btree (cod_tipo_parametro);


--
-- Name: ix_tipo_parametro_nombre_tipo_parametro; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_tipo_parametro_nombre_tipo_parametro ON public.tipo_parametro USING btree (nombre_tipo_parametro);


--
-- Name: ix_tipo_plan_cod_tipo_plan; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_tipo_plan_cod_tipo_plan ON public.tipo_plan USING btree (cod_tipo_plan);


--
-- Name: ix_tipo_plan_nombre_tipo_plan; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_tipo_plan_nombre_tipo_plan ON public.tipo_plan USING btree (nombre_tipo_plan);


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
-- Name: ix_tipo_planificacion_nombre_tipo_planificacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_tipo_planificacion_nombre_tipo_planificacion ON public.tipo_planificacion USING btree (nombre_tipo_planificacion);


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

