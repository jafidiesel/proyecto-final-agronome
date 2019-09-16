import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';

@Component({
  selector: 'app-crear-parametro',
  templateUrl: './crear-parametro.component.html'
})
export class CrearParametroComponent implements OnInit {

  opcionesParametroMockedData: any;

  constructor( private _configuracionService: ConfiguracionService ) {
    
    this.opcionesParametroMockedData = this._configuracionService.getOpcionesParametrotroData();

  }
  ngOnInit() {
    
  }

  
}
