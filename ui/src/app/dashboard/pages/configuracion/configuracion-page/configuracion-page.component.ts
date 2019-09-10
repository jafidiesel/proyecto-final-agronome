import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-configuracion-page',
  templateUrl: './configuracion-page.component.html'
})
export class ConfiguracionPageComponent implements OnInit {
  configurationButtons: any[] = [
    ['Nomencladores', '/configuracion/listarNomencladores'],
    ['Parámetros', '/configuracion/listarParametros'],
    ['Actividad', '/configuracion/listarActividades'],
    ['Recomendaciones', '/configuracion/listarRecomendaciones'],
    ['Planes', '/configuracion/listarPlanes'],
    ['Análisis', '/configuracion/listarAnalisis'],

  ];

  constructor() { }

  ngOnInit() {
  }

}
