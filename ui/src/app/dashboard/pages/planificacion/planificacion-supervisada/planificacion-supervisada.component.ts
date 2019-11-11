import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth/auth.service';

@Component({
  selector: 'app-planificacion-supervisada',
  templateUrl: './planificacion-supervisada.component.html',
})

export class PlanificacionSupervisadaComponent implements OnInit {
  rol: string;
  visible: boolean;

  dummyDataCultivo = [
    "Tomate", "Lechuga", "Zanahoria", "Calabaza", "Cebolla"
  ];

  tableDataHeader = ['Parcela', 'Cuadros']
  parcelaArray = []

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.visible = false;
    this.rol = this.auth.getRol();
    this.parcelaArray.push(this.tableDataHeader)
    this.parcelaArray.push([
      'Parcela 1',
      '1,2,3'
    ])
  }

  supervisar(){
    this.visible = true;
  }

}
