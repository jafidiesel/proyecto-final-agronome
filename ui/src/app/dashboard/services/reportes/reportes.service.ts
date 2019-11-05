import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReportesService {

  constructor(private http: HttpClient) {
    console.log("ReportesService up and running");
  }

  /**
  * @param json json
  * @return Observable<string>
  *  
  * POST obtiene el dataset para realizar la grafica de barras de actividades
  */
  getReporteActividad(fechaDesde:any, fechaHasta:any): Observable<any> {
    let json = {
      fchDesde: String(fechaDesde.year + "-" + fechaDesde.month + "-" + fechaDesde.day + " 00:00"),
      fchHasta: String(fechaHasta.year + "-" + fechaHasta.month + "-" + fechaHasta.day + " 23:00")
    }
    return this.http.post<String>(`http://localhost:9001/api/reporte/actividadGfBar`, json);
  }

  /**
  * @param json json
  * @return Observable<string>
  *  
  * POST obtiene el dataset para realizar la grafica de torta de recomendaciones
  */
  getReporteRecomendacion(json: any): Observable<any> {
    return this.http.post(`http://localhost:9001/api/recomendacion/actividad`, json);
  }

  /**
  * @param json json
  * @return Observable<string>
  *  
  * POST obtiene el dataset para realizar la grafica de barras de siembra
  */
  getReporteSiembra(json: any): Observable<any> {
    return this.http.post(`http://localhost:9001/api/recomendacion/actividad`, json);
  }

}
