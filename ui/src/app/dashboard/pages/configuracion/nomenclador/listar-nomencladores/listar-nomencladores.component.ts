import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { faEdit } from '@fortawesome/free-solid-svg-icons';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-listar-nomencladores',
  templateUrl: './listar-nomencladores.component.html'
})
export class ListarNomencladoresComponent implements OnInit, OnDestroy {

  subscriptions : Subscription[] = [];
  nomencladoresMockedData: any;
  nomencladoresTabla = [];
  tableDataHeader = ['Nombre', 'Activo', 'Tipo Nomenclador', 'Editar'];
  
  tiposNomencladores = ['actividad',
  'estadoPlanificacion',
  'opcion',
  'permiso',
  'recomendacion',
  'recurso',
  'rol',
  'tipoAnalisis',
  'tipoCultivo',
  'tipoDato',
  'tipoParametro',
  'tipoPlan',
  'tipoPlanificacion',
  'tipoRecurso',
]; // Lista con todos los tipoNomenclador
  
  faEdit = faEdit;

  constructor( private _configuracionService: ConfiguracionService) {
  }
  
  ngOnInit() {
    this.nomencladoresMockedData = this._configuracionService.getNomencladorData();
    this.getNomencladores();
    
  }

  getNomencladores(){

      for (let index = 0; index < this.tiposNomencladores.length; index++) {
        const element = this.tiposNomencladores[index];
        
        this.subscriptions.push(this._configuracionService.getListaNomencladores(element).subscribe(
          (result: any) => {
            for (let index = 0; index < result.length ; index++) {
              this.nomencladoresTabla.push([
              `${result[index].nombre}`,
              `${result[index].isActiv}`,
              element, 
              `*/configuracion/editarNomenclador/${element}/${result[index].cod}`
            ]);
            }
          },
          error => console.error(error)
          )
        );
      }
  }


  onChangePage(nomencladoresTabla: Array<any>) {
    // update current page of items
    this.nomencladoresTabla = nomencladoresTabla;
  }

  ngOnDestroy(){
    this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
  }

}
