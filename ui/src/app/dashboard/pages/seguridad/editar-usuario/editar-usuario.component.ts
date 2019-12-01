import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { Subscription } from 'rxjs';
import { SeguridadService } from 'src/app/dashboard/services/seguridad.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-editar-usuario',
  templateUrl: './editar-usuario.component.html'
})
export class EditarUsuarioComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  formUsuario: FormGroup;

  codUsuario: string;

  rolesSelectArray = [];
  rolSeleccionado = {
    cod: null,
    nombre: null
  };

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private activatedRoute: ActivatedRoute, private _seguridadService: SeguridadService,
    private fb: FormBuilder) { }

  ngOnInit() {

    // Obtener los nomencladores del combo Rol

    this.subscriptions.push(
      this._seguridadService.getListaNomencladoresConFiltro('rol', true).subscribe(
        (result: any) => {
          for (let index = 0; index < result.length; index++) {
            this.rolesSelectArray.push(result[index]);
          }
        }
      )
    );

    // Obtener los datos del usuario
    this.subscriptions.push(
      this.activatedRoute.params.subscribe(params => {
        this.codUsuario = params['cod'];

        this.subscriptions.push(
          this._seguridadService.getUsuario(params['cod']).subscribe(
            result => {
              this.initForm(result);
            },
            error => this.onHttpError({ message: "Error message" })
          )
        )
      })
    );

  }

  actualizarRolSeleccionado(event) {
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const inn = selectEl.options[selectEl.selectedIndex].innerText;

    this.rolSeleccionado.cod = attrVal;
    this.rolSeleccionado.nombre = inn;

  }

  initForm(form) {

    this.formUsuario = this.fb.group({
      usuario: this.fb.group({
        usuario: [form.usuario, Validators.required],
        nombre: [form.nombre, Validators.required],
        apellido: [form.apellido, Validators.required],
        email: [form.email, [Validators.required, Validators.email]],
        contraseniaUsuario: [null, [Validators.required, Validators.minLength(6)]],
        cod: [ form.cod ]
      }),
      rol: this.fb.group({
        cod: [ parseInt(form.rol.cod) ]
      })
    });

  }

  onSubmitUsuario() {
    if (this.formUsuario.status == 'VALID') {
      this._seguridadService.putUsuario(this.codUsuario, this.formUsuario.value).subscribe(
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
