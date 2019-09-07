import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-crear-nomenclador',
  templateUrl: './crear-nomenclador.component.html'
})
export class CrearNomencladorComponent implements OnInit {
  nombre: string;
  tipoNomenclador: boolean;
  isActiv: string;
  obj: any[];

  constructor(private http: HttpClient) {}

  ngOnInit() {
  }

  imprimir( ) {
    let myobj = {
      nombre: this.nombre,
      tipoNomenclador: this.tipoNomenclador,
      isActiv: this.isActiv
    };

    console.log( JSON.stringify( myobj ) );

  }

  crearNomenclador(){
    let httpHeaders = new HttpHeaders()
     .set('Content-Type', 'application/json');


    let options = {
      headers: httpHeaders
    };
    
    // http://localhost:7000/api/configuracion/nomenclador
    let url = 'http://localhost:9001/api/configuracion/nomenclador';

    let myobj = {
      nameInput: this.nameInput,
      tipoNomencladorInput: this.tipoNomencladorInput,
      activoInput: this.activoInput
    };

    let objDummy = {
      "tipoNomenclador": "opcion",
      "nombre": "123123qas33323213asdased3d",
      "isActiv": true
    };

    this.http.post(
        url,
        obj2,
        options
        ).subscribe( (res: any)  => {
          console.log(res);
          console.log(res.data.nameInput);
        },
        err => {
          console.log(err.status);
          }
        );

  }

  getNomenclador (  ) {
    let httpHeaders = new HttpHeaders()
      .set('Content-Type', 'application/json');
    let options = {
      headers: httpHeaders
    };
    let url = 'http://localhost:9001/api/configuracion/nomenclador/1';

    this.http.get(
      url,
      options
      ).subscribe( (res: any)  => {
        console.log(res);
        console.log("nombre" + res.data.nombre);
        console.log("tipoNomenclador" + res.data.tipoNomenclador);
        console.log("isActiv" + res.data.isActiv);
      },
      err => {
        console.log("get -> "+ url)
        console.error("error code: " + err.status + "  " + err.error.message);
        }
      );
  }
  
  postNomenclador (  ) {
    let httpHeaders = new HttpHeaders()
    .set('Content-Type', 'application/json');
    let options = {
      headers: httpHeaders
    };
    let url = 'http://localhost:9001/api/configuracion/nomenclador';
    let obj2 = {
      "tipoNomenclador": "opcion",
      "nombre": "dummyObjectOpcion" + Math.floor(Math.random()*10),
      "isActiv": true
    };

    this.http.post(
      url,
      obj2,
      options
      ).subscribe( (res: any)  => {
        console.log(res);
      },
      err => {
        console.log("post -> "+ url)
        console.error("error code: " + err.status + "  " + err.error.message);
        }
      );
  }
}
