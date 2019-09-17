import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable } from 'rxjs';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-asociar-actividad',
  templateUrl: './asociar-actividad.component.html'
})
export class AsociarActividadComponent implements OnInit {
  opcionesParametroMockedData: any;

  listaNomencladoresActividad: Observable<Object>;
  
  tipoNomencladorLocal: string;
  tipoParametro: string;
  tiposNomencladoresSelect: Observable<string[]>;
  tiposParametrosSelect: Observable<string[]>;
  
  optionsList = [];

  test:any;

  actividadAsociadaAEnviar ={
    entidadIntermedia : "",
    id: -1,
    parametros: {
      id: "[1]"
    },
    optionsList: this.optionsList
  }


  constructor(private _configuracionService: ConfiguracionService) {
    this.opcionesParametroMockedData = this._configuracionService.getOpcionesParametrotroData();

  }

  ngOnInit() {
    this.listaNomencladoresActividad = this._configuracionService.getListaNomencladores('actividad');
    this.tiposNomencladoresSelect = this._configuracionService.getTiposNomenclador();     
    this.tiposParametrosSelect = this._configuracionService.getTiposNomenclador();     

  }

  actualizarActividad(obj){
    this.actividadAsociadaAEnviar.entidadIntermedia = obj.tipoNomenclador + "Parametro";
    this.actividadAsociadaAEnviar.id = obj.id;
    console.log(obj);
    console.log(this.actividadAsociadaAEnviar);
  }

  actualizar(){
    console.log("actualizar");
    this.actividadAsociadaAEnviar.optionsList = this.optionsList;
  }

  onSubmitAsociacion(form: NgForm) {

    if ( true ) {
      this._configuracionService.postAsociacionForm(this.actividadAsociadaAEnviar).subscribe(
        result => {
          console.log('Enviado.');
          //this.postSuccess = true;
          //this.resetForm();
        },
        error => console.log(error) //this.onHttpError(error)
      );
    } else {
      //this.postError = true;
      //this.postErrorMessage = 'Por favor complete correctamente los campos obligatorios del formulario.';
    }
  }
}
