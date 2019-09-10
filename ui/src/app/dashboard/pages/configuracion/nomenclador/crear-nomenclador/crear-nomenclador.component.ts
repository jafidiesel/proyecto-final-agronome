import { Component, OnInit, NgModule } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NgForm, NgModel } from '@angular/forms';
import { NomencladorInterface } from '../../../../data/nomenclador';
import { ConfiguracionService } from '../../../../services/configuracion/configuracion.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-crear-nomenclador',
  templateUrl: './crear-nomenclador.component.html'
})
export class CrearNomencladorComponent implements OnInit {
  nombre: string;
  tipoNomenclador: string;
  isActiv: boolean;

  postError = false;
  postErrorMessage = '';

  tiposNomencladoresSelect: Observable<string[]>;

  nomencladorAEnviar: NomencladorInterface = {
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
          console.log('Enviado.');
          console.log( result);
        },
        error => this.onHttpError(error)
      );
    } else {
      this.postError = true;
      this.postErrorMessage = 'Por favor complete los campos del formulario.';
    }
  }

  onBlur(field: NgModel) {
    console.log("In onBlur: " + field.valid);
  }
  


}
