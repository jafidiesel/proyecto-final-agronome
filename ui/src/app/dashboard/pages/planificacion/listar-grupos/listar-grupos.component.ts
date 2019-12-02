import { Component, OnInit, OnDestroy } from '@angular/core';
import { PlanificacionService } from 'src/app/dashboard/services/planificacion/planificacion.service';
import { AuthService } from 'src/app/auth/auth.service';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-listar-grupos',
  templateUrl: './listar-grupos.component.html'
})
export class ListarGruposComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  rol: string;
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
    this.rol = this.auth.getRol();

    this.subscriptions.push(
      this._planificacionService.getGrupos(this.codfinca).subscribe(
        result => {
          result.map(planificacion => this.planificacionesArray.push(planificacion));
        },
        error => this.onHttpError({ message: error.error.message })
      )
    );
  }

  cancelarGrupo(codGrupo: number) {
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
        cancelButton: 'btn btn-danger mr-1'
      },
      buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
      title: '¿Deseas cancelar el grupo planificación?',
      type: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Si',
      cancelButtonText: 'No',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {

        this.subscriptions.push(
          this._planificacionService.cancelarGrupo(codGrupo).subscribe(
            result => {
              swalWithBootstrapButtons.fire({
                title: '¡Exito!',
                text: result.message,
                type: 'success',
                confirmButtonText: 'Salir',
                reverseButtons: true
              })
            },
            error => {
              swalWithBootstrapButtons.fire({
                allowOutsideClick: true,
                type: 'error',
                title: 'Error',
                text: error.error.message,
                confirmButtonText: 'Ok',
                reverseButtons: true
              })
            }
          )
        )




      }
    })
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
