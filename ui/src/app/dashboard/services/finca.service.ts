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

  getProvincias(): Observable<String> {
    return this.http.get<String>('https://apis.datos.gob.ar/georef/api/provincias');
  }

  getProvincia(nombreProvincia: string): Observable<String> {
    return this.http.get<String>(`https://apis.datos.gob.ar/georef/api/provincias?nombre="${nombreProvincia}"`);
  }

  getMunicipios(idProvincia: number): Observable<String> {
    return this.http.get<String>(`https://apis.datos.gob.ar/georef/api/municipios?provincia=${idProvincia}&campos=id,nombre&max=100`);
  }

  getMunicipio(idProvincia: number, nombreMunicipio: string): Observable<String> {
    return this.http.get<String>(`https://apis.datos.gob.ar/georef/api/municipios?provincia=${idProvincia}&nombre=${nombreMunicipio}&campos=id,nombre`);
  }

  /**
   * @param json any
   * @return Observable<Object>
   *  
   * Realiza una peticion post para crear una finca
   */
  postFinca(json: any) {
    return this.http.post(`http://localhost:9001/api/finca`, json);
  }

  /**
   * @param codFinca number
   * @return Observable<Object>
   *  
   * Realiza una peticion get para obtener los datos de la finca
   */
  getFinca(codFinca: number) {
    return this.http.get<string>(`http://localhost:9001/api/finca/${codFinca}`);
  }

    /**
   * @param json any
   * @return Observable<Object>
   *  
   * Realiza una peticion post para crear una finca
   */
  putFinca(json: any, id:number) {
    return this.http.put(`http://localhost:9001/api/finca/${id}`, json);
  }

  
  // TODO: Testear la devolucion de la finca en la creacion de usuario
  /**
  * @return Observable<string>
  *  
  * GET obtiene todas las fincas
  */
 getFincas(): Observable<any> {
  return this.http.get<string>(`http://localhost:9001/api/finca`);
}



}
