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
  getListasActividad(cod: string): Observable<any> {
    let json = {
      codLibroCampo: parseInt(cod)
    }
    return this.http.post<string>(`http://localhost:9001/api/recomendacion/actividad`, json);
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

  /**
  * @param codFinca number 
  * @return Observable<string>
  *  
  * POST obtiene los libros de campo de la finca segun el codFinca enviado
  */
 getLibrosCampoRecomendacion(codFinca: number): Observable<any> {
  let json = {
    codFinca: codFinca
  }
  return this.http.post<string>(`http://localhost:9001/api/libroCampo/recomendacion`, json);
}
}
