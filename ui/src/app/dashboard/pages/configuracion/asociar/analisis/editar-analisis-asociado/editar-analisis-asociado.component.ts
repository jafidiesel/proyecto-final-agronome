import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable, Subscription } from 'rxjs';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { FormGroup, FormBuilder, Validators, FormArray } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-editar-analisis-asociado',
  templateUrl: './editar-analisis-asociado.component.html',
  styles: []
})
export class EditarAnalisisAsociadoComponent implements OnInit, OnDestroy {
  subscriptions : Subscription[] = [];

  asociarParametroForm:FormGroup;
  
  nombreNomenclador: string;
  codActividad:number;

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';
  
  faTrashAlt = faTrashAlt;

  // Lista con Parametros
  tiposParametrosSelectArray = [];
  parametroSeleccionado = {
    codParametro: null,
    nombreParametro: null
  };

  constructor(private activatedRoute: ActivatedRoute,
    private _configuracionService: ConfiguracionService,
    private fb: FormBuilder) { }

  ngOnInit() {
    
    this.subscriptions.push(this.activatedRoute.params.subscribe( params => {
      this.codActividad = params['cod'];
      this.subscriptions.push(this._configuracionService.getNomenclador( 'tipoAnalisis', params['cod'] ).subscribe(
        (result:any) => this.nombreNomenclador = result.nombre
      ));


      this.subscriptions.push(this._configuracionService.getAsociacionForm( 'tipoAnalisisParam', params['cod'] ).subscribe(
        (result: any) => {
          this.initForm(result);

        },
        error => console.log(error)
        ));
        
      } ));

      this.subscriptions.push( this._configuracionService.getListaParametrosPorTipo('analisis').subscribe(
        (result:any) =>{
          for (let index = 0; index < result.length; index++) {
            this.tiposParametrosSelectArray.push(result[index]);
          }
        }
      )); 
    
  }


  initForm(result){
    this.asociarParametroForm = this.fb.group({
      parametros: this.fb.array( result.parametros.map( element => this.crearParametro(element) ))
    });
  }
  
  crearParametro( obj: any){
    return this.fb.control({
          codParametro: obj.codParametro,
          nombreParametro: obj.nombreParametro,
          isActiv: true
        })
      ;
  }
  
  agregarItem(){
    let obj = {
      codParametro: this.parametroSeleccionado.codParametro,
      nombreParametro: this.parametroSeleccionado.nombreParametro
    }
    let arr = this.asociarParametroForm.get('parametros')  as FormArray;
    arr.push(this.crearParametro(obj))
  }

  quitarItem(index){
    let arr = this.asociarParametroForm.get('parametros')  as FormArray;
    if (index > -1) {
      arr.removeAt(index);
    }
  }

  actualizarParametroSeleccionado(event){
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const inn = selectEl.options[selectEl.selectedIndex].innerText;
    
    this.parametroSeleccionado.codParametro = attrVal;
    this.parametroSeleccionado.nombreParametro = inn;
    
  }

  onHttpError( errorResponse: any ) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  onSubmitAsociacion() {
    //this.updateOpciones();

    if ( this.asociarParametroForm.status == 'VALID' ) {
      this._configuracionService.putAsociacionForm('tipoAnalisisParam', this.codActividad ,this.asociarParametroForm.value).subscribe(
        result => {
          this.postSuccess = true;

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

  imprimir(){
    console.warn('this.asociarParametroForm.values',this.asociarParametroForm.value);
  }

  ngOnDestroy(){
    this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
  }

}
