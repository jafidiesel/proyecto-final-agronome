import { Component, OnInit, OnDestroy } from '@angular/core';
import { PlanificacionService } from 'src/app/dashboard/services/planificacion/planificacion.service';
import { AuthService } from 'src/app/auth/auth.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-listar-grupos',
  templateUrl: './listar-grupos.component.html'
})
export class ListarGruposComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];
  codfinca: number;

  planificacionesArray = [];

  // banderas de error
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(
    private _planificacionService: PlanificacionService,
    private auth: AuthService
  ) { }

  ngOnInit() {
    this.codfinca = parseInt(this.auth.getCurrentCodFinca());

    this.subscriptions.push(
      this._planificacionService.getPlanificacionesCreadas(this.codfinca).subscribe(
        result => {
          result.map(planificacion => this.planificacionesArray.push(planificacion));
          console.log('this.planificacionesArray',this.planificacionesArray);
        },
        error => this.onHttpError({ message: error.error.message })
      )
    );
  }

  // metodo custom para mostrar mensajes de error
  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
