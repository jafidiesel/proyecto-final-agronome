import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';

@Component({
  selector: 'app-listar-parametros',
  templateUrl: './listar-parametros.component.html'
})
export class ListarParametrosComponent implements OnInit {

  parametrosMockedData: any;
  constructor( private _configuracionService: ConfiguracionService ) {
    this.parametrosMockedData = this._configuracionService.getParametroData();

  }

  ngOnInit() {
  }
}
