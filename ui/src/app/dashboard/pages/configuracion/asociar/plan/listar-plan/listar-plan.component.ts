import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-listar-plan',
  templateUrl: './listar-plan.component.html',
  styles: []
})
export class ListarPlanComponent implements OnInit, OnDestroy {
  
  subscriptions : Subscription[] = [];
  
  // array de rows para table component
  planesTabla = [];
  tableDataHeader = ['Nombre Plan', 'Editar'];
  mostrarTabla:boolean = false;
  

  constructor(private _configuracionService: ConfiguracionService) {}

  ngOnInit() {
    this.subscriptions.push(this._configuracionService.getListaAsociacion('tipoPlanParam').subscribe(
      (result:any) => {
        this.planesTabla.push(this.tableDataHeader);

        for (let index = 0; index < result.asociaciones.length ; index++) {
          this.planesTabla.push([
          `${result.asociaciones[index].nombre}`,
          `*/configuracion/asociar/editarPlan/${result.asociaciones[index].cod}`
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
