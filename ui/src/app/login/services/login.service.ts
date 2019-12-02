import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) {
    console.log("LoginService up and running");
  }

  /**
  * @param token string (opcional)
  * @return Observable<string>
  *  
  * POST activa el usuario mediante el token que se envia por url
  */
  activateUser(token: string = 'empty'): Observable<any> {
    let result;

    if (token != 'empty') {
      result = this.http.get<String>(
        `http://localhost:9001/api/users/account/activate`,
        {
          headers: new HttpHeaders({ "Authorization": "Bearer " + token })
        });

    }
    return result;
  }

  /**
  * @param usuario string
  * @return Observable<string>
  *  
  * POST envia el usuario a recuperar la contraseña
  */
  sendRecover(usuarioReceived: string): Observable<any> {

    return this.http.post<String>(`http://localhost:9001/api/users/account/recover`, { usuario: usuarioReceived });

  }

  /**
  * @param usuario string
  * @return Observable<string>
  *  
  * POST envia el usuario a recuperar la contraseña
  */
  confirmPassword(password1: string, password2: string, token: string = 'empty'): Observable<any> {

    let result;
    let json = {
      pass: password1,
      passConfirm: password2
    }

    if (token != 'empty') {
      result = this.http.post<String>(
        `http://localhost:9001/api/users/account/restore`, json,
        {
          headers: new HttpHeaders({ "Authorization": "Bearer " + token })
        });

    }
    return result;
  }





}
