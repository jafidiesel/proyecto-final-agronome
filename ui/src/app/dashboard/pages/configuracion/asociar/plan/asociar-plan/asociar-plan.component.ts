import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable, Subscription } from 'rxjs';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';


@Component({
  selector: 'app-asociar-plan',
  templateUrl: './asociar-plan.component.html',
  styles: []
})
export class AsociarPlanComponent implements OnInit, OnDestroy {

  subscriptions : Subscription[] = [];

  asociarParametroForm:FormGroup;
  
  faTrashAlt = faTrashAlt;

  // Valores dropdown nomenclador
  listaNomencladoresPlan: Observable<Object>;
  listaNomencladoresPlanArray = [];

  // Lista con opciones
  tiposParametrosSelect: Observable<object>;
  tiposParametrosSelectArray = [];
  parametrosElegidos = [];
  parametroSeleccionado = {
    cod: null,
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
    this.initForm();

    this.subscriptions.push(this._configuracionService.getListaAsociacion('tipoPlanParam').subscribe(
      result => {

        for (let index = 0; index < result.sinAsociaciones.length; index++) {
          const element = result.sinAsociaciones[index];
          this.listaNomencladoresPlanArray.push(element);
          
        }
      }
    ));

    this.subscriptions.push( this._configuracionService.getListaParametrosPorTipo('plan').subscribe(
      (result:any) =>{
        for (let index = 0; index < result.length; index++) {
          this.tiposParametrosSelectArray.push(result[index]);
        }
      }
    )); 

  }

  initForm(){
      
    this.asociarParametroForm = this.fb.group({
      entidadIntermedia: ['tipoPlanParam'],
      cod: [null, Validators.required], // cod nomenclador actividad
      parametros: this.fb.group({
        cod: [null, Validators.required]
      }),
    });
  }

  onHttpError( errorResponse: any ) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  actualizarNomencladorPlan(event){
    // This is ducktape, do not usit at home
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    this.asociarParametroForm.patchValue({
      cod: attrVal
    });
  }

  actualizarParametroSeleccionado(event){
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const inn = selectEl.options[selectEl.selectedIndex].innerText;
    
    this.parametroSeleccionado.cod = attrVal;
    this.parametroSeleccionado.nombre = inn;
    
  }

  updateParametros(){
    this.asociarParametroForm.patchValue({
      parametros: {
        cod: "[" + this.parametrosElegidos.map( element => {return element.cod} ) + "]"
      }
    });
    
  }

  agregarItem(){
    let obj = {
      cod: this.parametroSeleccionado.cod,
      nombre: this.parametroSeleccionado.nombre
    }
    this.parametrosElegidos.push(obj);

    this.updateParametros();

  }

  quitarItem(itemARemover){
    this.parametrosElegidos.forEach( (item, index) => {
      if(item === itemARemover) {
        this.parametrosElegidos.splice(index,1);
      }
    }); 
  }

  onSubmitAsociacion() {
    this.updateParametros();

    if ( this.asociarParametroForm.status == 'VALID' ) {
      this._configuracionService.postAsociacionForm(this.asociarParametroForm.value).subscribe(
        result => {
          console.log('Enviado.');
          this.postSuccess = true;

          this.asociarParametroForm.controls['cod'].disable();
          //this.asociarParametroForm.controls['cod'].disable();
        },
        error => this.onHttpError(error)
      );
    } else {
      this.postError = true;
      this.postSuccess = false;
      this.postErrorMessage = 'Por favor complete correctamente los campos obligatorios del formulario.';
    }
  }

  ngOnDestroy(){
    this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
  }
}
