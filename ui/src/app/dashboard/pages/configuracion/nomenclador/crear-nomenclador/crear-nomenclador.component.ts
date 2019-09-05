import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-crear-nomenclador',
  templateUrl: './crear-nomenclador.component.html'
})
export class CrearNomencladorComponent implements OnInit {
  nameInput: string;
  activoInput: boolean;
  tipoNomencladorInput: string;
  obj: any[];

  constructor(private http: HttpClient) {}

  ngOnInit() {
  }

  imprimir( ) {
    let myobj = {
      nameInput: this.nameInput,
      tipoNomencladorInput: this.tipoNomencladorInput,
      activoInput: this.activoInput
    };

    console.log( JSON.stringify( myobj ) );

  }

  crearNomenclador(){
    let httpHeaders = new HttpHeaders()
     .set('Content-Type', 'application/json');


    let options = {
      headers: httpHeaders
    };

    let url = 'http://localhost:7000/api/configuracion/nomenclador';

    let myobj = {
      nameInput: this.nameInput,
      tipoNomencladorInput: this.tipoNomencladorInput,
      activoInput: this.activoInput
    };

    this.http.post(
        url,
        myobj,
        options
        ).subscribe( (res: any)  => {
          console.log(res);
          console.log(res.data.nameInput);
          $('#alerta').popover('show');
        },
        err => {
          console.log(err.status);
          }
        );

  }
}
