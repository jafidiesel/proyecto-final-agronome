import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable } from 'rxjs';
import { NgForm, NgModel } from '@angular/forms';

@Component({
  selector: 'app-crear-parametro',
  templateUrl: './crear-parametro.component.html'
})
export class CrearParametroComponent implements OnInit {

  tiposOpcionesSelect: Observable<Object>;
  optionsList = [];

  // Dropdown tipoParametro
  tiposParametrosSelect: Observable<Object>;
  tiposParametrosSelectArray =[];

  // Dropdown tipoDatp
  tiposDatosSelect: Observable<Object>;
  tiposDatosSelectArray =[];

  // json a enviar para POST
  parametroAEnviar: any = {
    parametro: {
      nombre: "",
      isActiv: false,
    },
    tipoParametro: {
      id: 0
    },
    tipoDato:{
      id: 0
    },
    opcion: []
  };

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor( private _configuracionService: ConfiguracionService ) {
  }

  ngOnInit() {
     this._configuracionService.getListaNomencladores('tipoParametro').subscribe(
      result => {
        for (let index = 0; index < result.length; index++) {
          const element:any = result[index];
          this.tiposParametrosSelectArray.push(element);
          
        }
      }
    );

    this._configuracionService.getListaNomencladores('tipoDato').subscribe(
      result => {
        for (let index = 0; index < result.length; index++) {
          const element:any = result[index];
          this.tiposDatosSelectArray.push(element);
          
        }
      }
    );

    this.tiposOpcionesSelect = this._configuracionService.getListaNomencladores('opcion');  
  }

  imprimir(){
    //console.log(this.optionsList);
  }
  
  onBlur(field: NgModel) {
    console.log("In onBlur: " + field.valid);
  }
  
  onHttpError( errorResponse: any ) {
    console.log(errorResponse);
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.error.messages
  }

  onSubmitParametro(form: NgForm) {
    this.parametroAEnviar.opcion = [];
    this.optionsList.forEach(element => {
      this.parametroAEnviar.opcion.push({'id': element});
    });

    if ( form.controls.tipoParametro.value && form.controls.nombre.value ) {
      this._configuracionService.postParametroForm(this.parametroAEnviar).subscribe(
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
    }
  }
  resetForm() {
    //this.nomencladorAEnviar.nombre = '';
    //this.nomencladorAEnviar.isActiv = false;
    //this.nomencladorAEnviar.tipoNomenclador = '';
  }
}
