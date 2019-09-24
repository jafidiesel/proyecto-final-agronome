import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-configuracion-page',
  templateUrl: './configuracion-page.component.html'
})
export class ConfiguracionPageComponent implements OnInit {
  configurationButtons: any[] = [
    ['Nomencladores', '/configuracion/listarNomencladores'],
    ['Parámetros', '/configuracion/listarParametros'],
    ['Asociar Actividad', '/configuracion/asociar/listarActividades'],
    ['Asociar Recomendaciones', '/configuracion/asociar/listarRecomendaciones'],
    ['Asociar Planes', '/configuracion/asociar/listarPlanes'],
    ['Asociar Análisis', '/configuracion/asociar/listarAnalisis'],

  ];

  constructor() { }

  ngOnInit() {
  }

}
