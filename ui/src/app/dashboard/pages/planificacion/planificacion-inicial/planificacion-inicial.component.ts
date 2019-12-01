import { Component, OnInit, OnDestroy } from '@angular/core';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';
import { PlanificacionService } from 'src/app/dashboard/services/planificacion/planificacion.service';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Subscription } from 'rxjs';
import { AuthService } from 'src/app/auth/auth.service';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-planificacion-inicial',
  templateUrl: './planificacion-inicial.component.html'
})
export class PlanificacionInicialComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];
  codfinca: number;

  parcelas = [];

  dummyDataCultivo = [
    "Lechuga", "Tomate", "Zanahoria", "Calabaza", "Cebolla"
  ];

  // formgroup
  planificacionForm: FormGroup;

  tipoCultivoArray = [];

  tablaParcelaArray = []
  mostrarTablaParcelas = false;

  // banderas de error
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(
    private router: Router,
    private _planificacionService: PlanificacionService,
    private _configuracionService: ConfiguracionService,
    private fb: FormBuilder,
    private auth: AuthService
  ) { }

  ngOnInit() {
    //this.parcelaArray.push([ 'Parcela 1', '1,2,3' ]);
    this.mostrarTablaParcelas = true;

    this.codfinca = parseInt(this.auth.getCurrentCodFinca());

    this.subscriptions.push(
      this._configuracionService.getListaNomencladoresConFiltro('tipoCultivo', true).subscribe(
        (result: any) => {
          result.map(element => {
            this.tipoCultivoArray.push([element.cod, element.nombre])
          });
        },
        error => this.onHttpError({ message: error.error.message })
      )
    );

    this.subscriptions.push(
      this._planificacionService.getParcelasLibres(this.codfinca).subscribe(
        result => {
          result.parcelas.map(element => this.parcelas.push(element))
          this.initForm(result.parcelas);

        },
        error => this.onHttpError({ message: error.error.message })
      )
    );

  }

  crearParcela(obj: any) {
    return this.fb.control({
      codParcela: obj.codParcela,
      nombre: obj.nombre,
      cuadros: this.fb.array(obj.cuadros.map(cuadro => this.crearCuadro(cuadro).value))
    })
  }

  crearCuadro(obj: any) {
    return this.fb.control({
      codcuadro: obj.codCuadro,
      nombreCuadro: obj.nombreCuadro,
      isActive: false
    })
  }

  initForm(form) {
    this.planificacionForm = this.fb.group({
      action: "i",
      codPlanifBefore: null,
      codFinca: this.codfinca,
      comentario: null,
      cultivos: [{
        codTipoCultivo: 0,
        cantidadCultivo: 0,
        produccionEsperada: 0,
        variedadCultivo: "",
        cicloUnico: false,
        parcelas: this.fb.array(form.map(parcela => this.crearParcela(parcela).value))
      }]

      
    });
    
    this.imprimir();

    
  }
  
  imprimir(){
    console.warn(this.planificacionForm.value);

  }

  procesarOpciones(event) {

    debugger;
    const selectEl = event.target;
    const optionText = selectEl.options[selectEl.selectedIndex].innerText;

    this.planificacionForm.value.cultivos.codTipoCultivo = optionText;

  }


  async agregarCuadros() {

    this.mostrarTablaParcelas = false;
    const { value: formValues } = await Swal.fire({
      title: 'Seleccione los cuadros:',
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      backdrop: true,
      html:
        ` <h4>Parcela 1</h4>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1"> 1
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2"> 2
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 3
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2"> 4
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 5
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 6
              <span class="form-check-sign"></span>
            </label>
          </div>

          <h4>Parcela 2</h4>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1"> 1
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2"> 2
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 3
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 4
              <span class="form-check-sign"></span>
            </label>
          </div>
    `
      ,
      focusConfirm: false,
      confirmButtonText: 'Agregar',
      showCancelButton: true,
      cancelButtonText: 'Cancelar',
      reverseButtons: true,
      preConfirm: () => {
        // Aqui se debe realizar la validacion de todos los campos seleccionados
        this.tablaParcelaArray.push(['Parcela 1', '1,2,3']);
        this.tablaParcelaArray.push(['Parcela 2', '2,3,4']);
        this.mostrarTablaParcelas = true;

      }
    });
  }


  onSubmit() {
    this._planificacionService.guardarPlanificacion('inicial');
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
      },
      buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
      title: '¡Exito!',
      text: 'Se creo la planificación inicial correctamente.',
      type: 'success',
      confirmButtonText: 'Salir',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {
        this.router.navigate(['/planificacion/verPlanificacionInicial']);
      }
    });


  }

  // metodo custom para mostrar mensajes de error
  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }


}
