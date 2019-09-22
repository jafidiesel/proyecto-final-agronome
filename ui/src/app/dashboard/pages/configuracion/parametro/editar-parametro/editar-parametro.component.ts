import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable, Subscription } from 'rxjs';
import { NgForm, FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-editar-parametro',
  templateUrl: './editar-parametro.component.html'
})
export class EditarParametroComponent implements OnInit, OnDestroy {

  subscriptions : Subscription[] = [];
  
  editarParametroForm:FormGroup;

 // json con los datos originales
  originalParametroAEditar: any = {
    parametro: {
      id: 0,
      nombre: "",
      isActiv: false,
    },
    tipoParametro: {
      id: 2,
      isActiv: false,
      nombre: ""
    },
    tipoDato:{
      id: 0,
      isActiv: false,
      nombre: ""
    },
    opcion: []
  };

  // Dropdown tipoParametro
  tiposParametrosSelect: Observable<Object>;
  tiposParametrosSelectArray =[];

  // Dropdown tipoDato
  tiposDatosSelect: Observable<Object>;
  tiposDatosSelectArray =[];

  // Lista con opciones
  tiposOpcionesSelect: Observable<object>;
  tiposOpcionesSelectArray = [];

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';
 
  constructor(private activatedRoute: ActivatedRoute,
    private _configuracionService: ConfiguracionService,
    private fb: FormBuilder) {}
    
  ngOnInit() {

    this.subscriptions.push(this.activatedRoute.params.subscribe( params => {
      
      this.subscriptions.push(this._configuracionService.getParametro( params['id'] ).subscribe(
        (result: any) => {
          this.initForm(result);
        
          this.originalParametroAEditar.parametro.id = result[0].parametro.cod;
          this.originalParametroAEditar.parametro.nombre = result[0].parametro.nombre;
          this.originalParametroAEditar.parametro.isActiv = result[0].parametro.isActiv;
          
          this.originalParametroAEditar.tipoParametro.id = result[0].tipoParametro.cod;
          this.originalParametroAEditar.tipoParametro.isActiv = result[0].tipoParametro.isActiv;
          this.originalParametroAEditar.tipoParametro.nombre = result[0].tipoParametro.nombre;
          
          this.originalParametroAEditar.tipoDato.id = result[0].tipoDato.cod;
          this.originalParametroAEditar.tipoDato.isActiv = result[0].tipoDato.isActiv;
          this.originalParametroAEditar.tipoDato.nombre = result[0].tipoDato.nombre;

          result[0].opcion.forEach(element => {
            this.originalParametroAEditar.opcion.push( { id:`${element.cod}` });
          });

          
        },
      error => console.log(error)
      ));
      
    } ));

    this.subscriptions.push(this._configuracionService.getListaNomencladoresConFiltro('tipoParametro',true).subscribe(
      result => {
        for (let index = 0; index < result.length; index++) {
          const element:any = result[index];
          this.tiposParametrosSelectArray.push(element);            
        }

        // Si el elemento no esta dentro de los activos, lo agrega al dropdown
        let agregarElemento = true;
        this.tiposParametrosSelectArray.forEach(element => {
          if( element.id == this.originalParametroAEditar.tipoParametro.id ){
            agregarElemento = false;
          }
        });
        if( agregarElemento ){
          let obj = {
            id: this.originalParametroAEditar.tipoParametro.id,
            isActiv: this.originalParametroAEditar.tipoParametro.isActiv,
            nombre: this.originalParametroAEditar.tipoParametro.nombre,
          }
          this.tiposParametrosSelectArray.push(obj);
        }

      }
    ));


    this.subscriptions.push(this._configuracionService.getListaNomencladoresConFiltro('tipoDato',true).subscribe(
      result => {
        for (let index = 0; index < result.length; index++) {
          const element:any = result[index];
          this.tiposDatosSelectArray.push(element);
          
        }

        // Si el elemento no esta dentro de los activos, lo agrega al dropdown
        /* let agregarElemento = true;
        this.tiposDatosSelectArray.forEach(element => {
          if( element.id == this.originalParametroAEditar.tipoDato.id ){
            agregarElemento = false;
          }
        });
        if( agregarElemento ){
          let obj = {
            id: this.originalParametroAEditar.tipoDato.id,
            isActiv: this.originalParametroAEditar.tipoDato.isActiv,
            nombre: this.originalParametroAEditar.tipoDato.nombre,
          }
          this.tiposDatosSelectArray.push(obj);
        } */
      }
    ));

    this.subscriptions.push( this._configuracionService.getListaNomencladoresConFiltro('opcion', true).subscribe(
      result =>{
        //this.tiposOpcionesSelectArray.push(result);
        console.log(result.length);
        for (let index = 0; index < result.length; index++) {
          console.log(this.tiposOpcionesSelect);
          this.tiposOpcionesSelectArray.push(result[index]);
        }
        console.log(this.tiposOpcionesSelectArray);
      }
    ));  

  }
    onHttpError( errorResponse: any ) {
      console.log(errorResponse);
      this.postError = true;
      this.postSuccess = false;
      this.postErrorMessage = errorResponse.error.messages;
    }
  
    onSubmitParametro() {

      console.warn(this.editarParametroForm.value);

      if( this.editarParametroForm.status == 'VALID' ){
        this._configuracionService.postParametroForm(this.editarParametroForm.value).subscribe(
          result => {
            console.log('Enviado.');
            
          },
          error => this.onHttpError(error)
        );
      }
    }
  

    initForm(formValues){
      
      this.editarParametroForm = this.fb.group({
        parametro: this.fb.group({
          id: [formValues[0].parametro.cod],
          nombre: [formValues[0].parametro.nombre, Validators.required],
          isActiv: [formValues[0].parametro.isActiv],
        }),
        tipoParametro: this.fb.group({
          id: [formValues[0].tipoParametro.cod, Validators.required],
          nombre: [formValues[0].tipoParametro.nombre],
          isActiv: [formValues[0].tipoParametro.isActiv],
        }),
        tipoDato: this.fb.group({
          id: [formValues[0].tipoDato.cod, Validators.required],
          nombre: [formValues[0].tipoDato.nombre],
          isActiv: [formValues[0].tipoDato.isActiv],
        }),
        opcion: this.fb.array( formValues[0].opcion.map( element => this.crearOpcion(element) ) ) 
        
      });
      console.log('editarParametroForm',this.editarParametroForm.value);
      console.log('form',this.editarParametroForm);
    }

    crearOpcion( obj: any){
      
      
      return this.fb.control({
            id: obj.cod,
            nombre: obj.nombre,
            isActiv: obj.isActiv
          })
        ;
      }



    ngOnDestroy(){
      this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
    }
}
