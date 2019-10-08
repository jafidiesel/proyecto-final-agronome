import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router } from '@angular/router';
import { faTint, faSpinner, faSeedling, faSpider, faCloudRain, faLeaf, faFlask, faFireAlt, faBriefcaseMedical, faPlusSquare } from '@fortawesome/free-solid-svg-icons';
import { NgbCalendar, NgbDateStruct, NgbDate, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormGroup, FormBuilder, FormControl, FormArray } from '@angular/forms';
import { Subscription } from 'rxjs';
import { ActividadService } from 'src/app/dashboard/services/actividad/actividad.service';

@Component({
  selector: 'app-registrar-actividad',
  templateUrl: './registrar-actividad.component.html'
})
export class RegistrarActividadComponent implements OnInit, OnDestroy {

  nombreActividad: string;

  subscriptions: Subscription[] = [];

  registrarActividadForm: FormGroup;

  step: number = 0;
  backButtonText = "Volver"; // both in initial state
  nextButtonText = "Siguiente";
  guardarClass = "d-none";
  cancelarClass = "btn-danger";

  configurationButtons: any[] = [];

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

  model: NgbDateStruct;
  date: { year: number, month: number, day: number };

  constructor(private router: Router,
    private calendar: NgbCalendar,
    private modalService: NgbModal,
    private fb: FormBuilder,
    private _actividadService: ActividadService) { }

  ngOnInit() {

    // Listado de actividades a seleccionar
    this.subscriptions.push(
      this._actividadService.getListaNomencladoresConFiltro('actividad', true).subscribe(
        (result: any) => {
          let defaultIcon = false;
          result.map(element => {
            defaultIcon = true;
            this.dummyConfigurationButtons.map(dummyElement => {
              if (this.ciEquals(this.slugify(dummyElement[0]), this.slugify(element.nombre))) {
                this.configurationButtons.push([(element.nombre).charAt(0).toUpperCase() + (element.nombre).slice(1), dummyElement[1], element.isActiv]);
                defaultIcon = false;
              }
            });
            if (defaultIcon) {
              this.configurationButtons.push([(element.nombre).charAt(0).toUpperCase() + (element.nombre).slice(1), this.dummyConfigurationButtons[9][1], element.isActiv]);
            }

          });

        }
      )
    );

    // Obtencion de la estructura de la actividad para crear formulario
    this.subscriptions.push(
      this._actividadService.getEstructuraActividad(1).subscribe( // reemplazar 1 con codActividad
        result => {
          console.log('result', result);
          //console.log('getEstructuraActividad', result);
          this.initForm(result);
        },
        error => console.log('error', error)
      )
    );

  }

  ciEquals(a: string, b: string) {
    return typeof a === 'string' && typeof b === 'string'
      ? a.localeCompare(b, undefined, { sensitivity: 'accent' }) === 0
      : a === b;
  }

  slugify(str: string) {
    var map = {
      '-': ' ',
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

  atras() {
    switch (this.step) {
      case 0:
        this.router.navigate(['/actividades']);
        break;
      case 1:
        //this.router.navigate(['/actividades']);
        this.backButtonText = "Volver";
        this.cancelarClass = "btn-danger";

        this.nextButtonText = "Siguiente";
        this.guardarClass = "d-none";

        this.nombreActividad = "";

        this.step--;
        break;
      case 2:
        this.backButtonText = "Atrás";
        this.cancelarClass = "btn-secondary";

        this.nextButtonText = "Siguiente";
        this.guardarClass = "btn-primary";
        this.step--;
        break;
      default:
        this.backButtonText = "Atrás";
        this.cancelarClass = "btn-secondary";

        this.nextButtonText = "Siguiente";
        this.guardarClass = "btn-primary";
        this.step--;
        break;
    }
  }

  siguiente() {
    switch (this.step) {
      case 3:
        //this.router.navigate(['/actividades'])
        break;
      case 2:
        this.backButtonText = "Atrás";
        this.nextButtonText = "Guardar";
        this.guardarClass = "btn-success";
        this.cancelarClass = "btn-secondary";
        this.step++;
        break;
      case 1:
        this.backButtonText = "Atrás";
        this.nextButtonText = "Siguiente";
        this.cancelarClass = "btn-secondary";
        this.guardarClass = "btn-primary";
        this.step++;
        break;
      default:
        this.backButtonText = "Atrás";
        this.nextButtonText = "Siguiente";
        this.guardarClass = "btn-primary";
        this.cancelarClass = "btn-secondary";
        this.step++;
        break;
    }

  }

  registrarActividad(nombreActividad: string) {
    this.nombreActividad = nombreActividad;
    this.siguiente();
  }

  onDateSelection(date: NgbDate) {
    this.date = date;
  }

  openVerticallyCentered(content) {
    this.modalService.open(content, { centered: true });
  }

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
  
  crearParametroConOpcion(obj: any, index) {
    console.log('obj.opcion', obj.opcion);
    return this.fb.control({
      codParam: obj.parametro.cod,
      valor: null,
      nombre: obj.parametro.nombre,
      isActiv: obj.parametro.isActiv,
      tipo: obj.tipoDato.nombre.toLowerCase(),
      opcion: obj.opcion
    });
  }

  actualizarValorParametro(event) {
    const selectEl = event.target;
    const valor = selectEl.value;
    const id = selectEl.id;
    
    this.registrarActividadForm.get('parametros').value.map( element => {
      if(id == element.nombre){
        element.valor = valor;
      }
    } );
  }

  initForm(form) {
    this.registrarActividadForm = this.fb.group({
      codActividad : 1,
      fchActivDetalle: "2019-10-30 22:12:54",
      observacion:"Se riega en la finca por segunda vez",
      imagenes:[{}],
      parametros: this.fb.array(form.parametros.map((element, index) => {
        console.log('index', index);
        if (element.opcion.length > 0) {
          return this.crearParametroConOpcion(element, index);
        } else {
          return this.crearParametro(element, index);
        }
      }))

    });

    console.log('this.registrarActividadForm', this.registrarActividadForm);
  }




  onSubmit() {
    console.log('form a enviar', this.registrarActividadForm.value);

    this.subscriptions.push(
      this._actividadService.postActividad(this.registrarActividadForm.value).subscribe(
        result => console.log('exito'),
        error => console.error(error)
      )
    );
  }

  imprimir() {
    console.warn("imprimir()", this.registrarActividadForm);
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
