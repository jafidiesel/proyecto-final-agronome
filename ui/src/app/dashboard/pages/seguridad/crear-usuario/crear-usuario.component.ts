import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Subscription, Observable } from 'rxjs';
import { formatDate } from "@angular/common";
import { SeguridadService } from 'src/app/dashboard/services/seguridad.service';
import { FincaService } from 'src/app/dashboard/services/finca.service';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-crear-usuario',
  templateUrl: './crear-usuario.component.html'
})
export class CrearUsuarioComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  faTrashAlt = faTrashAlt;

  formUsuario: FormGroup;

  // Lista con opciones
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

  format = 'dd-MM-yyyy';
  myDate = new Date();
  locale = 'en-US';
  formattedDate = formatDate(this.myDate, this.format, this.locale);


  constructor(
    private _seguridadService: SeguridadService,
    private _fincaService: FincaService,
    private fb: FormBuilder) { }

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

  checkUsuario() {
    if(this.formUsuario.value.usuario.usuario != null){
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
    if(this.formUsuario.value.usuario.email  != null){
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
    if(this.formUsuario.value.usuario.contraseniaUsuario != null){
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

  


  initForm() {
    this.formUsuario = this.fb.group({
      usuario: this.fb.group({
        usuario: [null, Validators.required],
        nombre: [null, Validators.required],
        apellido: [null, Validators.required],
        email: [null, [Validators.required, Validators.email]],
        contraseniaUsuario: [null, Validators.required],
        fchCrea: [this.formattedDate]
      }),
      rol: this.fb.group({
        cod: [this.rolSeleccionado.cod]
      }),
      fincas: [this.fb.control({
        codFinca: null,
        nombre: ""
      })]
    });

  }

  onSubmitUsuario() {
    this.updateFincas();

    if (this.formUsuario.status == 'VALID') {
      this._seguridadService.postUsuario(this.formUsuario.value).subscribe(
        (result: any) => {
          this.postSuccess = true;
          this.postError = false;
          this.postErrorMessage = '';
          this.postSuccessMessage = result.message;

        },
        error => this.onHttpError({ message: error.error.message })
      );
    } else {
      this.postError = true;
      this.postErrorMessage = "Ingrese todos los campos obligatorios.";
    }
  }

  crearFinca(obj: any) {
    debugger;
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
    console.log('this.fincaSeleccionada', this.fincaSeleccionada);

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
    debugger;
    console.log('agregarItem()', this.fincaSeleccionada);
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

  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
