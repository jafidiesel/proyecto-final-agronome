import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth/auth.service';
import { PlanificacionService } from 'src/app/dashboard/services/planificacion/planificacion.service';
import Swal from 'sweetalert2';
import { Router, ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { FormGroup, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-planificacion-supervisada',
  templateUrl: './planificacion-supervisada.component.html',
})

export class PlanificacionSupervisadaComponent implements OnInit {

  rol: string;
  codFinca: number;
  subscriptions: Subscription[] = [];

  // formgroup
  planificacionInicialForm: FormGroup;
  planificacionSupervisadaForm: FormGroup;

  tipoCultivoArray = [];

  tableDataHeader = ['Parcela', 'Cuadros']
  parcelaArray = []

  habilitarSupervisar = false;

  // banderas de error
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(
    private auth: AuthService,
    private _planificacionService: PlanificacionService,
    private _configuracionService: ConfiguracionService,
    private router: Router,
    private fb: FormBuilder,
    private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    this.codFinca = parseInt(this.auth.getCurrentCodFinca());
    this.rol = this.auth.getRol();

    this.subscriptions.push(
      this._configuracionService.getListaNomencladoresConFiltro('tipoCultivo', true).subscribe(
        (result: any) => {
          result.map(element => {
            this.tipoCultivoArray.push([element.cod, element.nombre])
          });
        },
        error => this.onHttpError({ message: error.error.message })
      )
    );

    this.subscriptions.push(
      this.activatedRoute.params.subscribe(params => {
        this._planificacionService.getPlanificacionesCreadas(this.codFinca, parseInt(params['cod'])).subscribe(
          result => {
            this.initForm(result);
          },
          error => this.onHttpError({ message: error.error.message })
        )

      })
    );



  }

  supervisar() {
    this.habilitarSupervisar = true;
  }

  procesarFormGroup() {
    let form = this.planificacionSupervisadaForm.value;
    this.planificacionSupervisadaForm.patchValue({
      cultivos: [{
        codTipoCultivo: parseInt(form.codTipoCultivo),
        cantidadCultivo: form.cantidadCultivo,
        produccionEsperada: form.produccionEsperada,
        variedadCultivo: form.variedadCultivo,
        cicloUnico: form.cicloUnico,
        parcelas: form.cultivos.parcelas
      }]

    });
  }

  initForm(form) {
    this.planificacionInicialForm = this.fb.group({
      action: "i",
      codPlanifBefore: null,
      codFinca: this.codFinca,
      comentario: null,
      codTipoCultivo: form.inicial.cultivo[0].tipoCultivo.cod,
      nombreTipoCultivo: form.inicial.cultivo[0].tipoCultivo.nombre,
      variedadCultivo: form.inicial.cultivo[0].variedadCultivo,
      cantidadCultivo: 0,
      produccionEsperada: form.inicial.cultivo[0].produccionEsperada,
      cicloUnico: form.inicial.cultivo[0].cicloUnico,
      cultivos: [{
        parcelas: form.inicial.cultivo[0].grupos.map(parcela => {
          return {
            nombreParcela: parcela.parcelas[0].nombreParcela,
            codParcela: parcela.parcelas[0].codParcela,
            cuadros:
              parcela.parcelas[0].cuadros.map(cuadro => {
                return { codCuadro: cuadro.codCuadro, nombreCuadro: cuadro.nombreCuadro }
              })
          }
        }),
      }]
    });


    this.planificacionSupervisadaForm = this.fb.group({
      action: "s",
      codPlanifBefore: form.inicial.cod,
      codFinca: this.codFinca,
      comentario: null,
      codTipoCultivo: form.inicial.cultivo[0].tipoCultivo.cod,
      variedadCultivo: form.inicial.cultivo[0].variedadCultivo,
      cantidadCultivo: 0,
      produccionEsperada: form.inicial.cultivo[0].produccionEsperada,
      cicloUnico: form.inicial.cultivo[0].cicloUnico,
      cultivos: [{
        parcelas: form.inicial.cultivo[0].grupos.map(parcela => {
          return {
            nombreParcela: parcela.parcelas[0].nombreParcela,
            codParcela: parcela.parcelas[0].codParcela,
            cuadros:
              parcela.parcelas[0].cuadros.map(cuadro => {
                return { codCuadro: cuadro.codCuadro, nombreCuadro: cuadro.nombreCuadro }
              })

          }
        }),
      }]
    });
  }

  onSubmit() {

    this.procesarFormGroup();


    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
      },
      buttonsStyling: false
    })

    //return false;
    this.subscriptions.push(
      this._planificacionService.guardarPlanificacion(this.planificacionSupervisadaForm.value).subscribe(
        result => {
          swalWithBootstrapButtons.fire({
            title: '¡Exito!',
            text: result.message,
            type: 'success',
            confirmButtonText: 'Salir',
            reverseButtons: true
          }).then((result) => {
            if (result.value) {
              this.router.navigate(['planificacion/verPlanificacionSupervisada']);
            }
          });

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
