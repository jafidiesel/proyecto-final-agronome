import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-planificacion-inicial',
  templateUrl: './planificacion-inicial.component.html'
})
export class PlanificacionInicialComponent implements OnInit {
  
  dummyDataCultivo = [
    "Tomate", "Lechuga", "Zanahoria", "Calabaza", "Cebolla"
  ];

  tableDataHeader = ['Parcela', 'Cuadros']
  parcelaArray = []

  constructor() { }

  ngOnInit() {
    this.parcelaArray.push(this.tableDataHeader)
    this.parcelaArray.push([
      'Parcela 1',
      '1,2,3'
    ])

    console.log("parcelasArray",this.parcelaArray);
  }

}
