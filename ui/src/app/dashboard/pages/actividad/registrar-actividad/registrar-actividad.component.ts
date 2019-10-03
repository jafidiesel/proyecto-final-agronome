import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router } from '@angular/router';
import { faTint, faSpinner, faSeedling, faSpider, faCloudRain, faLeaf, faFlask, faFireAlt, faBriefcaseMedical,faPlusSquare } from '@fortawesome/free-solid-svg-icons';
import { NgbCalendar, NgbDateStruct, NgbDate, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormGroup, FormBuilder } from '@angular/forms';
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
    ['new',faPlusSquare, true ]
  ];

  model: NgbDateStruct;
  date: { year: number, month: number, day: number };

  constructor(private router: Router,
    private calendar: NgbCalendar,
    private modalService: NgbModal,
    private fb: FormBuilder,
    private _actividadService: ActividadService) { }

  ngOnInit() {

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
            if(defaultIcon){
              this.configurationButtons.push([(element.nombre).charAt(0).toUpperCase() + (element.nombre).slice(1), this.dummyConfigurationButtons[9][1], element.isActiv]);
            }

          });

        }
      )
    );

    this.initForm();
  }

  ciEquals(a:string, b:string) {
    return typeof a === 'string' && typeof b === 'string'
      ? a.localeCompare(b, undefined, { sensitivity: 'accent' }) === 0
      : a === b;
  }

  slugify(str:string) {
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
    console.log(nombreActividad);
  }

  onDateSelection(date: NgbDate) {
    this.date = date;
  }

  openVerticallyCentered(content) {
    this.modalService.open(content, { centered: true });
  }


  initForm() {

    /* this.registrarActividadForm = this.fb.group({
      parametro: this.fb.group({
        cod: [formValues[0].parametro.cod],
        nombre: [formValues[0].parametro.nombre, Validators.required],
        isActiv: [formValues[0].parametro.isActiv],
      }),
      tipoParametro: this.fb.group({
        cod: [formValues[0].tipoParametro.cod, Validators.required],
        nombre: [formValues[0].tipoParametro.nombre],
        isActiv: [formValues[0].tipoParametro.isActiv],
      }),
      tipoDato: this.fb.group({
        cod: [formValues[0].tipoDato.cod, Validators.required],
        nombre: [formValues[0].tipoDato.nombre],
        isActiv: [formValues[0].tipoDato.isActiv],
      }),
      opcion: this.fb.array( formValues[0].opcion.map( element => this.crearOpcion(element) ) ) 
      
    }); */
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
