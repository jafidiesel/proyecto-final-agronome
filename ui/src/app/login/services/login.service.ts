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
    console.log('token to send: ', token);
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': token
      })
    };

    if (token != 'empty') {
      debugger;
      console.log('token con valor', token);
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

    return this.http.post<String>(`http://localhost:9001/api/users/account/recover`, { usuario: usuarioReceived }  );

  }



}
