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
    ['Hora de riego', 'Si', 'Time', 'Actividad', '*/configuracion/editarParametro/2', '-/Desactivar'],
    ['Cantidad', 'Si', 'Number', 'Actividad', '*/configuracion/editarParametro/2', '-/Desactivar'],
    ['Fecha', 'Si', 'Date', 'Recomendación', '*/configuracion/editarParametro/2', '-/Desactivar']
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
    ['Riego', 'Si', '*/configuracion/asociar/editarActividad/:id', '-/Desactivar'],
    ['Cosecha', 'Si', '*/configuracion/asociar/editarActividad/:id', '-/Desactivar'],
    ['Siembra', 'Si', '*/configuracion/asociar/editarActividad/:id', '-/Desactivar']
];

  constructor( private http: HttpClient ) { }

  /**
   * @deprecated Devuelve datos mockeados
   */
  getNomencladorData() {
    return this.nomencladorData;
  }

  /**
   * @deprecated Devuelve datos mockeados
   */
  getParametroData() {
    return this.parametroData;
  }

  /**
   * @deprecated Devuelve datos mockeados
   */
  getOpcionesParametrotroData() {
    return this.opcionesParametro;
  }

  /**
   * @deprecated Devuelve datos mockeados
   */
  setOpcionesParametrotroData(opcion:string) {
    this.opcionesParametro.push(opcion);
    console.log(this.opcionesParametro);
  }

  /**
   * @deprecated Devuelve datos mockeados
   */
  getPlanData() {
    return this.planData;
  }

  /**
   * @deprecated Devuelve datos mockeados
   */
  getRecomendacionData() {
    return this.recomendacionData;
  }

  /**
   * @deprecated Devuelve datos mockeados
   */
  getAnalisisData() {
    return this.analisisData;
  }
  
  /**
   * @deprecated Devuelve datos mockeados
   */
  getActividadData() {
    return this.actividadData;
  }

/**
 * @return observable<String [tipoNomenclador] [id]>
 * Description. Lista de los tipos de nomencladores
 */
  getTiposNomenclador() {
    let nomencladores=[
      ['actividad','0'],
      ['estadoPlanificacion','1'],
      ['opcion','2'],
      ['permiso','3'],
      ['recomendacion','4'],
      ['recurso','5'],
      ['rol','6'],
      ['tipoAnalisis','7'],
      ['tipoCultivo','8'],
      ['tipoDato','9'],
      ['tipoParametro','10'],
      ['tipoPlan','11'],
      ['tipoPlanificacion','12'],
      ['tipoRecurso','13'],
    ];
    return of(nomencladores);
  }
  
  postNomencladorForm( nomencladorJson: NomencladorInterface ): Observable<any> {
    //return of(nomencladorForm);
    return this.http.post( 'http://localhost:9001/api/configuracion/nomenclador', nomencladorJson);
  }

  putNomencladorForm( nomencladorJson: any ): Observable<any> {
    //return of(nomencladorForm);
    console.log(nomencladorJson);
    return this.http.put( `http://localhost:9001/api/configuracion/nomenclador/${nomencladorJson.tipoNomenclador}/${nomencladorJson.id}`, nomencladorJson);
  }

/**
 * @param tipoNomenclador string
 * @return Observable<Object>
 *  
 * Devuelve todos los nomencladores creados del tipo enviado por parámetro
 */
  getListaNomencladores(tipoNomenclador: string): Observable<String> {
    return this.http.get<String>(`http://localhost:9001/api/configuracion/nomenclador/${tipoNomenclador}`);
  }

  /**
 * @param tipoNomenclador string
 * @param isActiv boolean
 * @return Observable<Object>
 *  
 * Devuelve todos los nomencladores activos creados del tipo enviado por parámetro
 */
  getListaNomencladoresConFiltro(tipoNomenclador: string, isActiv: boolean): Observable<String> {
    let filtroJson = {
      "filtros":
        {
        "isActiv": isActiv
        }  
    }
    
    return this.http.post<String>(`http://localhost:9001/api/configuracion/nomenclador/${tipoNomenclador}`, filtroJson);
  }
  
  /**
   * @param tipoNomenclador string
   * @param id number
   * @return Observable<Object>
   *  
   * Obtiene un nomenclador en especifico
   */
  getNomenclador(tipoNomenclador: string, id: number){
    return this.http.get(`http://localhost:9001/api/configuracion/nomenclador/${tipoNomenclador}/${id}`);
  }

  /**
   * @param id number
   * @return Observable<Object>
   *  
   * Obtiene los datos del parametro segun su id
   */
  getParametro(id: number){
    return this.http.get( `http://localhost:9001/api/configuracion/parametro/${id}` );
    // http://localhost:9001/api/configuracion/parametro/2
    
  }

  /**
   * @param nomencladorJson any
   * @return Observable<Object>
   *  
   * Realiza una peticion post para almacenar el parametro creado
   */
  postParametroForm(parametroJson: any){
    //return of(nomencladorForm);
    return this.http.post( 'http://localhost:9001/api/configuracion/parametro', parametroJson);
  }

  /**
   * @param nomencladorJson any
   * @return Observable<Object>
   *  
   * Realiza una peticion put para modificar un parametro
   */
  putParametroForm(parametroJson: any){
    //return of(nomencladorForm);
    return this.http.put( 'http://localhost:9001/api/configuracion/parametro', parametroJson);
  }

  /**
   * @return Observable<Object>
   *  
   * Obtiene una lista de parametros
   */
  getListaParametros(){
    return this.http.get('http://localhost:9001/api/configuracion/parametro');
  }
  
  /**
   * @param tipoNomenclador string
   * @return Observable<Object>
   *  
   * O configuracion/asociar
   */
  getListaParametrosPorTipo(tipoNomenclador: string){
    return this.http.get(`http://localhost:9001/api/configuracion/parametro/${tipoNomenclador}`);
  }
  /**
   * @param asociacionJson json a guardar
   * @return Observable<Object>
   *  
   * POST configuracion/asociar
   */
  postAsociacionForm( asociacionJson: any ): Observable<any> {
    //return of(nomencladorForm);
    return this.http.post( 'http://localhost:9001/api/configuracion/asociar', asociacionJson);
  }

  /**
   * @param asociacionJson json a guardar
   * @return Observable<Object>
   *  
   * POST configuracion/asociar
   */
  getAsociacionForm( parametro:string, id: number ): Observable<any> {
    //return of(nomencladorForm);
    return this.http.get<string>( `http://localhost:9001/api/configuracion/asociar/${parametro}/${id}`);
  }

  putAsociacionForm( parametro:string, id: number, json:any ): Observable<any> {
    //return of(nomencladorForm);
    return this.http.put( `http://localhost:9001/api/configuracion/asociar/${parametro}/${id}`, json);
  }

  /**
   * @param parametro string
   * @return Observable<string>
   *  
   * GET obtiene la lista de asociaciones segun el parametro enviado
   */
  getListaAsociacion( parametro: string ): Observable<any> {
    //return of(nomencladorForm);
    return this.http.get<string>( `http://localhost:9001/api/configuracion/asociar/${parametro}`);
  }
}
