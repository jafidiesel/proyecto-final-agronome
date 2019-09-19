import { Component, OnInit } from '@angular/core';
import { ConfiguracionService } from 'src/app/dashboard/services/configuracion/configuracion.service';

@Component({
  selector: 'app-editar-actividad-asociada',
  templateUrl: './editar-actividad-asociada.component.html'
})
export class EditarActividadAsociadaComponent implements OnInit {

  constructor(private _configuracionService: ConfiguracionService) { }

  ngOnInit() {
  }

}
