import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { RecomendacionService } from 'src/app/dashboard/services/recomendacion/recomendacion.service';

@Component({
  selector: 'app-listar-recomendaciones',
  templateUrl: './listar-recomendaciones.component.html'
})
export class ListarRecomendacionesComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];


  tableDataHeaderReco = ['Nombre', 'Fecha', 'Observacion', 'Recomendar'];
  tableDataHeader = ['Nombre', 'Fecha', 'Observacion', 'Ver'];
  
  aRecomendarArray = [];
  mostrarTablaARecomendar = false;
  recomendadasArray = [];
  mostrarTablaRecomendadas = false;


  constructor(private _recomendacionService: RecomendacionService) { }

  ngOnInit() {
    // Listado de las actividades registradas
    this.subscriptions.push(
      this._recomendacionService.getListasActividad().subscribe(
        (result: any) => {
          this.aRecomendarArray.push(this.tableDataHeaderReco);
          console.log('result.actvidadesARecomendar',result.actvidadesARecomendar.length);
          result.actvidadesARecomendar.map((actividad: any) => {
            this.aRecomendarArray.push([
              actividad.actividad.nombreActividad,
              actividad.fchActivDetalle,
              actividad.observacion,
              `%/actividades/verActividad/${actividad.codActivDetalle}`
            ]);
          });
          console.log('aRecomendarArray',this.aRecomendarArray);
          this.mostrarTablaARecomendar = true;
          
          this.recomendadasArray.push(this.tableDataHeader);
          console.log('result.actividadesRecomendadas',result.actividadesRecomendadas.length);
          result.actividadesRecomendadas.map((actividad: any) => {
            this.recomendadasArray.push([
              actividad.actividad.nombreActividad,
              actividad.fchActivDetalle,
              actividad.observacion,
              `%/actividades/verActividad/${actividad.codActivDetalle}`
            ]);
          });
          console.log('recomendadasArray',this.recomendadasArray);
          this.mostrarTablaRecomendadas = true;

          
        },
        error => console.log(error)
      ));
  }

  imprimir() {
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }

}
