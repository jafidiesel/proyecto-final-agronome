import { Injectable } from '@angular/core';
import { NomencladorInterface } from '../../data/nomenclador';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ConfiguracionService {

  private nomencladorData = [
    ['Nombre', 'Activo', 'Tipo Nomenclador', 'Accion', ''],
    ['En Curso', 'Si', 'EstadoPlanificacion', '*/configuracion/editarNomenclador', '-/Desactivar'],
    ['Inicial', 'Si', 'TipoPlanificacion', '*/configuracion/editarNomenclador', '-/Desactivar'],
    ['Supervisada', 'Si', 'TipoPlanificacion', '*/configuracion/editarNomenclador', '-/Desactivar']
  ];

  private parametroData = [
    ['Nombre', 'Activo', 'Tipo de dato', 'Tipo de parámetro', 'Accion', ''],
    ['Hora de riego', 'Si', 'Time', 'Actividad', '*/configuracion/editarParametro', '-/Desactivar'],
    ['Cantidad', 'Si', 'Number', 'Actividad', '*/configuracion/editarParametro', '-/Desactivar'],
    ['Fecha', 'Si', 'Date', 'Recomendación', '*/configuracion/editarParametro', '-/Desactivar']
];

  private opcionesParametro = [
    'mañana',
    'tarde',
    'noche'
  ];

  private planData = [
    ['Nombre', 'Activo', 'Accion', ''],
    ['Riego', 'Si', '*/editar', '-/Desactivar'],
    ['Siembra', 'Si', '*/editar', '-/Desactivar'],
    ['Cosecha', 'Si', '*/editar', '-/Desactivar']
  ];

  private recomendacionData = [
    ['Nombre', 'Activo', 'Accion', ''],
    ['Fitosanitaria', 'Si', '*/editar', '-/Desactivar'],
    ['Fitosanitaria', 'Si', '*/editar', '-/Desactivar'],
    ['Fitosanitaria', 'Si', '*/editar', '-/Desactivar']
];
  private analisisData = [
    ['Nombre', 'Activo', 'Accion', ''],
    ['Suelo', 'Si', '*/editar', '-/Desactivar'],
    ['Agua', 'Si', '*/editar', '-/Desactivar'],
    ['Superficie', 'Si', '*/editar', '-/Desactivar']
];

  private actividadData = [
    ['Nombre', 'Activo', 'Accion', ''],
    ['Riego', 'Si', '*/editar', '-/Desactivar'],
    ['Cosecha', 'Si', '*/editar', '-/Desactivar'],
    ['Siembra', 'Si', '*/editar', '-/Desactivar']
];

  constructor( private http: HttpClient ) { }

  getNomencladorData() {
    return this.nomencladorData;
  }

  getParametroData() {
    return this.parametroData;
  }

  getOpcionesParametrotroData() {
    return this.opcionesParametro;
  }

  setOpcionesParametrotroData(opcion:string) {
    this.opcionesParametro.push(opcion);
    console.log(this.opcionesParametro);
  }

  getPlanData() {
    return this.planData;
  }

  getRecomendacionData() {
    return this.recomendacionData;
  }

  getAnalisisData() {
    return this.analisisData;
  }

  getActividadData() {
    return this.actividadData;
  }
  

  getTipoNomenclador(): Observable<string[]> {
    return of(['actividad',
    'estadoPlanificacion',
    'opcion',
    'permiso',
    'recomendacion',
    'recurso',
    'rol',
    'tipoAnalisis',
    'tipoCultivo',
    'tipoDato',
    'tipoParametro',
    'tipoPlan',
    'tipoPlanificacion',
    'tipoRecurso',
  ]);
  }

  postNomencladorForm( nomencladorForm: NomencladorInterface ) : Observable<any> {
    //return of(nomencladorForm);
    
    return this.http.post( 'http://localhost:9001/api/configuracion/nomenclador', nomencladorForm);

  }


}
