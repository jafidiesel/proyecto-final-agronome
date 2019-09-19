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
    ['Asociar Recomendaciones', '/configuracion/listarRecomendaciones'],
    ['Asociar Planes', '/configuracion/listarPlanes'],
    ['Asociar Análisis', '/configuracion/listarAnalisis'],

  ];

  constructor() { }

  ngOnInit() {
  }

}
