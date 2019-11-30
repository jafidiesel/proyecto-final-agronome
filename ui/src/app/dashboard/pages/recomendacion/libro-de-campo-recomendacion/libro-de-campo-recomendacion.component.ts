import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { ActividadService } from 'src/app/dashboard/services/actividad/actividad.service';
import { AuthService } from 'src/app/auth/auth.service';
import { RecomendacionService } from 'src/app/dashboard/services/recomendacion/recomendacion.service';

@Component({
  selector: 'app-libro-de-campo-recomendacion',
  templateUrl: './libro-de-campo-recomendacion.component.html'
})
export class LibroDeCampoRecomendacionComponent implements OnInit, OnDestroy {

  // variables de finca
  codFinca: number;

  // variables de libro de campo
  librosDeCampo = [];

  subscriptions: Subscription[] = [];

  // error flags 
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private _recomendacionService: RecomendacionService,
    private auth: AuthService) { }

  ngOnInit() {

    this.codFinca = parseInt(this.auth.getCurrentCodFinca());

    this.subscriptions.push(
      this._recomendacionService.getLibrosCampoRecomendacion(this.codFinca).subscribe(
        result => {
          result.map(finca => {
            this.librosDeCampo.push({
              codLibroCampo: finca.codLibroCampo,
              nombreLibroCampo: finca.nombreLibroCampo,
              fchIni: finca.fchIni.slice(0, 10) ,
              fchFin: finca.fchFin.slice(0, 10) ,
              nombreTipoCultivo: finca.cultivo.nombreTipoCultivo ,
              variedadCultivo: finca.cultivo.variedadCultivo ,
              actvidadesARecomendar: finca.actvidadesARecomendar ,
              actividadesRecomendadas: finca.actividadesRecomendadas,
              url: `/recomendaciones/listarRecomendaciones/${finca.codLibroCampo}`  
            });
          });
        },
        error => this.onHttpError({ message: "Error al recuperar los libros de campo" })
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
