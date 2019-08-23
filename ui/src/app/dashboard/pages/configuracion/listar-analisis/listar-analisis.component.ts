import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from '../../../services/configuracion/configuracion.service';

@Component({
  selector: 'app-listar-analisis',
  templateUrl: './listar-analisis.component.html',
  styleUrls: ['./listar-analisis.component.css']
})
export class ListarAnalisisComponent implements OnInit {
  analisisMockedData: any;

  constructor(private _configuracionService: ConfiguracionService ) {
    this.analisisMockedData = this._configuracionService.getAnalisisData();
   }

  ngOnInit() {
  }

}
