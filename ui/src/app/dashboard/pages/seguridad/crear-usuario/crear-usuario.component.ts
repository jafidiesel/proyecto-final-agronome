import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Subscription } from 'rxjs';
import { formatDate } from "@angular/common";

@Component({
  selector: 'app-crear-usuario',
  templateUrl: './crear-usuario.component.html'
})
export class CrearUsuarioComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  formUsuario: FormGroup;

  rolesSelectArray = [];
  rolSeleccionado = {
    cod: null,
    nombre: null
  };

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  format = 'dd/MM/yyyy';
  myDate = new Date();
  locale = 'en-US';
  formattedDate = formatDate(this.myDate, this.format, this.locale);


  constructor(private _configuracionService: ConfiguracionService,
    private fb: FormBuilder) { }

  /*   {
      "usuario": {
        "nombre": "usuario1",
        "email": "",
        "contraseniaUsuario": "",
        "fchCrea" = "",
      },
      
      "rol":{
        "cod": "",
      }
    } */

  ngOnInit() {
    this.initForm();
    this.subscriptions.push(this._configuracionService.getListaNomencladoresConFiltro('rol', true).subscribe(
      (result: any) => {
        for (let index = 0; index < result.length; index++) {
          this.rolesSelectArray.push(result[index]);
        }
      }
    ));
  }

  actualizarRolSeleccionado(event) {
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const inn = selectEl.options[selectEl.selectedIndex].innerText;

    this.rolSeleccionado.cod = attrVal;
    this.rolSeleccionado.nombre = inn;

  }

  initForm() {
    this.formUsuario = this.fb.group({
      usuario: this.fb.group({
        nombre: [null, Validators.required],
        email: [null, [Validators.required,Validators.email] ],
        contraseniaUsuario: [null, [Validators.required,  Validators.minLength(6)] ],
        fechaCrea: [this.formattedDate ]
      }),
      rol: this.fb.group({
        cod: [this.rolSeleccionado.cod]
      })
    });

  }

  imprimir(){
    console.log('formUsuario',this.formUsuario);
  }

  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
