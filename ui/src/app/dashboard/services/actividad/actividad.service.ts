import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ActividadService {

  constructor() {
    console.log("ActividadService up and running");

  }

  private dummyTextLibroDeCampo = [
    {
      nombre: "Libro de campo n°1",
      actividades: {
        
      }
    }
  ];


}
