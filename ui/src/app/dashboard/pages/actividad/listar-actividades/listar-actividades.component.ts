import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { ActividadService } from 'src/app/dashboard/services/actividad/actividad.service';
import { AuthService } from 'src/app/auth/auth.service';


@Component({
  selector: 'app-listar-actividades',
  templateUrl: './listar-actividades.component.html'
})
export class ListarActividadesComponent implements OnInit, OnDestroy {

  rol: string;

  subscriptions: Subscription[] = [];

  mostrarTabla = false;
  tableDataHeader = ['Nombre', 'Fecha', 'Observacion', 'Ver'];

  actividadesArray = [];

  constructor(private _actividadService: ActividadService, private auth: AuthService) { }

  ngOnInit() {
    this.rol = this.auth.getRol();


    // Listado de las actividades registradas
    this.subscriptions.push(
      this._actividadService.getListaActividades().subscribe(
        (result: any) => { 
          this.actividadesArray.push(this.tableDataHeader);

          result.ActividadDetalle.map( (element) => {
            this.actividadesArray.push([
              element.actividad.nombreActividad,
              element.fchActivDetalle,
              element.observacion,
              `%/actividades/verActividad/${element.codActivDetalle}`,
            ]);
          });
          this.mostrarTabla = true;
        },
        error => console.log(error)
      ));
  }

  imprimir(){
    console.log("actividadesArray",this.actividadesArray);
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }

}
