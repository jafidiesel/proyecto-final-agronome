import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ActividadService {

  constructor(private http: HttpClient) {
    console.log("ActividadService up and running");

  }

  private dummyTextLibroDeCampo = [
    {
      nombre: "Libro de campo n°1",
      actividades: {

      }
    }
  ];

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
   * @param codActividad number
   * @return Observable<Object>
   *  
   * Realiza una peticion GET para obtener los parametros que componen la estructura de dicha actividad elegida
   */
  getEstructuraActividad(codActividad: number): Observable<any> {
    return this.http.get<string>(`http://localhost:9001/api/actividad/parametros/${codActividad}`);
  }


  /**
   * @param json any
   * @return Observable<Object>
   *  
   * Realiza una peticion post para registrar una actividad
   */
  postActividad(json: any) {
    return this.http.post(`http://localhost:9001/api/actividad`, json);
  }

  /**
  * @param id number
  * @return Observable<Object>
  *  
  * Realiza un delete para eliminar una actividad registrada (baja lógica)
  */
  deleteActividad(id: number) {
    return this.http.delete(`http://localhost:9001/api/actividad/${id}`);
  }

  /**
  * @return Observable<string>
  *  
  * GET obtiene la lista de actividades registradas
  */
  getListaActividades(): Observable<any> {
    return this.http.get<string>(`http://localhost:9001/api/actividad`);
  }

  /**
  * @param id number 
  * @return Observable<string>
  *  
  * GET obtiene la información detallada de una actividad segun el id enviado
  */
  getActividad(id: number): Observable<any> {
    return this.http.get<string>(`http://localhost:9001/api/actividad/${id}`);
  }

  /**
  * @param codFinca number 
  * @return Observable<string>
  *  
  * POST obtiene los libros de campo de la finca segun el codFinca enviado
  */
  getLibrosCampo(codFinca: number): Observable<any> {
    let json = {
      codFinca: 3
    }
    return this.http.post<string>(`http://localhost:9001/api/libroCampo`,json);
  }


}
