import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';

@Component({
  selector: 'app-listar-recomendaciones',
  templateUrl: './listar-recomendaciones.component.html',
})
export class ListarRecomendacionesComponent implements OnInit {
  recomendacionesMockedData: any;

  constructor( private _configuracionService: ConfiguracionService ) {
    this.recomendacionesMockedData = this._configuracionService.getRecomendacionData();
   }

  ngOnInit() {
  }

}
