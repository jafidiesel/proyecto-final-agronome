import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable, Subscription } from 'rxjs';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-asociar-analisis',
  templateUrl: './asociar-analisis.component.html',
  styles: []
})
export class AsociarAnalisisComponent implements OnInit, OnDestroy {
  opcionesParametroMockedData: any;
  subscriptions : Subscription[] = [];

  asociarParametroForm:FormGroup;
  
  faTrashAlt = faTrashAlt;

  // Valores dropdown nomenclador
  listaNomencladoresActividad: Observable<Object>;
  listaNomencladoresActividadArray = [];

  // Lista con opciones
  tiposParametrosSelect: Observable<object>;
  tiposParametrosSelectArray = [];
  parametrosElegidos = [];
  parametroSeleccionado = {
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
    this.initForm(this.asociarParametroForm);

    this.subscriptions.push(this._configuracionService.getListaAsociacion('tipoAnalisisParam').subscribe(
      result => {

        for (let index = 0; index < result.sinAsociaciones.length; index++) {
          const element = result.sinAsociaciones[index];
          this.listaNomencladoresActividadArray.push(element);
          
        }
      }
    ));

    this.subscriptions.push( this._configuracionService.getListaParametrosPorTipo('analisis').subscribe(
      (result:any) =>{
        for (let index = 0; index < result.length; index++) {
          this.tiposParametrosSelectArray.push(result[index]);
        }
      }
    )); 

  }

  initForm(formValues){
      
    this.asociarParametroForm = this.fb.group({
      entidadIntermedia: ['tipoAnalisisParam'],
      id: [null, Validators.required], // id nomenclador actividad
      parametros: this.fb.group({
        id: [null, Validators.required]
      }),
    });
  }

  onHttpError( errorResponse: any ) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  actualizarNomencladorActividad(event){
    // This is ducktape, do not usit at home
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    this.asociarParametroForm.patchValue({
      id: attrVal
    });

    console.log('this.asociarParametroForm',this.asociarParametroForm);
  }

  actualizarParametroSeleccionado(event){
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const inn = selectEl.options[selectEl.selectedIndex].innerText;
    
    this.parametroSeleccionado.id = attrVal;
    this.parametroSeleccionado.nombre = inn;
    
  }

  updateOpciones(){
    this.asociarParametroForm.patchValue({
      parametros: {
        id: "[" + this.parametrosElegidos.map( element => {return element.id} ) + "]"
      }
    });
    
  }

  agregarItem(){
    let obj = {
      id: this.parametroSeleccionado.id,
      nombre: this.parametroSeleccionado.nombre
    }
    this.parametrosElegidos.push(obj);

    this.updateOpciones();

  }

  quitarItem(itemARemover){
    this.parametrosElegidos.forEach( (item, index) => {
      if(item === itemARemover) {
        this.parametrosElegidos.splice(index,1);
      }
    }); 
  }

  onSubmitAsociacion() {
    this.updateOpciones();

    if ( this.asociarParametroForm.status == 'VALID' ) {
      this._configuracionService.postAsociacionForm(this.asociarParametroForm.value).subscribe(
        result => {
          console.log('Enviado.');
          this.postSuccess = true;

          this.asociarParametroForm.controls['id'].disable();
          //this.asociarParametroForm.controls['id'].disable();
        },
        error => console.log(error) //this.onHttpError(error)
      );
    } else {
      this.postError = true;
      this.postSuccess = false;
      this.postErrorMessage = 'Por favor complete correctamente los campos obligatorios del formulario.';
    }
  }

  imprimir(){
    console.warn('this.asociarParametroForm.values',this.asociarParametroForm.value);
  }

  ngOnDestroy(){
    this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
  }
}
