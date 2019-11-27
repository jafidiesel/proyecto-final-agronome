import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { ActividadService } from 'src/app/dashboard/services/actividad/actividad.service';
import { AuthService } from 'src/app/auth/auth.service';

@Component({
  selector: 'app-libro-de-campo',
  templateUrl: './libro-de-campo.component.html'
})
export class LibroDeCampoComponent implements OnInit, OnDestroy {

  // variables de finca
  codFinca: number;

  // variables de libro de campo
  librosDeCampo = [];

  subscriptions: Subscription[] = [];

  // error flags 
  postSuccess = false;
  postError = false;
  postErrorMessage = '';


  // TODO: please refactor this, for the love of Ada, please

  cantLC: any[] = [1, 2];

  /*  [
     {
         "codLibroCampo": 1,
         "nombreLibroCampo": "Tomate BC",
         "fchIni": "24-11-2019 00:00:00",
         "fchFin": "",
         "cultivo": {
             "cod": 1,
             "cantidadCultivo": 2,
             "produccionEsperada": 3.0,
             "variedadCultivo": "perita",
             "cicloUnico": true,
             "codTipoCultivo": 1,
             "nombreTipoCultivo": "tomate"
         }
     }
 ] */

  constructor(private _actividadService: ActividadService,
    private auth: AuthService) { }

  ngOnInit() {
    this.codFinca = this.auth.getcodFinca();

    this.subscriptions.push(
      this._actividadService.getLibrosCampoRecomendacion(this.codFinca).subscribe(
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
              url: `/actividades/listarActividades/${finca.codLibroCampo}`  
            });
          });
        },
        error => this.onHttpError({ message: "Error al recuperar los libros de campo" })
      )
    );


  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }

  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

}
