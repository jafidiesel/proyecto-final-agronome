import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';


@Component({
  selector: 'app-listar-actividades-asociadas',
  templateUrl: './listar-actividades-asociadas.component.html'
})
export class ListarActividadesAsociadasComponent implements OnInit {
  actividadesMockedData: any;

  constructor(private _configuracionService: ConfiguracionService) {
    this.actividadesMockedData = this._configuracionService.getActividadData();
   }

  ngOnInit() {
  }

}
