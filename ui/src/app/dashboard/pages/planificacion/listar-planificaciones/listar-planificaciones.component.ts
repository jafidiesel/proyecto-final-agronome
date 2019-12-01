import { Component, OnInit } from '@angular/core';
import { PlanificacionService } from 'src/app/dashboard/services/planificacion/planificacion.service';
import { AuthService } from 'src/app/auth/auth.service';

@Component({
  selector: 'app-listar-planificaciones',
  templateUrl: './listar-planificaciones.component.html'
})
export class ListarPlanificacionesComponent implements OnInit {

  ultimoEstado: string;
  rol: string;


  planificacionesArray = [];

  constructor(
    private _planificacionService: PlanificacionService, 
    private auth: AuthService,) { }

  ngOnInit() {
    this.rol = this.auth.getRol();

    this.ultimoEstado = this._planificacionService.getTipoPlanificacion();
    if (this.ultimoEstado == 'inicial') {
      this.planificacionesArray.push(
        ["Planificación tomate BA-3", this.ultimoEstado, "20-09-2019", "/planificacion/verPlanificacionInicial"]
      );

    } else if (this.ultimoEstado == 'supervisada') {
      this.planificacionesArray.push(
        ["Planificación tomate BA-3", this.ultimoEstado, "20-09-2019", "/planificacion/verPlanificacionSupervisada"]
      );
    } else if (this.ultimoEstado == 'final') {
      this.planificacionesArray.push(
        ["Planificación tomate BA-3", this.ultimoEstado, "20-09-2019", "/planificacion/verPlanificacionFinal"]
      );
    }


    this.planificacionesArray.push(
      ["Planificación lechuga CA-3", "Final", "13-04-2019", "/planificacion/verPlanificacionFinal"]
    );
  }

  limpiarPlanificacionInicial(){
    this._planificacionService.deleteTipoPlanificacion();
  }

}
