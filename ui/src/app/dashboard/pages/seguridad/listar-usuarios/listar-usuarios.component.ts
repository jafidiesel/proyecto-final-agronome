import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { SeguridadService } from 'src/app/dashboard/services/seguridad.service';
import { formatDate } from "@angular/common";

@Component({
  selector: 'app-listar-usuarios',
  templateUrl: './listar-usuarios.component.html'
})
export class ListarUsuariosComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  // array de rows para table component
  usuariosTabla = [];
  tableDataHeader = ['Usuario', 'Nombre', 'Apellido', 'Email', 'Fecha Creación', 'Activo', 'Rol', 'Editar'];
  mostrarTabla: boolean = false;

  format = 'MM-dd-yyyy';
  locale = 'en-US';
  

  constructor(private _seguridadService: SeguridadService) { }

  ngOnInit() {

    this.subscriptions.push(this._seguridadService.getUsuarios().subscribe(
      (result: any) => {
        this.usuariosTabla.push(this.tableDataHeader);

        for (let index = 0; index < result.length; index++) {
          console.log(result[index].fchCrea);
          this.usuariosTabla.push([
            `${result[index].usuario}`,
            `${result[index].nombre}`,
            `${result[index].apellido}`,
            `${result[index].email}`,
            /* formatDate(`${result[index].fchCrea}`, this.format, this.locale), */
            `${result[index].fchCrea}`,
            `${result[index].isActiv}`,
            `${result[index].rol.nombre}`,
            `*/seguridad/editarUsuario/${result[index].cod}`
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
