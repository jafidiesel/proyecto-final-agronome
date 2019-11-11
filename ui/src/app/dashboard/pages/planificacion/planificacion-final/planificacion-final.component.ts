import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth/auth.service';

@Component({
  selector: 'app-planificacion-final',
  templateUrl: './planificacion-final.component.html',
  styleUrls: ['./planificacion-final.component.css']
})
export class PlanificacionFinalComponent implements OnInit {
  rol: string;
  visible: boolean;

  dummyDataCultivo = [
    "Tomate","Lechuga","Zanahoria", "Calabaza", "Cebolla"
  ];

  tableDataHeader = ['Parcela', 'Cuadros']
  parcelaArray = []

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.visible = false;
    this.rol = this.auth.getRol();
    console.log(this.rol)
    this.parcelaArray.push(this.tableDataHeader)
    this.parcelaArray.push(
      ['Parcela 1','1,2,3'],
    ['Parcela 2', '2,3,4'])
  }

  finalizar(){
    this.visible = true;

  }
}
