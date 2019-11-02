import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';

import { ActividadService } from 'src/app/dashboard/services/actividad/actividad.service';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-ver-actividad',
  templateUrl: './ver-actividad.component.html'
})
export class VerActividadComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  registrarActividadForm: FormGroup;
  loaded: boolean;
  codActividad: number;

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private _actividadService: ActividadService,
    private fb: FormBuilder,
    private modalService: NgbModal,
    private activatedRoute: ActivatedRoute, ) { }

  ngOnInit() {
    this.subscriptions.push(
      this.activatedRoute.params.subscribe(params => {
        this.subscriptions.push(

          this._actividadService.getActividad(params['cod']).subscribe(
            result => {
              this.codActividad = params['cod'];
              this.initForm(result);
            },
            error =>  this.onHttpError({ message: "Error al pedir los datos de la actividad." })
          )
        );

      })
    )
  }

  crearParametro(obj: any) {
    return this.fb.control({
      codParam: obj.codParametro,
      valor: obj.valor,
      nombre: obj.nombreParametro.toLowerCase()
    })
      ;
  }

  initForm(form) {
    this.registrarActividadForm = this.fb.group({
      codActividad: form.actividad.codActividad,
      nombreActividad: form.actividad.nombreActividad,
      fchActivDetalle: form.fchActivDetalle,
      observacion: form.observacion,
      imagenes: [{}],
      parametro: this.fb.array(form.parametro.map(element => this.crearParametro(element)))

    });
    this.loaded = true;

  }

  openVerticallyCentered(content) {
    this.modalService.open(content, { centered: true });
  }

  deleteActivity() {
    console.warn(this.codActividad);
    this.subscriptions.push(
      this._actividadService.deleteActividad(this.codActividad).subscribe(
        result => this.postSuccess = true,
        error => this.onHttpError({ message: "Error al eliminar" })
      )
    );
  }

  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
