import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-listar-parametros',
  templateUrl: './listar-parametros.component.html'
})
export class ListarParametrosComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];


  // array de rows para table component
  nomencladoresTabla = [];
  tableDataHeader = ['Nombre', 'Activo', 'Editar'];
  mostrarTabla: boolean = false;

  constructor(private _configuracionService: ConfiguracionService) { }

  ngOnInit() {

    this.subscriptions.push(this._configuracionService.getListaParametros().subscribe(
      (result: any) => {
        this.nomencladoresTabla.push(this.tableDataHeader);

        for (let index = 0; index < result.length; index++) {
          this.nomencladoresTabla.push([
            `${result[index].nombre}`,
            `${result[index].isActiv}`,
            `*/configuracion/editarParametro/${result[index].cod}`
          ]);
        }
        this.mostrarTabla = true;
      },
      error => console.error(error)
    ));
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
