import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SeguridadService {

  params = new HttpHeaders()
    .set("Authorization", "Bearer  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidXN1YXJpbzQiLCJyb2wiOiJhZG1pbmlzdHJhZG9yIiwianRpIjoiZmMwMWU3MGYtY2ZkOS00Mjc1LWExNjMtZDFkN2QwMzZlOTYzIiwiZXhwIjoxNTcxMDk2NTk1fQ.9sBTYhk21SSRw1_OqbQ56JUvLLdbyiVLNzq_FMsT-8s");

  constructor(private http: HttpClient) {
    console.log("SeguridadService up and running");

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
  * @param form form
  *  
  * Devuelve todos los nomencladores activos creados del tipo enviado por parámetro
  */
  postUsuario(json: any): Observable<String> {

    return this.http.post<String>(`http://localhost:9001/api/users`, json);
  }

  /**
  * @return List Observable<Object>
  *  
  * Devuelve todos los usuarios
  */
  getUsuarios(): Observable<String> {

    return this.http.get<String>(`http://localhost:9001/api/users`);
  }

  /**
  * @param cod string
  * @return Observable<Object>
  *  
  * Devuelve los datos de un usuario segun su cod
  */
  getUsuario(cod: string): Observable<String> {

    return this.http.get<String>(`http://localhost:9001/api/users/${cod}`);
  }

  /**
  * @param cod string
  *  
  * Actualiza los datos de un usuario
  */
  putUsuario(cod: string, json: any): Observable<String> {

    return this.http.put<String>(`http://localhost:9001/api/users/${cod}`, json);
  }

  /**
  * @param cod string
  *  
  * Actualiza los datos de un usuario
  */
  checkUsername(user: string): Observable<String> {
    let json = {
      atributo: "usuario",
      valor: user
    }

    return this.http.post<String>(`http://localhost:9001/api/users/account/user`, json);
  }

  /**
  * @param cod string
  *  
  * Actualiza los datos de un usuario
  */
  checkEmail(email: string): Observable<String> {
    let json = {
      atributo: "email",
      valor: email
    }
    return this.http.post<String>(`http://localhost:9001/api/users/account/user`, json);
  }

    /**
  * @param cod string
  *  
  * Actualiza los datos de un usuario
  */
 checkContraseniaUsuario(contraseniaUsuario: string): Observable<String> {
  let json = {
    atributo: "contraseniaUsuario",
    valor: contraseniaUsuario
  }
  return this.http.post<String>(`http://localhost:9001/api/users/account/user`, json);
}

}
