import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable, Subscription } from 'rxjs';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-asociar-actividad',
  templateUrl: './asociar-actividad.component.html'
})
export class AsociarActividadComponent implements OnInit, OnDestroy {
  opcionesParametroMockedData: any;
  subscriptions : Subscription[] = [];

  crearParametroForm:FormGroup;
  
  faTrashAlt = faTrashAlt;

  // Valores dropdown nomenclador
  listaNomencladoresActividad: Observable<Object>;
  listaNomencladoresActividadArray = [];

  // Lista con opciones
  tiposParametrosSelect: Observable<object>;
  tiposParametrosSelectArray = [];
  parametrosElegidos = [];
  parametroSeleccionada = {
    id: null,
    nombre: null
  };

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private _configuracionService: ConfiguracionService,
    private fb: FormBuilder) {
  }

  ngOnInit() {
    this.initForm(this.crearParametroForm);
    this.subscriptions.push(this._configuracionService.getListaNomencladoresConFiltro('actividad', true).subscribe(
      result => {
        console.log('result',result);

        for (let index = 0; index < result.length; index++) {
          const element = result[index];
          this.listaNomencladoresActividadArray.push(element);
          
        }
      }
    ));

    this.subscriptions.push( this._configuracionService.getListaParametros().subscribe(
      (result:any) =>{
        //this.tiposParametrosSelectArray.push(result);
        for (let index = 0; index < result.length; index++) {
          this.tiposParametrosSelectArray.push(result[index]);
        }
      }
    )); 

  }

 /*  {
    "entidadIntermedia": "actividadParametro",
    "id": 1,
    "parametros": {
        "id": "[9]"
    }
} */

  initForm(formValues){
      
    this.crearParametroForm = this.fb.group({
      entidadIntermedia: ['actividadParametro'],
      id: null,
      parametros: this.fb.group({
        id: null,
        nombre: ['', Validators.required],
        isActiv: [false],
      }),
      
    });
  }

  actualizarActividad(obj){
  }

  actualizar(){
  }

  onSubmitAsociacion() {

    /* if ( true ) {
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
    } */
  }

  imprimir(){
    console.warn('this.crearParametroForm.value',this.crearParametroForm.value);
  }

  ngOnDestroy(){
    this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
  }
}
