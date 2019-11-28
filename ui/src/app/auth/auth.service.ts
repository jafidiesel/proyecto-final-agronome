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

  constructor(private http: HttpClient) {
    this.leerToken();
  }

  login(usuario: UsuarioModel) {
    return this.http.post(this.url, usuario).pipe(
      map(resp => {
        this.guardarToken(resp['token']);
        this.guardarRol(resp['rol']);
        this.guardarNombre(resp['nombre']);

        let fincaLength = (resp['finca'] != null) ? resp['finca'].length : 0;
        this.guardarFincas(resp['finca'], fincaLength, resp['rol']);



        return resp;
      })
    );
  }

  logoutLocalStorage() {
    localStorage.removeItem('rol');
    localStorage.removeItem('token');
    localStorage.removeItem('nombre');
    localStorage.removeItem('cantFincas');
    localStorage.removeItem('fincas');
    localStorage.removeItem('currentCodFinca');
    localStorage.removeItem('currentNombreFinca');
  }

  private guardarToken(idToken: string) {
    this.userToken = idToken;
    localStorage.setItem('token', idToken);
  }


  private guardarRol(rol: string) {
    localStorage.setItem('rol', rol);
  }

  private guardarNombre(nombre: string) {
    localStorage.setItem('nombre', nombre);
  }

  guardarFincas(arrayFinca: any, cantFincas: number, rol: string) {
    localStorage.setItem('cantFincas', cantFincas.toString());
    if (rol == 'ingeniero') {
      localStorage.setItem('fincas', JSON.stringify(arrayFinca));
    } else if (rol == 'administrador') {
      localStorage.setItem('fincas', "0")
    } else {
      localStorage.removeItem('fincas');
      localStorage.setItem('fincas', JSON.stringify(arrayFinca));
    }

  }

  setearFinca(codFinca: number, nombreFinca: string) {
    localStorage.setItem('currentCodFinca', String(codFinca));
    localStorage.setItem('currentNombreFinca', nombreFinca);
  }

  leerToken() {
    if (localStorage.getItem('token')) {
      this.userToken = localStorage.getItem('token');
    } else {
      this.userToken = '';
    }
  }
  
  
  getToken() {
    if (localStorage.getItem('token')) {
      return localStorage.getItem('token');
    }
  }
  
  getRol() {
    if (localStorage.getItem('rol')) {
      return localStorage.getItem('rol');
    }
  }
  
  getNombre() {
    if (localStorage.getItem('nombre')) {
      return localStorage.getItem('nombre');
    }
  }
  
  getNombresFinca() {
    if (localStorage.getItem('fincas') != "undefined") {
      let array = [];
      let result = [];
      array = JSON.parse(localStorage.getItem('fincas'));
      if (array.length > 0) {
        array.map(finca => {
          result.push(finca.nombreFinca);
        });
        return result;
      } else {
        return [];
      }
    } else {
      return [];
    }
  }
  
  getcodFinca() {
    if (localStorage.getItem('fincas') != "undefined") {
      let array = [];
      let result = [];
      array = JSON.parse(localStorage.getItem('fincas'));
      if (array.length > 0) {
        array.map(finca => result.push(finca.codFinca));
      }
      return result;
    }
  }
  
  getFincas() {
    if (localStorage.getItem('fincas') != "undefined") {
      return JSON.parse(localStorage.getItem('fincas'));
    }
  }
  
  getCurrentNombreFinca(){
    let result = localStorage.getItem('currentNombreFinca') == null ? "" : localStorage.getItem('currentNombreFinca');
    return result;
  }
  
  getCurrentCodFinca(){
    let result = localStorage.getItem('currentcodFinca') == null ? "" : localStorage.getItem('currentCodFinca');
    return result;
  }
  
}
