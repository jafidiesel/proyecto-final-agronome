import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-ver-planificacion-final',
  templateUrl: './ver-planificacion-final.component.html',
})
export class VerPlanificacionFinalComponent implements OnInit {

  tableDataHeader = ['Parcela', 'Cuadros']
  parcelaArray = []
  constructor() { }

  ngOnInit() {
    this.parcelaArray.push(this.tableDataHeader)
    this.parcelaArray.push(
      ['Parcela 1','1,3'],
      ['Parcela 2', '3,4'])
  }

}
