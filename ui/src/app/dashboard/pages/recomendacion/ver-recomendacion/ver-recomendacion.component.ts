import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { FormGroup, FormBuilder } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { RecomendacionService } from 'src/app/dashboard/services/recomendacion/recomendacion.service';

@Component({
  selector: 'app-ver-recomendacion',
  templateUrl: './ver-recomendacion.component.html'
})
export class VerRecomendacionComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  actividadForm: FormGroup;
  recomendacionForm: FormGroup;

  actividadLoaded: boolean;
  recomendacionLoaded: boolean;
  codActividad: number;

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private _recomendacionService: RecomendacionService,
    private fb: FormBuilder,
    private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    /* actividad */
    this.subscriptions.push(
      this.activatedRoute.params.subscribe(params => {
        this.subscriptions.push(

          this._recomendacionService.getActividad(params['codAct']).subscribe(
            result => {
              this.codActividad = params['codAct'];
              this.initFormActividad(result);
            },
            error => this.onHttpError({ message: "Error al pedir los datos de la actividad." })
          )
        );

      })
    );
    /* recomendacion */
    this.subscriptions.push(
      this.activatedRoute.params.subscribe(params => {
        this.subscriptions.push(
          this._recomendacionService.getRecomendacion(params['codRec']).subscribe(
            result => {
              this.initFormRecomendacion(result);
            },
            error => this.onHttpError({ message: "Error al pedir los datos de la recomendación." })
          )
        )
      })
    );
  }

  crearParametro(obj: any) {
    return this.fb.control({
      codParam: obj.codParametro,
      valor: obj.valor,
      nombre: obj.nombreParametro.toLowerCase()
    });
  }


  initFormActividad(form) {
    this.actividadForm = this.fb.group({
      codActividad: form.actividad.codActividad,
      nombreActividad: form.actividad.nombreActividad,
      fchActivDetalle: form.fchActivDetalle,
      observacion: form.observacion,
      imagen: [{}],
      parametro: this.fb.array(form.parametro.map(element => this.crearParametro(element)))

    });
    this.actividadLoaded = true;
  }

  initFormRecomendacion(form) {
    this.recomendacionForm = this.fb.group({
      codRecomDetalle: form.codRecomDetalle,
      nombreRecomendacion: form.recomendacion.nombreRecomendacion,
      fchRecomDetalle: form.fchRecomDetalle,
      observacion: form.observacion,
      nombreUsuario: form.usuario.nombreUsuario,
      parametro: this.fb.array(form.parametro.map(element => this.crearParametro(element)))

    });
    this.recomendacionLoaded = true;
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
