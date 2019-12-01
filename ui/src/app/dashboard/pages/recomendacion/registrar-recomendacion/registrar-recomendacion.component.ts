import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup } from '@angular/forms';
import { RecomendacionService } from 'src/app/dashboard/services/recomendacion/recomendacion.service';
import { Subscription } from 'rxjs';
import { NgbDateStruct, NgbDate } from '@ng-bootstrap/ng-bootstrap';
import Swal from 'sweetalert2';


@Component({
  selector: 'app-registrar-recomendacion',
  templateUrl: './registrar-recomendacion.component.html'
})
export class RegistrarRecomendacionComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  actividadForm: FormGroup;
  recomendacionForm: FormGroup;

  actividadLoaded: boolean;
  recomendacionLoaded: boolean;
  codActividad: any;
  codRecomendacion: any;
  nombreRecomendacion: string;
  codLibroCampo:number;

  // variables para manejar el formato de las fechas
  format = 'dd-MM-yyyy';
  locale = 'en-US';
  model: NgbDateStruct;
  date: { year: 2019, month: 10, day: 12 };
  fechaFormateada = "";

  time = { hour: 13, minute: 30 };

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private _recomendacionService: RecomendacionService,
    private router: Router,
    private fb: FormBuilder,
    private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    /* actividad */
    this.subscriptions.push(
      this.activatedRoute.params.subscribe(params => {
        this.subscriptions.push(

          this._recomendacionService.getActividad(params['codAct']).subscribe(
            result => {
              this.codActividad = params['codAct'];
              this.initFormActividad(result);

              if (result.actividad.codActividad == 7) {
                // deteccion de catastrofe
                this.codRecomendacion = 2;
                this.nombreRecomendacion = "Detección de catástrofe";
              } else if (result.actividad.codActividad == 8) {
                // deteccion fitosanitaria
                this.codRecomendacion = 1;
                this.nombreRecomendacion = "Detección fitosanitario";
              } else {
                /* Recibe cualquier valor que no sea 7 u 8 */
                this.onHttpError({ message: "Ocurrió un error con la actividad." });
                return false;
              }

              this.subscriptions.push(
                this._recomendacionService.getEstructuraRecomendacion(this.codRecomendacion).subscribe(
                  result => {
                    this.initFormRecomendacion(result);
                  },
                  error => this.onHttpError({ message: "Error al obtener el formulario de recomendación." })
                )
              );
            },
            error => this.onHttpError({ message: "Error al pedir los datos de la actividad." })
          )
        );

      })
    );

  }

  // metodo para comparar dos strings 
  ciEquals(a: string, b: string) {
    return typeof a === 'string' && typeof b === 'string'
      ? a.localeCompare(b, undefined, { sensitivity: 'accent' }) === 0
      : a === b;
  }

  // metodo para convertir strings con may, min y caracteres especiales
  slugify(str: string) {
    var map = {
      '': ' ',
      'a': 'á|à|ã|â|À|Á|Ã|Â',
      'e': 'é|è|ê|É|È|Ê',
      'i': 'í|ì|î|Í|Ì|Î',
      'o': 'ó|ò|ô|õ|Ó|Ò|Ô|Õ',
      'u': 'ú|ù|û|ü|Ú|Ù|Û|Ü',
      'c': 'ç|Ç',
      'n': 'ñ|Ñ'
    };
    str = str.toLowerCase();

    for (var pattern in map) {
      str = str.replace(new RegExp(map[pattern], 'g'), pattern);
    }
    return str;
  }

  procesarOpciones(event) {

    const selectEl = event.target;
    const optionText = selectEl.options[selectEl.selectedIndex].innerText;

    if (this.slugify(optionText.toLowerCase()) == "otro" || this.slugify(optionText.toLowerCase()) == "otra") {
      let input = document.createElement("input");
      input.setAttribute('id', 'other' + selectEl.value);
      input.classList.add("form-control", "mt-2");
      input.placeholder = "Detalle su opción elegida."
      if (!document.querySelector('[id^=other]')) {
        selectEl.parentElement.append(input);
      }

    }

    let formValues: any;
    formValues = this.recomendacionForm.value;

    formValues.parametro.map(element => {
      if (element.opcion != null) {
        element.opcion.map(opc => {
          if (this.ciEquals(this.slugify(opc.nombre), this.slugify(optionText))) {
            element.valor = this.slugify(optionText);
          }
        });
      }
    });
  }

  checkOtherFields() {
    this.recomendacionForm.value.parametro.map(element => {
      if (element.valor == "otro" || element.valor == "otra") {
        let otherFields: any = document.querySelector('[id^=other]');
        element.valor = element.valor + ": " + otherFields.value;
      }
    });
  }


  // metodo para asignar la fecha seleccionada
  onDateSelection(date: NgbDate) {
    let dayString = date.day.toString();

    if ((dayString).length < 2) {
      dayString = "0" + date.day;
    }

    // Modificar para alterar el  orden del formato de la fecha
    let fecha = date.year + "-" + date.month + "-" + dayString + " ";

    this.recomendacionForm.patchValue({
      fchRecomDetalle: fecha,
    });
  }

  // actualizacion del valor del parametro
  actualizarValorParametro(event) {
    const selectEl = event.target;
    const valor = selectEl.value;
    const id = selectEl.id;

    this.recomendacionForm.get('parametro').value.map(element => {
      if (id == element.nombre) {
        element.valor = valor;
      }
    });
  }

  crearParametro(obj: any) {
    return this.fb.control({
      codParam: obj.codParametro,
      valor: obj.valor,
      nombre: obj.nombreParametro,
    });
  }

  crearParametroRecomendacion(obj: any) {
    return this.fb.control({
      codParam: obj.parametro.cod,
      valor: null,
      nombre: obj.parametro.nombre,
      tipo: obj.tipoDato.nombre.toLowerCase()
    });
  }

  // creacion del parametro para formgroup con opciones
  crearParametroRecomendacionConOpcion(obj: any, index) {
    return this.fb.control({
      codParam: obj.parametro.cod,
      valor: null,
      nombre: obj.parametro.nombre,
      isActiv: obj.parametro.isActiv,
      tipo: obj.tipoDato.nombre.toLowerCase(),
      opcion: obj.opcion
    });
  }


  initFormActividad(form) {
    this.codLibroCampo = form.libroCampo.codLibroCampo;

    this.actividadForm = this.fb.group({
      codActividad: form.actividad.codActividad,
      nombreActividad: form.actividad.nombreActividad,
      fchActivDetalle: form.fchActivDetalle,
      nombreLibroCampo: form.libroCampo.nombreLibroCampo,
      observacion: form.observacion,
      imagen: [{}],
      parametro: this.fb.array(form.parametro.map(element => this.crearParametro(element)))

    });
    this.actividadLoaded = true;
  }

  initFormRecomendacion(form) {
    /* form = estructura de la recomendacion */
    /* TODO: cambiar el 'parametros' por 'parametro' */
    this.recomendacionForm = this.fb.group({
      tempFecha: this.date,
      tempHora: this.time,
      codRecomendacion: parseInt(this.codRecomendacion),
      codActividadDetalle: parseInt(this.codActividad),
      nombreRecomendacion: this.nombreRecomendacion,
      codLibroCampo: this.codLibroCampo,
      fchRecomDetalle: null,
      observacion: " ",
      parametro: this.fb.array(form.parametros.reverse().map((element, index) => {
        if (element.opcion.length > 0) {
          return this.crearParametroRecomendacionConOpcion(element, index);
        } else {
          return this.crearParametroRecomendacion(element);
        }
      })),
      analisis: [{}]

    });
    this.recomendacionLoaded = true;
  }

  // envio de form
  onSubmit() {
    this.checkOtherFields();

    // Modificar para alterar el  orden del formato de la fecha
    let fecha = this.recomendacionForm.value.fchActivDetalle + " " + this.recomendacionForm.value.tempHora.hour + ":" + this.recomendacionForm.value.tempHora.minute;

    this.recomendacionForm.patchValue({
      fchActivDetalle: fecha,
    });

    if (this.recomendacionForm.status == 'VALID') {
      this.subscriptions.push(
        this._recomendacionService.postRecomendacion(this.recomendacionForm.value).subscribe(
          result => {
            this.postSuccess = true;
            this.postError = false;
            this.postErrorMessage = '';

            //prodn
            const swalWithBootstrapButtons = Swal.mixin({
              customClass: {
                confirmButton: 'btn btn-success ml-1',
              },
              buttonsStyling: false
            })

            swalWithBootstrapButtons.fire({
              title: '¡Exito!',
              text: 'Se registro su recomendación correctamente.',
              type: 'success',
              confirmButtonText: 'Salir',
              reverseButtons: true
            }).then((result) => {
              if (result.value) {
                this.router.navigate(['recomendaciones/libroDeCampo']);
              }
            }
            )
          },
          error => this.onHttpError(error)
        )
      );

    } else {
      this.onHttpError({ message: "Complete todos los campos obligatorios." });
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
