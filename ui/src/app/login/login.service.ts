import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) { }

  /**
  * @return Observable<string>
  *  
  * GET obtiene la lista de actividades recomendadas y a recomendar
  */
  getActivar(token:any): Observable<any> {
    return this.http.post<string>(`http://localhost:9001/api/users/account/activate`,token);
  }
}
