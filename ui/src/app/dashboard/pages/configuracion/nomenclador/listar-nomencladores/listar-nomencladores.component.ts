import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { async } from '@angular/core/testing';

@Component({
  selector: 'app-listar-nomencladores',
  templateUrl: './listar-nomencladores.component.html'
})
export class ListarNomencladoresComponent implements OnInit {

  nomencladoresMockedData: any;
  nomencladoresTabla:any;
  nomencladoresArray: Array<string> = [];

  constructor( private _configuracionService: ConfiguracionService) {
    this.nomencladoresMockedData = _configuracionService.getNomencladorData();
    this.nomencladoresArray.push('','','');
    
  }
  
  ngOnInit() {
    this.nomencladoresTabla = this._configuracionService.getNomencladores();
    console.log(this._configuracionService.getNomencladores());
    console.log(this.nomencladoresTabla);
  }

}
