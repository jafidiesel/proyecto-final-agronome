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
}
