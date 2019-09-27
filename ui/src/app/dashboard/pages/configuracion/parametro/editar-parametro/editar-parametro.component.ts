import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable, Subscription } from 'rxjs';
import { FormGroup, FormBuilder, Validators, FormArray } from '@angular/forms';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-editar-parametro',
  templateUrl: './editar-parametro.component.html'
})
export class EditarParametroComponent implements OnInit, OnDestroy {

  subscriptions : Subscription[] = [];
  
  editarParametroForm:FormGroup;
  faTrashAlt = faTrashAlt;

 // json con los datos originales
  originalParametroAEditar: any = {
    parametro: {
      cod: 0,
      nombre: "",
      isActiv: false,
    },
    tipoParametro: {
      cod: 2,
      isActiv: false,
      nombre: ""
    },
    tipoDato:{
      cod: 0,
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
  opcionesElegidas = [];
  opcionSeleccionada = {
    cod: null,
    nombre: null
  };

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';
 
  constructor(private activatedRoute: ActivatedRoute,
    private _configuracionService: ConfiguracionService,
    private fb: FormBuilder) {}
    
  ngOnInit() {

    this.subscriptions.push(this.activatedRoute.params.subscribe( params => {
      
      this.subscriptions.push(this._configuracionService.getParametro( params['cod'] ).subscribe(
        (result: any) => {
          this.initForm(result);
        
          this.originalParametroAEditar.parametro.cod = result[0].parametro.cod;
          this.originalParametroAEditar.parametro.nombre = result[0].parametro.nombre;
          this.originalParametroAEditar.parametro.isActiv = result[0].parametro.isActiv;
          
          this.originalParametroAEditar.tipoParametro.cod = result[0].tipoParametro.cod;
          this.originalParametroAEditar.tipoParametro.isActiv = result[0].tipoParametro.isActiv;
          this.originalParametroAEditar.tipoParametro.nombre = result[0].tipoParametro.nombre;
          
          this.originalParametroAEditar.tipoDato.cod = result[0].tipoDato.cod;
          this.originalParametroAEditar.tipoDato.isActiv = result[0].tipoDato.isActiv;
          this.originalParametroAEditar.tipoDato.nombre = result[0].tipoDato.nombre;

          result[0].opcion.forEach(element => {
            this.originalParametroAEditar.opcion.push( { cod:`${element.cod}` });
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
          if( element.cod == this.originalParametroAEditar.tipoParametro.cod ){
            agregarElemento = false;
          }
        });
        if( agregarElemento ){
          let obj = {
            cod: this.originalParametroAEditar.tipoParametro.cod,
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
        for (let index = 0; index < result.length; index++) {
          this.tiposOpcionesSelectArray.push(result[index]);
        }
      }
    ));  

  }
  onHttpError( errorResponse: any ) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  onSubmitParametro() {

    console.warn(this.editarParametroForm.value);

    if( this.editarParametroForm.status == 'VALID' ){
      this._configuracionService.putParametroForm(this.editarParametroForm.value).subscribe(
        result => {
          this.postSuccess = true;
          this.postError = false;
          this.postErrorMessage = '';
          
        },
        error => this.onHttpError(error)
      );
    }
  }
  

  initForm(formValues){
    
    this.editarParametroForm = this.fb.group({
      parametro: this.fb.group({
        cod: [formValues[0].parametro.cod],
        nombre: [formValues[0].parametro.nombre, Validators.required],
        isActiv: [formValues[0].parametro.isActiv],
      }),
      tipoParametro: this.fb.group({
        cod: [formValues[0].tipoParametro.cod, Validators.required],
        nombre: [formValues[0].tipoParametro.nombre],
        isActiv: [formValues[0].tipoParametro.isActiv],
      }),
      tipoDato: this.fb.group({
        cod: [formValues[0].tipoDato.cod, Validators.required],
        nombre: [formValues[0].tipoDato.nombre],
        isActiv: [formValues[0].tipoDato.isActiv],
      }),
      opcion: this.fb.array( formValues[0].opcion.map( element => this.crearOpcion(element) ) ) 
      
    });

    formValues[0].opcion.map( element => {
      this.opcionesElegidas.push({
        cod: element.cod,
        nombre: element.nombre
      });
    } );

  }

  crearOpcion( obj: any){
    return this.fb.control({
          cod: obj.cod,
          nombre: obj.nombre,
          isActiv: obj.isActiv
        })
      ;
  }

    
  updateOpciones(){
    this.editarParametroForm.patchValue({
      opcion: this.fb.array( this.opcionesElegidas.map( element => this.crearOpcion(element) ) ).value
    });
  }

  agregarItem(){
    let obj = {
      cod: this.opcionSeleccionada.cod,
      nombre: this.opcionSeleccionada.nombre
    }
    this.opcionesElegidas.push(obj);

    let arr = this.editarParametroForm.get('opcion')  as FormArray;
    arr.push(this.crearOpcion(obj))

  }

  actualizaropcionSeleccionada(event){
    const selectEl = event.target;
    const attrVal = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const inn = selectEl.options[selectEl.selectedIndex].innerText;
    this.opcionSeleccionada.cod = attrVal;
    this.opcionSeleccionada.nombre = inn;
    
  }

  quitarItem(index){
    let arr = this.editarParametroForm.get('opcion')  as FormArray;
    if (index > -1) {
      arr.removeAt(index);
    }
  }

  ngOnDestroy(){
    this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
  }
}
