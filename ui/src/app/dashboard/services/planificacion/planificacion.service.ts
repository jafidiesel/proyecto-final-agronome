import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PlanificacionService {

  constructor() { }

  guardarPlanificacion(tipo: string) {
    localStorage.setItem('tipoPlanificacion', tipo.toString());
  }

  getTipoPlanificacion() {
    if (localStorage.getItem('tipoPlanificacion')) {
      return localStorage.getItem('tipoPlanificacion');
    }
  }

  deleteTipoPlanificacion(){
    localStorage.removeItem('tipoPlanificacion');
  }

}
