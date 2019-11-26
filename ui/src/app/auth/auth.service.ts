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
        this.guardarFinca(resp['finca'], fincaLength, resp['rol']);



        return resp;
      })
    );
  }

  private guardarToken(idToken: string) {
    this.userToken = idToken;
    localStorage.setItem('token', idToken);
  }

  leerToken() {
    if (localStorage.getItem('token')) {
      this.userToken = localStorage.getItem('token');
    } else {
      this.userToken = '';
    }
  }

  private guardarRol(rol: string) {
    localStorage.setItem('rol', rol);
  }

  private guardarNombre(nombre: string) {
    localStorage.setItem('nombre', nombre);
  }

  guardarFinca(arrayFinca: any, cantFincas: number, rol: string) {
    localStorage.setItem('cantFincas', cantFincas.toString());
    if (rol == 'ingeniero') {
      localStorage.setItem('fincas', JSON.stringify(arrayFinca));
    } else if (rol == 'administrador') {
      localStorage.setItem('fincas', "0")
    } else {
      localStorage.removeItem('fincas');
      localStorage.setItem('fincas', JSON.stringify(arrayFinca[0]));
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

  getNombreFinca() {
    if (localStorage.getItem('fincas') != "undefined") {
      let obj: any;
      obj = JSON.parse(localStorage.getItem('fincas'));
      return obj.nombreFinca;
    }else{
      return "";
    }
  }

  getcodFinca(): number {
    if (localStorage.getItem('fincas') != "undefined") {
      let obj: any;
      obj = JSON.parse(localStorage.getItem('fincas'));
      return obj.codFinca;
    }
  }



}
