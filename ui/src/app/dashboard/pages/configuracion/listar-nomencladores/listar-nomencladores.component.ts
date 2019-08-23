import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';

@Component({
  selector: 'app-listar-nomencladores',
  templateUrl: './listar-nomencladores.component.html',
  styleUrls: ['./listar-nomencladores.component.css']
})
export class ListarNomencladoresComponent implements OnInit {

  nomencladoresMockedData: any;

  constructor( private _configuracionService: ConfiguracionService) {
    this.nomencladoresMockedData = _configuracionService.getNomencladorData();

   }

  ngOnInit() {
  }

}
