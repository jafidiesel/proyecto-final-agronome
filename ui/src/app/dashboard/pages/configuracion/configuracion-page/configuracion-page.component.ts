import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-configuracion-page',
  templateUrl: './configuracion-page.component.html',
  styleUrls: ['./configuracion-page.component.css']
})
export class ConfiguracionPageComponent implements OnInit {
  configurationButtons: any[] = [
    ['Actividad', '/configuracion/listarActividades'],
    ['Recomendaciones', '/configuracion/listarRecomendaciones'],
    ['Planes', '/configuracion/listarPlanes'],
    ['Análisis', '/configuracion/listarAnalisis'],
    ['Nomencladores', '/configuracion/listarNomencladores'],
    ['Parámetros', '/configuracion/listarParametros'],

  ];

  constructor() { }

  ngOnInit() {
  }

}
