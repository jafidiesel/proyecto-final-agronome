import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable, Subscription } from 'rxjs';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';


@Component({
  selector: 'app-asociar-recomendacion',
  templateUrl: './asociar-recomendacion.component.html'
})
export class AsociarRecomendacionComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  asociarParametroForm: FormGroup;

  faTrashAlt = faTrashAlt;

  // Valores dropdown nomenclador
  listaNomencladoresRecomendacion: Observable<Object>;
  listaNomencladoresRecomendacionArray = [];

  // Lista con opciones
  tiposParametrosSelect: Observable<object>;
  tiposParametrosSelectArray = [];
  parametrosElegidos = [];
  parametroSeleccionado = {
    cod: null,
    nombre: null
  };

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private _configuracionService: ConfiguracionService,
    private fb: FormBuilder) {
  }

  ngOnInit() {
    this.initForm();

    this.subscriptions.push(this._configuracionService.getListaAsociacion('recomendacionParametro').subscribe(
      result => {

        for (let index = 0; index < result.sinAsociaciones.length; index++) {
          const element = result.sinAsociaciones[index];
          this.listaNomencladoresRecomendacionArray.push(element);

        }
      }
    ));

    this.subscriptions.push(this._configuracionService.getListaParametrosPorTipo('recomendacion').subscribe(
      (result: any) => {
        for (let index = 0; index < result.length; index++) {
          this.tiposParametrosSelectArray.push(result[index]);
        }
      }
    ));

  }

  initForm() {

    this.asociarParametroForm = this.fb.group({
      entidadIntermedia: ['recomendacionParametro'],
      cod: [null, Validators.required], // cod nomenclador actividad
      parametros: this.fb.group({
        cod: [null, Validators.required]
      }),
    });
  }

  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  actualizarNomencladorActividad(event) {
    // This is ducktape, do not usit at home
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    this.asociarParametroForm.patchValue({
      cod: attrVal
    });

  }

  actualizarParametroSeleccionado(event) {
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const inn = selectEl.options[selectEl.selectedIndex].innerText;

    this.parametroSeleccionado.cod = attrVal;
    this.parametroSeleccionado.nombre = inn;

  }

  updateParametros() {
    this.asociarParametroForm.patchValue({
      parametros: {
        cod: "[" + this.parametrosElegidos.map(element => { return element.cod }) + "]"
      }
    });

  }

  agregarItem() {
    let obj = {
      cod: this.parametroSeleccionado.cod,
      nombre: this.parametroSeleccionado.nombre
    }
    this.parametrosElegidos.push(obj);

    this.updateParametros();

  }

  quitarItem(itemARemover) {
    this.parametrosElegidos.forEach((item, index) => {
      if (item === itemARemover) {
        this.parametrosElegidos.splice(index, 1);
      }
    });
  }

  onSubmitAsociacion() {
    this.updateParametros();

    if (this.asociarParametroForm.status == 'VALID') {
      this._configuracionService.postAsociacionForm(this.asociarParametroForm.value).subscribe(
        result => {
          this.postSuccess = true;

          this.asociarParametroForm.controls['cod'].disable();
        },
        error => this.onHttpError(error)
      );
    } else {
      this.postError = true;
      this.postSuccess = false;
      this.postErrorMessage = 'Por favor complete correctamente los campos obligatorios del formulario.';
    }
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
