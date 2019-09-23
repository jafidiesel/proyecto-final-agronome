import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registrar-actividad',
  templateUrl: './registrar-actividad.component.html'
})
export class RegistrarActividadComponent implements OnInit {

  step: number = 1;
  backButtonText = "Volver"; // both in initial state
  nextButtonText = "Siguiente";
  guardarClass="btn-primary";
  cancelarClass="btn-danger";


  constructor(private router: Router,) { }

  ngOnInit() {
  }

  atras(){
    switch (this.step){
      case 1:
        this.router.navigate(['/actividades']);
        break;
      case 2:
        this.backButtonText = "Volver";
        this.cancelarClass = "btn-danger";

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
      default:
        this.backButtonText = "Atrás";
        this.nextButtonText = "Siguiente";
        this.guardarClass = "btn-primary";
        this.cancelarClass = "btn-secondary";
        this.step++;
        break;
    }

  }

}
