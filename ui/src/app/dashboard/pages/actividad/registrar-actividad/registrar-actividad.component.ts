import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router } from '@angular/router';
import { faTint, faSpinner, faSeedling, faSpider, faCloudRain, faLeaf, faFlask, faFireAlt, faBriefcaseMedical, faPlusSquare } from '@fortawesome/free-solid-svg-icons';
import { NgbCalendar, NgbDateStruct, NgbDate, NgbModal, NgbTimepicker } from '@ng-bootstrap/ng-bootstrap';
import { FormGroup, FormBuilder, FormControl, FormArray, Validators } from '@angular/forms';
import { Subscription } from 'rxjs';
import { ActividadService } from 'src/app/dashboard/services/actividad/actividad.service';
import Swal from 'sweetalert2';
import { AuthService } from 'src/app/auth/auth.service';



@Component({
  selector: 'app-registrar-actividad',
  templateUrl: './registrar-actividad.component.html'
})
export class RegistrarActividadComponent implements OnInit, OnDestroy {

  // variables utilizadas para mostrar info
  nombreActividad: string;
  codActividad: number;

  // variables de finca
  codFinca: string;

  // variables de libro de campo
  librosDeCampo = [];


  // array usado para limpiar las subscripciones
  subscriptions: Subscription[] = [];

  // formgroup
  registrarActividadForm: FormGroup;

  // variables usadas para manejar la redireccion
  step: number = 0;
  backButtonText = "Volver"; // both in initial state
  nextButtonText = "Guardar";
  guardarClass = "btn-success";
  cancelarClass = "btn-danger";

  configurationButtons: any[] = [];

  // mock data for icons
  dummyConfigurationButtons: any[] = [
    ['Riego', faCloudRain, true],
    ['Siembra', faSpinner, true],
    ['Fertilización', faFlask, true],
    ['Preparación suelo', faSeedling, true],
    ['Tratamiento fitosanitario', faBriefcaseMedical, true],
    ['Cosecha', faLeaf, true],
    ['Detección Fitosanitaria', faSpider, true],
    ['Detección Catástrofe', faFireAlt, true],
    ['Fertirrigación', faTint, true],
    ['new', faPlusSquare, true]
  ];

  // variables para manejar el formato de las fechas
  format = 'dd-MM-yyyy';
  locale = 'en-US';
  model: NgbDateStruct;
  date: { year: 2019, month: 10, day: 12 };
  fechaFormateada = "";

  time = { hour: 13, minute: 30 };

  // flag que comprueba el estado de los comprobados
  camposParametrosCompletados = false;

  // banderas de error
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private router: Router,
    private calendar: NgbCalendar,
    private modalService: NgbModal,
    private fb: FormBuilder,
    private _actividadService: ActividadService,
    private _authService: AuthService) { }

  ngOnInit() {

    this.codFinca = this._authService.getCurrentCodFinca();

    this.subscriptions.push(
      this._actividadService.getLibrosCampo( parseInt(this.codFinca) ).subscribe(
        result => {
          result.map(finca => {
            this.librosDeCampo.push({
              codLibroCampo: finca.codLibroCampo,
              nombreLibroCampo: finca.nombreLibroCampo
            });
          });
        },
        error => this.onHttpError({ message: "Ocurrio un error obteniendo los libros de campo." })
      )
    );
    // Listado de actividades a seleccionar
    this.subscriptions.push(
      this._actividadService.getListaNomencladoresConFiltro('actividad', true).subscribe(
        (result: any) => {
          let defaultIcon = false;
          result.map(element => {
            defaultIcon = true;
            this.dummyConfigurationButtons.map(dummyElement => {
              if (this.ciEquals(this.slugify(dummyElement[0]), this.slugify(element.nombre))) {
                this.configurationButtons.push([(element.nombre).charAt(0).toUpperCase() + (element.nombre).slice(1), dummyElement[1], element.isActiv, element.cod]);
                defaultIcon = false;

              }
            });
            if (defaultIcon) {
              this.configurationButtons.push([(element.nombre).charAt(0).toUpperCase() + (element.nombre).slice(1), this.dummyConfigurationButtons[9][1], element.isActiv, element.cod]);
            }
            this.codActividad = element.cod;
          });

          // Obtencion de la estructura de la actividad para crear formulario
          this.subscriptions.push(
            this._actividadService.getEstructuraActividad(this.codActividad).subscribe(
              result => {
                this.initForm(result);
              },
              error => this.onHttpError({ message: "Error al recuperar el formulario de la actividad" })
            )
          );
        }
      )
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

  // metodo para manejar la navegacion hacia atras
  atras() {
    this.postError = false;
    this.postErrorMessage = '';
    switch (this.step) {
      case 0:
        this.router.navigate(['/actividades/listarActividades']);
        break;
      case 1:
        this.backButtonText = "Volver";
        this.cancelarClass = "btn-danger";
        this.nombreActividad = "";

        this.step--;
        break;
      case 2:
        this.backButtonText = "Atrás";
        this.cancelarClass = "btn-secondary";
        this.step--;
        break;
      default:
        this.backButtonText = "Atrás";
        this.cancelarClass = "btn-secondary";
        this.step--;
        break;
    }
  }

  // metodo para manejar la navegacion hacia adelante
  siguiente() {
    this.postError = false;
    this.postErrorMessage = '';

    switch (this.step) {
      case 2:
        this.checkOtherFields();
        this.onSubmit();
        /*
                this.backButtonText = "Atrás";
                this.nextButtonText = "Guardar";
                this.guardarClass = "btn-success";
                this.cancelarClass = "btn-secondary";
                this.step++; */
        break;
      case 1:
        /* this.backButtonText = "Atrás";
        this.cancelarClass = "btn-secondary";
        this.step++; */
        this.checkOtherFields();
        this.onSubmit();
        break;
      default:
        this.backButtonText = "Atrás";
        this.cancelarClass = "btn-secondary";
        this.step++;
        break;
    }

  }

  // inicializador de la estructura de la actividad segun que actividad se selecciona
  registrarActividad(nombreActividad: string, codActividad: number) {
    this.codActividad = codActividad;

    this.subscriptions.push(
      this._actividadService.getEstructuraActividad(codActividad).subscribe(
        result => {
          this.initForm(result);
        },
        error => this.onHttpError({ message: "Error al obtener la estructura de la actividad." })
      )
    );

    this.nombreActividad = nombreActividad;
    this.codActividad = codActividad;
    this.siguiente();
  }

  // metodo para asignar la fecha seleccionada
  onDateSelection(date: NgbDate) {
    let dayString = date.day.toString();

    if ((dayString).length < 2) {
      dayString = "0" + date.day;
    }

    // Modificar para alterar el  orden del formato de la fecha
    let fecha = date.year + "-" + date.month + "-" + dayString;

    this.registrarActividadForm.patchValue({
      fchActivDetalle: fecha,
    });
  }

  // metodo para abrir el modal
  openVerticallyCentered(content) {
    this.modalService.open(content, { centered: true });
  }


  // creacion del parametro para formgroup
  crearParametro(obj: any, index) {
    return this.fb.control({
      codParam: obj.parametro.cod,
      valor: null,
      nombre: obj.parametro.nombre,
      isActiv: obj.parametro.isActiv,
      tipo: obj.tipoDato.nombre.toLowerCase(),
    })
      ;
  }

  // creacion del parametro para formgroup con opciones
  crearParametroConOpcion(obj: any, index) {
    return this.fb.control({
      codParam: obj.parametro.cod,
      valor: null,
      nombre: obj.parametro.nombre,
      isActiv: obj.parametro.isActiv,
      tipo: obj.tipoDato.nombre.toLowerCase(),
      opcion: obj.opcion
    });
  }


  // inicializador del formgroup
  initForm(form) {
    this.registrarActividadForm = this.fb.group({
      tempFecha: this.date,
      tempHora: this.time,
      codActividad: this.codActividad,
      fchActivDetalle: [null, Validators.required],
      observacion: " ",
      codLibroCampo: [null, Validators.required],
      imagen: [{}],
      parametro: this.fb.array(form.parametros.map((element, index) => {
        if (element.opcion.length > 0) {
          return this.crearParametroConOpcion(element, index);
        } else {
          return this.crearParametro(element, index);
        }
      }))

    });

  }

  parametrosCompletados() {
    // verificador si los parametros de la actividad fueron completados
    let list = document.querySelectorAll(".input-parametros");
    for (let index = 0; index < list.length; index++) {
      const element: any = list[index];
      if (element.value == "") return false;
    }
    return true;
  }

  procesarOpciones(event) {

    const selectEl = event.target;
    const optionText = selectEl.options[selectEl.selectedIndex].innerText;

    if (this.slugify(optionText.toLowerCase()) == "otro" || this.slugify(optionText.toLowerCase()) == "otra") {
      let input = document.createElement("input");
      input.setAttribute('id', 'other' + selectEl.value);
      input.classList.add("form-control", "mt-2");
      input.placeholder = "Detalle su opción elegida."
      selectEl.parentElement.append(input);

    }
    let formValues: any;
    formValues = this.registrarActividadForm.value;

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

  // actualizacion del valor del parametro
  actualizarValorParametro(event) {
    const selectEl = event.target;
    const valor = selectEl.value;
    const id = selectEl.id;

    this.registrarActividadForm.get('parametro').value.map(element => {
      if (id == element.nombre) {
        element.valor = valor;
      }
    });
  }

  checkOtherFields() {
    this.registrarActividadForm.value.parametro.map(element => {
      if (element.valor == "otro" || element.valor == "otra") {
        let otherFields: any = document.querySelector('[id^=other]');
        element.valor = element.valor + ": " + otherFields.value;
      }
    });
  }


  // envio de form
  onSubmit() {
    // Modificar para alterar el  orden del formato de la fecha
    let fecha = this.registrarActividadForm.value.fchActivDetalle + " " + this.registrarActividadForm.value.tempHora.hour + ":" + this.registrarActividadForm.value.tempHora.minute;

    this.registrarActividadForm.patchValue({
      fchActivDetalle: fecha,
    });

    if (this.registrarActividadForm.status == 'VALID'
      && this.parametrosCompletados()
      && this.registrarActividadForm.value.tempFecha.day != '') {
      this.subscriptions.push(
        this._actividadService.postActividad(this.registrarActividadForm.value).subscribe(
          result => {
            this.postSuccess = true;
            this.postError = false;
            this.postErrorMessage = '';

            const swalWithBootstrapButtons = Swal.mixin({
              customClass: {
                confirmButton: 'btn btn-success ml-1',
              },
              buttonsStyling: false
            })

            swalWithBootstrapButtons.fire({
              title: '¡Exito!',
              text: 'Se registro la actividad correctamente.',
              type: 'success',
              confirmButtonText: 'Salir',
              reverseButtons: true
            }).then((result) => {
              if (result.value) {
                this.router.navigate(['actividades/listarActividades']);
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
