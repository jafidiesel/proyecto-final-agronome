import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { faTint, faSpinner, faSeedling, faSpider, faCloudRain, faLeaf, faFlask, faFireAlt, faBriefcaseMedical,  } from '@fortawesome/free-solid-svg-icons';
import { NgbCalendar, NgbDateStruct, NgbDate, NgbModal} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-registrar-actividad',
  templateUrl: './registrar-actividad.component.html'
})
export class RegistrarActividadComponent implements OnInit {

  step: number = 0;
  backButtonText = "Volver"; // both in initial state
  nextButtonText = "Siguiente";
  guardarClass="d-none";
  cancelarClass="btn-danger";

  configurationButtons: any[] = [
    ['Riego', faCloudRain, true],
    ['Siembra',faSpinner, true],
    ['Fertilizacion', faFlask, true],
    ['Preparacion suelo', faSeedling, true],
    ['Tratamiento fitosanitario', faBriefcaseMedical, true],
    ['Cosecha', faLeaf, true],
    ['Deteccion Fitosanitaria', faSpider, true],
    ['Deteccion Catastrofe', faFireAlt, true],
    ['Fertirrigacion', faTint, true],
  ];

  model: NgbDateStruct;
  date: {year: number, month: number, day:number};

  constructor(private router: Router,
    private calendar: NgbCalendar,
    private modalService: NgbModal) {}

  ngOnInit() {
  }

  atras(){
    switch (this.step){
      case 0:
        this.router.navigate(['/actividades']);
        break;
      case 1:
        //this.router.navigate(['/actividades']);
        this.backButtonText = "Volver";
        this.cancelarClass = "btn-danger";

        this.nextButtonText = "Siguiente";
        this.guardarClass = "d-none";
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
    
  siguiente(){
    switch (this.step){
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

  registrarActividad(nombreActividad: string){
    this.siguiente();
    console.log(nombreActividad);
  }

  onDateSelection(date: NgbDate) {
    this.date = date;
  }

  openVerticallyCentered(content) {
    this.modalService.open(content, { centered: true });
  }
}
