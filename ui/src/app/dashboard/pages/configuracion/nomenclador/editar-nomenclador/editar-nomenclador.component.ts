import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable } from 'rxjs';
import { NgForm, NgModel } from '@angular/forms';

@Component({
  selector: 'app-editar-nomenclador',
  templateUrl: './editar-nomenclador.component.html'
})
export class EditarNomencladorComponent implements OnInit {

  originalNomencladorAcargar = {
    id: -1,
    nombre: '',
    tipoNomenclador: -1,
    isActiv: false
  };

  nomencladorAcargar ={};

  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  tiposNomencladoresSelect: Observable<string[]>;

  constructor(private activatedRoute: ActivatedRoute,
    private _configuracionService: ConfiguracionService) {
      this.activatedRoute.params.subscribe( params => {
        this._configuracionService.getNomenclador(params['tipoNomenclador'] , params['id'] ).subscribe(
          (result: any) => {
            console.log(params['tipoNomenclador'] + params['id'] );
            console.log(result);
            this.originalNomencladorAcargar.nombre = result.nombre;
            this.originalNomencladorAcargar.isActiv = result.isActiv;
            this.originalNomencladorAcargar.tipoNomenclador = result.tipoNomenclador;
            this.nomencladorAcargar = { ...this.originalNomencladorAcargar };
          },
        error => console.log(error)
        );
        
      } );
      
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
  
      /* if ( form.controls.tipoNomenclador.value && form.controls.nombre.value ) {
        this._configuracionService.postNomencladorForm(this.nomencladorAEnviar).subscribe(
          result => {
            console.log('Enviado.');
            this.postSuccess = true;
            this.resetForm();
          },
          error => this.onHttpError(error)
        );
      } else {
        this.postError = true;
        this.postErrorMessage = 'Por favor complete correctamente los campos obligatorios del formulario.';
      } */
    }
  
    onBlur(field: NgModel) {
      console.log("In onBlur: " + field.valid);
    }
}
