import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FincaService {

  constructor(private http: HttpClient) {
    console.log("FincaService up and running");
  }

  getProvincias(): Observable<String>{
    return this.http.get<String>('https://apis.datos.gob.ar/georef/api/provincias');
  }

  getMunicipios(idProvincia: number): Observable<String> {
    return this.http.get<String>(`https://apis.datos.gob.ar/georef/api/municipios?provincia=${idProvincia}&campos=id,nombre&max=100`);
  }

  /**
   * @param json any
   * @return Observable<Object>
   *  
   * Realiza una peticion post para crear una finca
   */
  
  postFinca(json:any){
    return this.http.post(`http://localhost:9001/api/finca`, json);
  }

}
