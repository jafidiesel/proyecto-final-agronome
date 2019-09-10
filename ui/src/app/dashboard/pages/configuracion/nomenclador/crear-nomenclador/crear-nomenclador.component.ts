import { Component, OnInit, NgModule } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NgForm, NgModel } from '@angular/forms';
import { Nomenclador } from '../../../../data/nomenclador';
import { ConfiguracionService } from '../../../../services/configuracion/configuracion.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-crear-nomenclador',
  templateUrl: './crear-nomenclador.component.html'
})
export class CrearNomencladorComponent implements OnInit {
  nombre: string;
  tipoNomenclador: number;
  isActiv: boolean;

  postError = false;
  postErrorMessage = '';

  tiposNomencladoresSelect: Observable<string[]>;

  nomencladorAEnviar: Nomenclador = {
    nombre: this.nombre,
    tipoNomenclador: this.tipoNomenclador,
    isActiv: this.isActiv
  };

  constructor(private http: HttpClient, private configuracionService: ConfiguracionService) {}

  ngOnInit() {
    this.tiposNomencladoresSelect = this.configuracionService.getTipoNomenclador();
  }

  onHttpError( errorResponse: any ) {
    console.log(errorResponse);
    this.postError = true;
    this.postErrorMessage = errorResponse.error.errorMessage
  }

  onSubmitNomenclador(form: NgForm) {
    console.log('in onSubmitNomenclador ' + form.valid);

    if( form.valid ) {
      this.configuracionService.postNomencladorForm(this.nomencladorAEnviar).subscribe(
        result => {
          console.log('succes');
          console.log( result);
        },
        error => this.onHttpError(error)
      );
    } else {
      this.postError = true;
      this.postErrorMessage = 'Please check the form values';
    }
  }

  onBlur(field: NgModel) {
    console.log("In onBlur: " + field.valid);
  }

  imprimir( ) {
    // formCrearNomenclador
    console.log( JSON.stringify( this.nomencladorAEnviar ) );
  }


/*
  crearNomenclador(){
    let httpHeaders = new HttpHeaders()
     .set('Content-Type', 'application/json');


    let options = {
      headers: httpHeaders
    };

    // http://localhost:7000/api/configuracion/nomenclador
    let url = 'http://localhost:9001/api/configuracion/nomenclador';

    let myobj = {
      nameInput: this.nombre,
      tipoNomencladorInput: this.tipoNomenclador,
      activoInput: this.isActiv
    };

    let objDummy = {
      "tipoNomenclador": "opcion",
      "nombre": "123123qas33323213asdased3d",
      "isActiv": true
    };

    this.http.post(
        url,
        objDummy,
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
  } */
}
