import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { async } from '@angular/core/testing';
import { faEdit, faPowerOff } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-listar-nomencladores',
  templateUrl: './listar-nomencladores.component.html'
})
export class ListarNomencladoresComponent implements OnInit {

  nomencladoresMockedData: any;
  nomencladoresTabla = [];
  tableDataHeader = ['Nombre', 'Activo', 'Tipo Nomenclador', 'Accion', ''];

  faEdit = faEdit;
  faPowerOff = faPowerOff;

  constructor( private _configuracionService: ConfiguracionService) {
    this.nomencladoresMockedData = _configuracionService.getNomencladorData();
    this.getNomencladores();


  }

  ngOnInit() {
  }

  getNomencladores(){
    this._configuracionService.getNomencladores().subscribe(
      (result: any) => {
        for (let index = 0; index < result.length ; index++) {
          this.nomencladoresTabla.push([
            `${result[index].nombre}`,
            `${result[index].isActiv}`,
            'Actividad', 
            `*/configuracion/editarNomenclador/${result[index].id}`, 
            `-/Desactivar`]);
        }
        // document.getElementById('app-table').innerHTML = '<app-table [tableData]="this.nomencladoresTabla" ></app-table>';
      },
      error => console.log('error')
    );

  }

  imprimir() {
    console.log(this.nomencladoresTabla);
  }

}
