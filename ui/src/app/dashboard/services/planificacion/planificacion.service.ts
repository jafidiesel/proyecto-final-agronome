import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PlanificacionService {

  constructor(private http: HttpClient) {
    console.log("PlanificacionService up and running");
  }

  /**
  * @deprecated
  */
  getTipoPlanificacion() {
    if (localStorage.getItem('tipoPlanificacion')) {
      return localStorage.getItem('tipoPlanificacion');
    }
  }
  /**
  * @deprecated
  */
  deleteTipoPlanificacion() {
    localStorage.removeItem('tipoPlanificacion');
  }

  /**
  * @param codFinca number 
  * @return Observable<string>
  *  
  * GET obtiene las planificaciones creadas segun el codigo de la finca
  */
  getPlanificacionesCreadas(codFinca: number): Observable<any> {
    return this.http.get<string>(`http://localhost:9001/api/planificacion/grupos/${codFinca}`);
  }

  /**
  * @param codFinca number 
  * @return Observable<string>
  *  
  * GET obtiene las parcelas libres segun el codigo de la finca
  */
  getParcelasLibres(codFinca: number): Observable<any> {
    return this.http.get<string>(`http://localhost:9001/api/planificacion/parcelas/${codFinca}`);
  }

  /**
  * @param codFinca number 
  * @return Observable<string>
  *  
  * GET obtiene las parcelas libres segun el codigo de la finca
  */
  guardarPlanificacion(json:any): Observable<any> {
    return this.http.post<string>(`http://localhost:9001/api/planificacion`,json);
  }

}
