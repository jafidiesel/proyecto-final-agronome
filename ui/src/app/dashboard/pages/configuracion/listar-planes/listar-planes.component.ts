import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from '../../../services/configuracion/configuracion.service';

@Component({
  selector: 'app-listar-planes',
  templateUrl: './listar-planes.component.html',
  styleUrls: ['./listar-planes.component.css']
})
export class ListarPlanesComponent implements OnInit {

  planesMockedData: any;
  constructor( private _configuracionService: ConfiguracionService ) {
    this.planesMockedData = this._configuracionService.getPlanData();
   }

  ngOnInit() {
  }

}
