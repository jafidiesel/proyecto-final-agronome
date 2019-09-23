import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Subscription } from 'rxjs';
import { debug } from 'util';


@Component({
  selector: 'app-listar-actividades-asociadas',
  templateUrl: './listar-actividades-asociadas.component.html'
})
export class ListarActividadesAsociadasComponent implements OnInit, OnDestroy {
  
  subscriptions : Subscription[] = [];
  
  // array de rows para table component
  actividadesTabla = [];
  tableDataHeader = ['Nombre Actividad', 'Activo', 'Editar'];
  mostrarTabla:boolean = false;
  
  actividadesMockedData: any;

  constructor(private _configuracionService: ConfiguracionService) {
    this.actividadesMockedData = this._configuracionService.getActividadData();
   }

  ngOnInit() {
    this.subscriptions.push(this._configuracionService.getListaAsociacion('actividadParametro').subscribe(
      (result:any) => {
        this.actividadesTabla.push(this.tableDataHeader);

        for (let index = 0; index < result.parametro.length ; index++) {
          this.actividadesTabla.push([
          `${result.parametro[index].nombreActividad}`,
          `${result.parametro[index].isActiv}`,
          `*/configuracion/asociar/editarActividad/${result.parametro[index].codActividad}`
        ]);
        }
        this.mostrarTabla = true;
      },
      error => console.error(error)
    ));
  }

  ngOnDestroy(){
    this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
  }
}
