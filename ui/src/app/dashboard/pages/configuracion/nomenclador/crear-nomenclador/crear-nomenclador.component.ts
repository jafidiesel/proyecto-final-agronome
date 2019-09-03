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

  constructor( private http: HttpClient ) {
    const headers = new HttpHeaders()
    .set("Content-Type", "application/json");
    console.log(headers);

    // http://127.0.0.1:4000/api/configuracion/nomenclador/1
    this.http.get('https://restcountries.eu/rest/v2/lang/es' )
        .subscribe( Response => {
          console.log(Response);
        } );
   }

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
}
