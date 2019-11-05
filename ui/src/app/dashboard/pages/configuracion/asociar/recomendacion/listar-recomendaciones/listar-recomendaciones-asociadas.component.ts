import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-listar-recomendaciones-asociadas',
  templateUrl: './listar-recomendaciones-asociadas.component.html',
})
export class ListarRecomendacionesAsociadasComponent implements OnInit, OnDestroy {
  subscriptions : Subscription[] = [];
  
  // array de rows para table component
  recomendacionesTabla = [];
  tableDataHeader = ['Nombre Recomendacion', 'Editar'];
  mostrarTabla:boolean = false;
  

  constructor(private _configuracionService: ConfiguracionService) {}

  ngOnInit() {
    this.subscriptions.push(this._configuracionService.getListaAsociacion('recomendacionParametro').subscribe(
      (result:any) => {
        this.recomendacionesTabla.push(this.tableDataHeader);

        for (let index = 0; index < result.asociaciones.length ; index++) {
          this.recomendacionesTabla.push([
          `${result.asociaciones[index].nombre}`,
          `*/configuracion/asociar/editarRecomendacion/${result.asociaciones[index].cod}`
        ]);
        }
        this.mostrarTabla = true;
      },
      error => console.error(error)
    ));
  }

  ngOnDestroy(){
    this.subscriptions.forEach( (subscription) => subscription.unsubscribe() );
  }
}
