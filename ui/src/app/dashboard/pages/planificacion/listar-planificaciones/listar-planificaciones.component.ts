import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-listar-planificaciones',
  templateUrl: './listar-planificaciones.component.html'
})
export class ListarPlanificacionesComponent implements OnInit {

  planificacionesArray = [
    ["Planificación tomate BA-3", "Inicial", "20-09-2019", "0"],
    ["Planificación papa MA-1", "Supervisada", "20-05-2019", "0"],
    ["Planificación tomate CA-2", "Finalizada", "20-01-2019", "0"],
  ];

  constructor() { }

  ngOnInit() {
  }

}
