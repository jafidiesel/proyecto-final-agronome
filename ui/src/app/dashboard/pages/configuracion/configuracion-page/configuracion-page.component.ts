import { Component, OnInit } from '@angular/core';
import { faCog, faCogs, faList } from '@fortawesome/free-solid-svg-icons';


@Component({
  selector: 'app-configuracion-page',
  templateUrl: './configuracion-page.component.html'
})
export class ConfiguracionPageComponent implements OnInit {
  faCog = faCog;
  faCogs = faCogs;
  faList = faList;

  configurationButtons: any[] = [
    ['Nomencladores', '/configuracion/listarNomencladores', faCog],
    ['Parámetros', '/configuracion/listarParametros', faCogs],
    ['Asociar Actividad', '/configuracion/asociar/listarActividades', faList],
    ['Asociar Recomendaciones', '/configuracion/asociar/listarRecomendaciones', faList],
    ['Asociar Planes', '/configuracion/asociar/listarPlanes', faList],
    ['Asociar Análisis', '/configuracion/asociar/listarAnalisis', faList],

  ];

  constructor() { }

  ngOnInit() {
  }

}
