import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Subscription } from 'rxjs';
import { formatDate } from "@angular/common";
import { SeguridadService } from 'src/app/dashboard/services/seguridad.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

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

  format = 'yyyy-MM-dd';
  myDate = new Date();
  locale = 'en-US';
  formattedDate = formatDate(this.myDate, this.format, this.locale);


  constructor(private _seguridadService: SeguridadService,
    private fb: FormBuilder) { }

  /*   
    {
  "usuario": {
    "usuario": "usuario",
    "nombre": "nombre",
    "apellido": "adaaf",
    "email": "dffsgafa@gmail.com",
    "contraseniaUsuario": "123456",
    "fchCrea" : "12/03/1990",
    "isActiv": true
  },
  
  "rol":{
    "cod": 1
  }
}
 */

  ngOnInit() {
    this.initForm();
    this.subscriptions.push(
      this._seguridadService.getListaNomencladoresConFiltro('rol', true).subscribe(
        (result: any) => {
          for (let index = 0; index < result.length; index++) {
            this.rolesSelectArray.push(result[index]);
          }
        }
      )
    );
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
        usuario: [null, Validators.required],
        nombre: [null, Validators.required],
        apellido: [null, Validators.required],
        email: [null, [Validators.required, Validators.email]],
        contraseniaUsuario: [null, [Validators.required, Validators.minLength(6)]],
        isActiv: [false],
        fchCrea: [this.formattedDate]
      }),
      rol: this.fb.group({
        cod: [this.rolSeleccionado.cod]
      })
    });

  }

  onSubmitUsuario() {
    console.warn(this.formUsuario.value);

    if (this.formUsuario.status == 'VALID') {
      this._seguridadService.postUsuario(this.formUsuario.value).subscribe(
        result => {
          this.postSuccess = true;
          this.postError = false;
          this.postErrorMessage = '';


        },
        error => this.onHttpError(error)
      );
    } else {
      this.postError = true;
      this.postErrorMessage = "Ingrese todos los campos obligatorios.";
    }
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
