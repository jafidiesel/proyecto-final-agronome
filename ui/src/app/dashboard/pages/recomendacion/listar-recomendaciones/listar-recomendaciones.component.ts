import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { RecomendacionService } from 'src/app/dashboard/services/recomendacion/recomendacion.service';

@Component({
  selector: 'app-listar-recomendaciones',
  templateUrl: './listar-recomendaciones.component.html'
})
export class ListarRecomendacionesComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];


  mostrarTabla = false;
  tableDataHeader = ['Nombre', 'Fecha', 'Observacion', 'Ver'];

  aRecomendarArray = [];
  recomendadasArray = [];


  constructor(private _recomendacionService: RecomendacionService) { }

  ngOnInit() {
    // Listado de las actividades registradas
    this.subscriptions.push(
      this._recomendacionService.getListasActividad().subscribe(
        (result: any) => {
          result.actvidadesARecomendar.map((actividad: any) => {
            this.aRecomendarArray.push([
              actividad.actividad.nombreActividad,
              actividad.fchActivDetalle,
              actividad.observacion,
              `%/actividades/verActividad/${actividad.codActivDetalle}`
            ]);
          });
          console.log('aRecomendarArray',this.aRecomendarArray);
          
          result.actividadesRecomendadas.map((actividad: any) => {
            this.recomendadasArray.push([
              actividad.actividad.nombreActividad,
              actividad.fchActivDetalle,
              actividad.observacion,
              `%/actividades/verActividad/${actividad.codActivDetalle}`
            ]);
          });
          console.log('recomendadasArray',this.recomendadasArray);


          
          this.mostrarTabla = true;
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
