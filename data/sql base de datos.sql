
##analisis de agua:
INSERT INTO public.parametro(
            nombre_parametro, is_activ, fk_cod_tipo_parametro, 
            fk_cod_tipo_dato)
    VALUES 
('fuente de riego ',TRUE,4,1),
('calcio mg/l',TRUE,4,3),
('sodio mg/l',TRUE,4,3),
('bicarbonatos mg/l',TRUE,4,3),
('sulfato mg/l',TRUE,4,3),
('nitrato - nitrógeno',TRUE,4,3),
('fosfato - fósforo',TRUE,4,3),
('boro',TRUE,4, 3),
('temperatura del agua',TRUE,4,3),
('temperatura del aire',TRUE,4,3),
('tipo de riego',TRUE,4,6),
('sales totales g/l',TRUE,4,3),
('magnesiomg/l',TRUE,4, 3),
('carbonatos mg/l',TRUE,4,3),
('cloro mg/l',TRUE,4,3),
('dureza total',TRUE,4,3),
('amonio - nitrógeno',TRUE,4,3),
('potasio',TRUE,4,3),
('acidez',TRUE,4,3),
('relación de absorción de sodio',TRUE,4, 3),
('humedad del aire',TRUE,4,3);

SELECT nombre_parametro
  FROM public.parametro
  GROUP BY nombre_parametro 
     HAVING COUNT(*)>1;




##PARAMETrOS tipo_analisis_param
##.tipo_analisis_param
INSERT INTO public.tipo_analisis_param(
            is_activ, fk_cod_parametro, fk_cod_tipo_analisis)
    VALUES 
##ANALISIS DE SUELO
(TRUE,11,2),
(TRUE,12,2),
(TRUE,13,2),
(TRUE,14,2),
(TRUE,15,2),
(TRUE,16,2),
(TRUE,17,2),
(TRUE,18,2),
(TRUE,19,2),
(TRUE,20,2),
(TRUE,21,2),
(TRUE,22,2),
(TRUE,23,2);

##analasis de agua
(TRUE,23,1),
(TRUE,24,1),
(TRUE,25,1),
(TRUE,26,1),
(TRUE,27,1),
(TRUE,28,1),
(TRUE,29,1),
(TRUE,30,1),
(TRUE,31,1),
(TRUE,32,1),
(TRUE,33,1),
(TRUE,34,1),
(TRUE,35,1),
(TRUE,36,1),
(TRUE,37,1),
(TRUE,38,1),
(TRUE,39,1),
(TRUE,40,1),
(TRUE,41,1),
(TRUE,42,1),
(TRUE,43,1),
(TRUE,44,1);



##Actidades parametros

#actividad de riego

('tipo de riego',TRUE,1,6),
('fuente de riego',TRUE,1,1),
('caudal M3/h',TRUE,1,3),
('total M3/h',TRUE,1,3),
('pH',TRUE,1,3);

Parm activida de riego
(TRUE,45,1),
(TRUE,46,1),
(TRUE,47,1),
(TRUE,48,1),
(TRUE,49,1);



#actividad de siembra

('tipo de siembra',TRUE,1,6),
('cultivo y variedad a plantar',TRUE,1,1),
('marco de plantación (distancia entre las plantas)' ,TRUE,1,3),
('fecha estimada de recolección',TRUE,1,7),
('cantidad de plantas por m2',TRUE,1,2),
('profundidad (cm)',TRUE,1,3);

#Parm activida de siembra
(TRUE,50,2), 
(TRUE,51,2),
(TRUE,52,2),
(TRUE,53,2),
(TRUE,54,2),
(TRUE,55,2);





#activida de fertilizacion
56 ('fertilizante/Abono (nombre)',TRUE,1,1),
57 ('marca',TRUE,1,1),
58 ('dosis',TRUE,1,3),
59 ('unidades (Ámbito) unidad de medida de la dosis',TRUE,1,3),
60 ('dosis',TRUE,1,2);

#Parm activida de fertilizacion 
(TRUE,56,3),
(TRUE,57,3),
(TRUE,58,3),
(TRUE,59,3),
(TRUE,60,3);




#Actividad de preparación de suelo:

61 ('actividad',TRUE,1,6),
62 ('profundidad (Cm)',TRUE,1,3),
63 ('velocidad (Km/h)',TRUE,1,3);

#Parm Actividad de preparación de suelo
(TRUE,61,4),
(TRUE,62,4),
(TRUE,63,4);


#activida de tratamiento fitosanitario

64 ('es objeto de asesoramiento',TRUE,1,6),
65 ('nro de recomendación',TRUE,1,2),
66 ('enfermedad o Plaga',TRUE,1,6),
67 ('producto',TRUE,1,1),
68 ('marca',TRUE,1,1),
69 ('dosis',TRUE,1,3),
59 ('unidades (Ámbito)',TRUE,1,1), //porque ya existe no hay que crearlo
70 ('plazo de seguridad',TRUE,1,5);

#Parm  activida de tratamiento fitosanitario
(TRUE,64,5),
(TRUE,65,5),
(TRUE,66,5),
(TRUE,67,5),
(TRUE,68,5),
(TRUE,69,5),
(TRUE,59,5),
(TRUE,70,5);





#actividad de cosecha
71 ('producción cosechada (cantidad)',TRUE,1,3),
72 ('finalización de cultivo',TRUE,1,6);

#Parm  actividad de cosecha
(TRUE,71,6);
(TRUE,72,6);


#actividad de detección situación fitosanitaria 
73 ('posible enfermedad o Plaga',TRUE,1,6);

#Parm actividad detección situación fitosanitaria 
(TRUE,73,7);


#Actividad de detección de catástrofe
74 ('nombre de catástrofe',TRUE,1,1);
#Parm  Actividad de detección de catástrof
(TRUE,74,8);


#Actidad de fertirrigacion
75 ('equipo fertirrigación',TRUE,1,1),
76 ('nombre fertilizante',TRUE,1,1),
77 ('sulfato de potasio',TRUE,1,3),
78 ('sulfato amónico',TRUE,1,3),
79 ('sulfato magnesio',TRUE,1,3),
80 ('fosfato M potasio',TRUE,1,3),
81 ('tiempo de riego',TRUE,1,5),
82 ('conductividad eléctrica',TRUE,1,3);

#Parm  Actidad de fertirrigacion

(TRUE,75,9),
(TRUE,76,9),
(TRUE,77,9),
(TRUE,78,9),
(TRUE,79,9),
(TRUE,80,9),
(TRUE,81,9),
(TRUE,82,9),
(TRUE,49,9);


#Recomendacion fitosanitaria

83 ('plazo de seguridad',TRUE,2,2),
84 ('dosis recomendada',TRUE,2,3),
85 ('cantidad total recomendada',TRUE,2,3),
86 ('plazo máximo de aplicación',TRUE,2,7),
87 ('plazo mínimo de reentrada',TRUE,2,7),
88 ('compuesto',TRUE,2,1),
89 ('producto recomendado',TRUE,2,1),
90 ('enfermedad o plaga',TRUE,2,6);

#parm Recomendacion fitosanitaria

(TRUE,83,1),
(TRUE,84,1),
(TRUE,85,1),
(TRUE,86,1),
(TRUE,87,1),
(TRUE,88,1),
(TRUE,89,1),
(TRUE,90,1);


Recomendacion de catastrofe
91 ('nombre de catástrofe',TRUE,2,1);
#parm Recomendacion de catastrofe
(TRUE,91,2);