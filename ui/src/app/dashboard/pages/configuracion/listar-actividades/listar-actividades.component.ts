import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from '../../../services/configuracion/configuracion.service';

@Component({
  selector: 'app-listar-actividades',
  templateUrl: './listar-actividades.component.html',
  styleUrls: ['./listar-actividades.component.css']
})
export class ListarActividadesComponent implements OnInit {
  actividadesMockedData: any;

  constructor(private _configuracionService: ConfiguracionService) {
    this.actividadesMockedData = this._configuracionService.getActividadData();
   }

  ngOnInit() {
  }

}
