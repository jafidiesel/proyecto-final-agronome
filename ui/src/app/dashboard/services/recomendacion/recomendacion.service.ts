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
}
