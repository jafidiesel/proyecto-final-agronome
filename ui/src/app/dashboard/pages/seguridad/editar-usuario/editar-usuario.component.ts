import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { Subscription, Observable } from 'rxjs';
import { SeguridadService } from 'src/app/dashboard/services/seguridad.service';
import { ActivatedRoute } from '@angular/router';
import { FincaService } from 'src/app/dashboard/services/finca.service';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-editar-usuario',
  templateUrl: './editar-usuario.component.html'
})
export class EditarUsuarioComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  formUsuario: FormGroup;
  faTrashAlt = faTrashAlt;


  codUsuario: string;

  // Lista con fincas
  tiposFincasSelect: Observable<Object>;
  tiposFincasSelectArray = [];
  fincasElegidas = [];
  fincaSeleccionada = {
    codFinca: null,
    nombre: null
  };

  rolesSelectArray = [];
  rolSeleccionado = {
    cod: null,
    nombre: null
  };

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';
  postSuccessMessage = '';

  constructor(
    private activatedRoute: ActivatedRoute, private _seguridadService: SeguridadService,
    private _fincaService: FincaService,
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
            error => this.onHttpError({ message: error.error.message })
          )
        )
      })
    );

    this.subscriptions.push(
      this._fincaService.getFincas().subscribe(
        result => {
          for (let index = 0; index < result.finca.length; index++) {
            const element = result.finca[index];
            this.tiposFincasSelectArray.push(element);
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

  initForm(form) {

    this.formUsuario = this.fb.group({
      usuario: this.fb.group({
        usuario: [form.usuario, Validators.required],
        nombre: [form.nombre, Validators.required],
        apellido: [form.apellido, Validators.required],
        email: [form.email, [Validators.required, Validators.email]],
        contraseniaUsuario: [null, [Validators.required, Validators.minLength(6)]],
        cod: [form.cod]
      }),
      rol: this.fb.group({
        cod: [parseInt(form.rol.cod)]
      }),
      fincas: [this.fb.control({
        codFinca: null,
        nombre: ""
      })]
    });

  }


  checkUsuario() {
    if (this.formUsuario.value.usuario.usuario != null) {
      this.subscriptions.push(
        this._seguridadService.checkUsername(this.formUsuario.value.usuario.usuario).subscribe(
          result => {
            this.postError = false;
            this.postSuccess = false;
            this.postErrorMessage = "";
          },
          error => this.onHttpError({ message: error.error.message })
        )
      );

    }
  }

  checkEmail() {
    if (this.formUsuario.value.usuario.email != null) {
      this.subscriptions.push(
        this._seguridadService.checkEmail(this.formUsuario.value.usuario.email).subscribe(
          result => {
            this.postError = false;
            this.postSuccess = false;
            this.postErrorMessage = "";
          },
          error => this.onHttpError({ message: error.error.message })
        )
      );
    }
  }

  checkContraseniaUsuario() {
    if (this.formUsuario.value.usuario.contraseniaUsuario != null) {
      this.subscriptions.push(
        this._seguridadService.checkContraseniaUsuario(this.formUsuario.value.usuario.contraseniaUsuario).subscribe(
          result => {
            this.postError = false;
            this.postSuccess = false;
            this.postErrorMessage = "";
          },
          error => this.onHttpError({ message: error.error.message })
        )
      );
    }
  }

  crearFinca(obj: any) {
    return this.fb.control({
      codFinca: obj.codFinca,
      nombre: obj.nombre,
    });
  }

  actualizarFincaSeleccionada(event) {
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const inn = selectEl.options[selectEl.selectedIndex].innerText;
    this.fincaSeleccionada.codFinca = attrVal;
    this.fincaSeleccionada.nombre = inn;
  }

  updateFincas() {
    this.formUsuario.patchValue({
      fincas: this.fb.array(
        this.fincasElegidas.map(
          element => this.crearFinca(element)
        )
      ).value
    });
  }

  agregarItem() {
    this.fincasElegidas.push({
      codFinca: this.fincaSeleccionada.codFinca,
      nombre: this.fincaSeleccionada.nombre
    });
  }

  quitarItem(itemARemover) {
    this.fincasElegidas.forEach((item, index) => {
      if (item === itemARemover) {
        this.fincasElegidas.splice(index, 1);
      }
    });
  }


  onSubmitUsuario() {
    this.updateFincas();

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
