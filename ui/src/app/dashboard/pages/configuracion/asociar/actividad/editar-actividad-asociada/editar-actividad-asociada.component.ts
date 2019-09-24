import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable, Subscription } from 'rxjs';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { FormGroup, FormBuilder, Validators, FormArray } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-editar-actividad-asociada',
  templateUrl: './editar-actividad-asociada.component.html'
})
export class EditarActividadAsociadaComponent implements OnInit {
  subscriptions : Subscription[] = [];

  asociarParametroForm:FormGroup;
  
  nombreNomenclador: string;
  idActividad:number;

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';
  
  faTrashAlt = faTrashAlt;

  // Lista con Parametros
  tiposParametrosSelectArray = [];
  parametroSeleccionado = {
    idParametro: null,
    nombreParametro: null
  };

  constructor(private activatedRoute: ActivatedRoute,
    private _configuracionService: ConfiguracionService,
    private fb: FormBuilder) { }

  ngOnInit() {
    
    this.subscriptions.push(this.activatedRoute.params.subscribe( params => {
      this.idActividad = params['id'];
      this.subscriptions.push(this._configuracionService.getNomenclador( 'actividad', params['id'] ).subscribe(
        (result:any) => this.nombreNomenclador = result.nombre
      ));


      this.subscriptions.push(this._configuracionService.getAsociacionForm( 'actividadParametro', params['id'] ).subscribe(
        (result: any) => {
          this.initForm(result);

        },
        error => console.log(error)
        ));
        
      } ));

      this.subscriptions.push( this._configuracionService.getListaParametros().subscribe(
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
    console.log('initform',this.asociarParametroForm)
  }
  
  crearParametro( obj: any){
    let codigo;
    if(obj.codParametro == null){
      codigo = obj.idParametro;
    }else {
      codigo = obj.codParametro
    }
    return this.fb.control({
          idParametro: codigo,
          nombreParametro: obj.nombreParametro,
          isActiv: true
        })
      ;
  }
  
  agregarItem(){
    debugger;
    let obj = {
      idParametro: this.parametroSeleccionado.idParametro,
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
    
    this.parametroSeleccionado.idParametro = attrVal;
    this.parametroSeleccionado.nombreParametro = inn;
    
  }

  onHttpError( errorResponse: any ) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  onSubmitAsociacion() {
    //this.updateOpciones();
    console.log(this.asociarParametroForm.value);

    if ( this.asociarParametroForm.status == 'VALID' ) {
      this._configuracionService.putAsociacionForm('actividadParametro', this.idActividad ,this.asociarParametroForm.value).subscribe(
        result => {
          console.log('Enviado.');
          this.postSuccess = true;

          this.asociarParametroForm.controls['id'].disable();
          
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
