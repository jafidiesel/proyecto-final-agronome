import { Component, OnInit, OnDestroy } from '@angular/core';
import { NgForm, NgModel } from '@angular/forms';
import { NomencladorInterface } from '../../../../data/nomenclador';
import { ConfiguracionService } from '../../../../services/configuracion/configuracion.service';
import { Subscription, Observable } from 'rxjs';



@Component({
  selector: 'app-crear-nomenclador',
  templateUrl: './crear-nomenclador.component.html'
})
export class CrearNomencladorComponent implements OnInit, OnDestroy {
  
  subscriptions : Subscription[] = [];
  
  nombre: string;
  tipoNomenclador: string;
  isActiv = false;

  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  tiposNomencladoresSelect: Observable<String[][]>;

  nomencladorAEnviar: NomencladorInterface = {
    nombre: this.nombre,
    tipoNomenclador: this.tipoNomenclador,
    isActiv: this.isActiv
  };

  constructor( private _configuracionService: ConfiguracionService) {
    
  }
  
  ngOnInit() {
    this.tiposNomencladoresSelect = this._configuracionService.getTiposNomenclador();
  }

  onHttpError( errorResponse: any ) {
    console.log(errorResponse);
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.error.messages
  }

  onSubmitNomenclador(form: NgForm) {

    if ( form.controls.tipoNomenclador.value && form.controls.nombre.value ) {
      this.subscriptions.push(this._configuracionService.postNomencladorForm(this.nomencladorAEnviar).subscribe(
        result => {
          console.log('Enviado.');
          this.postSuccess = true;
          this.postError = false;
          this.resetForm();
        },
        error => this.onHttpError(error)
      ));
    } else {
      this.postError = true;
      this.postErrorMessage = 'Por favor complete correctamente los campos obligatorios del formulario.';
    }
  }

  onBlur(field: NgModel) {
    console.log("In onBlur: " + field.valid);
  }

  resetForm() {
    this.nomencladorAEnviar.nombre = '';
    this.nomencladorAEnviar.isActiv = false;
    this.nomencladorAEnviar.tipoNomenclador = '';
  }
  
  ngOnDestroy(){
    this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
  }

}
