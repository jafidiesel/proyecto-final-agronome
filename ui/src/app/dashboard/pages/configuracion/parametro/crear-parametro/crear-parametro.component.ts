import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable, Subscription } from 'rxjs';
import { NgForm, NgModel, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-crear-parametro',
  templateUrl: './crear-parametro.component.html'
})
export class CrearParametroComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  crearParametroForm: FormGroup;

  faTrashAlt = faTrashAlt;

  // json a enviar para POST
  originalParametroAEnviar: any = {
    parametro: {
      nombre: "",
      isActiv: false,
    },
    tipoParametro: {
      cod: 0
    },
    tipoDato: {
      cod: 0
    },
    opcion: []
  };

  // Dropdown tipoParametro
  tiposParametrosSelect: Observable<Object>;
  tiposParametrosSelectArray = [];

  // Dropdown tipoDato
  tiposDatosSelect: Observable<Object>;
  tiposDatosSelectArray = [];

  // Lista con opciones
  tiposOpcionesSelect: Observable<Object>;
  tiposOpcionesSelectArray = [];
  opcionesElegidas = [];
  opcionSeleccionada = {
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
    this.subscriptions.push(this._configuracionService.getListaNomencladores('tipoParametro').subscribe(
      result => {
        for (let index = 0; index < result.length; index++) {
          const element: any = result[index];
          this.tiposParametrosSelectArray.push(element);

        }
      }
    ));

    this.subscriptions.push(this._configuracionService.getListaNomencladoresConFiltro('tipoDato', true).subscribe(
      result => {
        for (let index = 0; index < result.length; index++) {
          const element: any = result[index];
          this.tiposDatosSelectArray.push(element);

        }
      }
    ));

    this.subscriptions.push(
      this._configuracionService.getListaNomencladoresConFiltro('opcion', true).subscribe(
        result => {
          for (let index = 0; index < result.length; index++) {
            const element = result[index];
            this.tiposOpcionesSelectArray.push(element);
  
          }
        }
      )
    );

  }

  onBlur(field: NgModel) {
    console.log("In onBlur: " + field.valid);
  }



  onSubmitParametro(form: NgForm) {
    console.warn(this.crearParametroForm.value);
    this.updateOpciones();

    if (this.crearParametroForm.status == 'VALID') {
      this._configuracionService.postParametroForm(this.crearParametroForm.value).subscribe(
        result => {
          this.postSuccess = true;
          this.postError = false;
          this.postErrorMessage = '';

        },
        error => this.onHttpError(error)
      );
    } else {
      // [disabled]="!crearParametroForm.valid"
      this.postError = true;
      this.postErrorMessage = "Ingrese todos los campos obligatorios.";
    }
  }


  initForm() {

    this.crearParametroForm = this.fb.group({
      parametro: this.fb.group({
        nombre: ['', Validators.required],
        isActiv: [false],
      }),
      tipoParametro: this.fb.group({
        cod: [null, Validators.required],
        nombre: [''],
        isActiv: [false],
      }),
      tipoDato: this.fb.group({
        cod: [null, Validators.required],
        nombre: [''],
        isActiv: [false],
      }),
      opcion: [this.fb.control({
        cod: null,
        nombre: "",
        isActiv: false
      })]

    });
  }


  crearOpcion(obj: any) {
    return this.fb.control({
      cod: obj.cod,
      nombre: obj.nombre,
    })
      ;
  }

  actualizaropcionSeleccionada(event) {
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const inn = selectEl.options[selectEl.selectedIndex].innerText;
    this.opcionSeleccionada.cod = attrVal;
    this.opcionSeleccionada.nombre = inn;

  }

  updateOpciones() {
    this.crearParametroForm.patchValue({
      opcion: this.fb.array(this.opcionesElegidas.map(element => this.crearOpcion(element))).value
    });
  }

  agregarItem() {
    this.opcionesElegidas.push({
      cod: this.opcionSeleccionada.cod,
      nombre: this.opcionSeleccionada.nombre
    });
  }

  quitarItem(itemARemover) {
    this.opcionesElegidas.forEach((item, index) => {
      if (item === itemARemover) {
        this.opcionesElegidas.splice(index, 1);
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
