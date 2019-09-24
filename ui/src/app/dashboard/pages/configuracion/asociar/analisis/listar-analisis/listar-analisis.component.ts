import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-listar-analisis',
  templateUrl: './listar-analisis.component.html',
  styles: []
})
export class ListarAnalisisComponent implements OnInit, OnDestroy {
  
  subscriptions : Subscription[] = [];
  
  // array de rows para table component
  actividadesTabla = [];
  tableDataHeader = ['Nombre Analisis', 'Editar'];
  mostrarTabla:boolean = false;
  
  actividadesMockedData: any;

  constructor(private _configuracionService: ConfiguracionService) {
    //this.actividadesMockedData = this._configuracionService.getActividadData();
   }

  ngOnInit() {
    this.subscriptions.push(this._configuracionService.getListaAsociacion('tipoAnalisisParam').subscribe(
      (result:any) => {
        this.actividadesTabla.push(this.tableDataHeader);

        for (let index = 0; index < result.asociaciones.length ; index++) {
          this.actividadesTabla.push([
          `${result.asociaciones[index].nombre}`,
          `*/configuracion/asociar/editarAnalisis/${result.asociaciones[index].cod}`
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