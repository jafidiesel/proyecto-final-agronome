import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RecomendacionService {

  constructor(private http: HttpClient) {
    console.log("RecomendacionService up and running");
  }

  /**
  * @return Observable<string>
  *  
  * GET obtiene la lista de actividades recomendadas y a recomendar
  */
  getListasActividad(): Observable<any> {
    return this.http.get<string>(`http://localhost:9001/api/recomendacion/actividad`);
  }

  /**
  * @param id number 
  * @return Observable<string>
  *  
  * GET obtiene la información detallada de una actividad segun el id enviado
  */
  getActividad(id: number): Observable<any> {
    return this.http.get<string>(`http://localhost:9001/api/actividad/registrar/${id}`);
  }

  /**
  * @param id number 
  * @return Observable<string>
  *  
  * GET obtiene la información detallada de una recomendacion segun el id enviado
  */
  getRecomendacion(id: number): Observable<any> {
    return this.http.get<string>(`http://localhost:9001/api/recomendacion/${id}`);
  }

  /**
  * @param id number 
  * @return Observable<string>
  *  
  * GET obtiene la estructura de una recomendacion segun el id enviado
  */
  getEstructuraRecomendacion(id: number): Observable<any> {
    return this.http.get<string>(`http://localhost:9001/api/recomendacion/parametros/${id}`);
  }

  /**
  * @param id number 
  * @return Observable<string>
  *  
  * GET obtiene la estructura de una recomendacion segun el id enviado
  */
  postRecomendacion(json: any): Observable<any> {
    return this.http.post(`http://localhost:9001/api/recomendacion/registrar`,json);
  }
}
