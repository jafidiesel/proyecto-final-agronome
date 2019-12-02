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
  codFinca: number;

  parcelas = [];
  parcelasToSend = [];

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

    this.codFinca = parseInt(this.auth.getCurrentCodFinca());

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
      this._planificacionService.getParcelasLibres(this.codFinca).subscribe(
        result => {
          result.parcelas.map(element => this.parcelas.push(element))
          this.initForm(result.parcelas);
          this.addIdsToCuadros(this.parcelas);

        },
        error => this.onHttpError({ message: error.error.message })
      )
    );

  }

  /* 
    crearCuadro(obj: any) {
      return this.fb.control({
        codcuadro: obj.codCuadro,
        nombreCuadro: obj.nombreCuadro,
        isActive: false
      })
    }
  
    crearParcela(obj: any) {
      return this.fb.control({
        codParcela: obj.codParcela,
        nombre: obj.nombre,
        cuadros: this.fb.array(obj.cuadros.map(cuadro => this.crearCuadro(cuadro).value))
      })
    }
  
    crearCultivo(obj: any) {
      return this.fb.control({
        codTipoCultivo: 0,
        variedadCultivo: "",
        cantidadCultivo: 0,
        produccionEsperada: 0,
        cicloUnico: false,
        parcelas: this.fb.array(obj.map(parcela => this.crearParcela(parcela).value))
      })
    } */

  addIdsToCuadros(parcelasArray) {
    let id = "cuadro-id-";
    let numero = 0;
    let resultArray = parcelasArray.map(parcela => {
      parcela.cuadros.map(cuadro => {
        cuadro.id = (id + numero);
        cuadro.isActive = false;
        numero++;
      });

    });
  }

  initForm(form) {
    this.planificacionForm = this.fb.group({
      action: "i",
      codPlanifBefore: null,
      codFinca: this.codFinca,
      comentario: null,
      codTipoCultivo: null,
      variedadCultivo: "",
      cantidadCultivo: 0,
      produccionEsperada: 0,
      cicloUnico: false,
      parcelas: [],
      cultivos: [{}]


    });

  }

  imprimir() {
    console.warn(this.planificacionForm.value);
  }
  imprimirParcelasToSend() {
    console.warn(this.parcelasToSend);
  }

  procesarInputs() {
    let nodeList: any;
    nodeList = document.querySelectorAll("input[id*=cuadro-id-]:checked");

    for (let index = 0; index < nodeList.length; index++) {
      const inputElement = nodeList[index];
      this.parcelasToSend = this.parcelas;
      this.parcelasToSend.map(parcela => {
        parcela.cuadros.map(cuadro => {
          if (cuadro.id == inputElement.id) {
            cuadro.isActive = true;
          }
        });
      });
    }
  }

  procesarParcelasToSend() {
    let jsonToSend = {};

    jsonToSend['parcelas'] = [];

    this.parcelasToSend.map(parcela => {
      let jsonParcela = {};
      parcela.cuadros.map(cuadro => {
        if (cuadro.isActive) {
          jsonParcela['codParcela'] = parcela.codParcela;
          if (jsonParcela['cuadros'] == null) jsonParcela['cuadros'] = [];
          jsonParcela['cuadros'].push({
            codCuadro: cuadro.codCuadro,
            nombreCuadro: cuadro.nombreCuadro
          })

        }
      });
      if (jsonParcela['cuadros'] != null) jsonToSend['parcelas'].push(jsonParcela);

    });

    if (jsonToSend['parcelas'].length > 0) {
      return jsonToSend;
    } else {
      return {}
    }
  }

  procesarFormGroup(parcelas: any) {
    let form = this.planificacionForm.value;
    this.planificacionForm.patchValue({
      cultivos: [{
        codTipoCultivo: parseInt(form.codTipoCultivo),
        cantidadCultivo: form.cantidadCultivo,
        produccionEsperada: form.produccionEsperada,
        variedadCultivo: form.variedadCultivo,
        cicloUnico: form.cicloUnico,
        parcelas: parcelas
      }]

    });

    //delete this.planificacionForm.value.codTipoCultivo;
    //delete this.planificacionForm.value.cantidadCultivo;
    //delete this.planificacionForm.value.produccionEsperada;
    //delete this.planificacionForm.value.variedadCultivo;
    //delete this.planificacionForm.value.cicloUnico;
    //delete this.planificacionForm.value.parcelas;

  }

  procesarForm() {
    this.procesarInputs();
    let parcelasConCuadros = this.procesarParcelasToSend();

    if (parcelasConCuadros != {}) {
      this.procesarFormGroup(parcelasConCuadros['parcelas']);
    }


  }


  procesarTipoCultivo(event) {
    const selectEl = event.target;
    const optionText = selectEl.options[selectEl.selectedIndex].innerText;
    const optionValue = selectEl.value;

    this.planificacionForm.value.codTipoCultivo = optionValue;

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
    this.procesarForm();

    console.warn(this.planificacionForm.value);
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
      },
      buttonsStyling: false
    })

    this.subscriptions.push(
      this._planificacionService.guardarPlanificacion(this.planificacionForm.value).subscribe(
        result =>{
          swalWithBootstrapButtons.fire({
            title: '¡Exito!',
            text: result.message,
            type: 'success',
            confirmButtonText: 'Salir',
            reverseButtons: true
          }).then((result) => {
            if (result.value) {
              this.router.navigate(['/planificacion/verPlanificacionInicial']);
            }
          });

        },
        error => this.onHttpError({ message: error.error.message})
      )
    );



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
