import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Observable } from 'rxjs';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-editar-parametro',
  templateUrl: './editar-parametro.component.html'
})
export class EditarParametroComponent implements OnInit {

 // json con los datos originales
 originalParametroAEditar: any = {
   parametro: {
     id: 0,
     nombre: "",
     isActiv: false,
   },
   tipoParametro: {
     id: 0,
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

 // json a enviar para PUT
 parametroAEditar = {};

  // Dropdown tipoParametro
  tiposParametrosSelect: Observable<Object>;
  tiposParametrosSelectArray =[];

  // Dropdown tipoDato
  tiposDatosSelect: Observable<Object>;
  tiposDatosSelectArray =[];

 
  constructor(private activatedRoute: ActivatedRoute,
    private _configuracionService: ConfiguracionService) {
      this.parametroAEditar = { ...this.originalParametroAEditar };
      this.activatedRoute.params.subscribe( params => {
        this._configuracionService.getParametro(params['id'] ).subscribe(
          (result: any) => {
            console.log(result);

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

            
            this.parametroAEditar = { ...this.originalParametroAEditar };
            
          },
        error => console.log(error)
        );
        
      } );
        
    }

    ngOnInit() {
      this._configuracionService.getListaNomencladoresConFiltro('tipoParametro',true).subscribe(
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
          console.log(this.tiposParametrosSelectArray.length);
          document.querySelectorAll('#tipoParametro option')
            .forEach( (element:any) =>{
              console.log(element.value); 
            });
        }
      );


      this._configuracionService.getListaNomencladoresConFiltro('tipoDato',true).subscribe(
        result => {
          for (let index = 0; index < result.length; index++) {
            const element:any = result[index];
            this.tiposDatosSelectArray.push(element);
            
          }

          // Si el elemento no esta dentro de los activos, lo agrega al dropdown
          let agregarElemento = true;
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
            this.tiposParametrosSelectArray.push(obj);
          }
        }
      );

    }
    onHttpError( errorResponse: any ) {
      console.log(errorResponse);
     /*  this.postError = true;
      this.postSuccess = false;
      this.postErrorMessage = errorResponse.error.messages */
    }
  
    onSubmitNomenclador(form: NgForm) {
/* 
      if ( form.controls.nombre.value ) {
        this._configuracionService.putNomencladorForm(this.parametroAEditar).subscribe(
          result => {
            console.log('Enviado.');
            this.postSuccess = true;
            this.resetForm();
          },
          error => this.onHttpError(error)
        );
      } else {
        this.postError = true;
        this.postErrorMessage = 'Por favor complete correctamente los campos obligatorios del formulario.';
      } */
    }
  

    resetForm() {
      /* this.parametroAEditar.nombre = '';
      this.parametroAEditar.isActiv = false; */
      //this.parametroAEditar.tipoNomenclador = '';
    }

}
