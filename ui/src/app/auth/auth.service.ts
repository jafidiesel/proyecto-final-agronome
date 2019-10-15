import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UsuarioModel } from '../models/usuario.model';
import { map } from 'rxjs/operators'

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  // login en api backend
  // http://localhost:9001/api/users/login
  /* {
  "usuario": "usuario21",
    "contraseniaUsuario": "sha256$WO3vlwV6$ec5e6d50c7a863021a6ea13cde0387936c5869d3d01d9deae5639884870a71c9"
  } */
  private url = 'http://localhost:9001/api/users/login';

  userToken: string;

constructor( private http : HttpClient ) { 
  this.leerToken();
 }

  logout(){

  }

  login( usuario: UsuarioModel ){
    return this.http.post(this.url, usuario).pipe(
      map( resp => {
        this.guardarToken( resp['token'] );
        this.guardarRol( resp['rol'] );
        return resp;
      })
    );
  }

  private guardarToken( idToken: string){
    this.userToken = idToken;
    localStorage.setItem('token',idToken);
  }

  leerToken(  ){
    if( localStorage.getItem('token') ){
      this.userToken = localStorage.getItem('token');
    }else{
      this.userToken = ''; 
    }
  }

  private guardarRol( rol: string){
    localStorage.setItem('rol',rol);
  }
}
