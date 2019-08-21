import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ConfiguracionService {

  private nomencladorData = [
    ['Nombre', 'Activo', 'Tipo Nomenclador', 'Accion', ''],
    ['En Curso', 'Si', 'EstadoPlanificacion', '#/editar', '#/Desactivar'],
    ['Inicial', 'Si', 'TipoPlanificacion', '#/editar', '#/Desactivar'],
    ['Supervisada', 'Si', 'TipoPlanificacion', '#/editar', '#/Desactivar']
  ];

  private parametroData = [
    ['Nombre', 'Activo', 'Tipo de dato', 'Tipo de parámetro', 'Accion', ''],
    ['Hora de riego', 'Si', 'Time', 'Actividad', '#/editar', '#/Desactivar'],
    ['Cantidad', 'Si', 'Number', 'Actividad', '#/editar', '#/Desactivar'],
    ['Fecha', 'Si', 'Date', 'Recomendación', '#/editar', '#/Desactivar']
];

  private planData = [
    ['Nombre', 'Activo', 'Accion', ''],
    ['Riego', 'Si', '#/editar', '#/Desactivar'],
    ['Siembra', 'Si', '#/editar', '#/Desactivar'],
    ['Cosecha', 'Si', '#/editar', '#/Desactivar']
  ];

  private recomendacionData = [
    ['Nombre', 'Activo', 'Accion', ''],
    ['Fitosanitaria', 'Si', '#/editar', '#/Desactivar'],
    ['Fitosanitaria', 'Si', '#/editar', '#/Desactivar'],
    ['Fitosanitaria', 'Si', '#/editar', '#/Desactivar']
];
  private analisisData = [
    ['Nombre', 'Activo', 'Accion', ''],
    ['Suelo', 'Si', '#/editar', '#/Desactivar'],
    ['Agua', 'Si', '#/editar', '#/Desactivar'],
    ['Superficie', 'Si', '#/editar', '#/Desactivar']
];

  private actividadData = [
    ['Nombre', 'Activo', 'Accion', ''],
    ['Riego', 'Si', '#/editar', '#/Desactivar'],
    ['Cosecha', 'Si', '#/editar', '#/Desactivar'],
    ['Siembra', 'Si', '#/editar', '#/Desactivar']
];

  constructor() { }

  getNomencladorData() {
    return this.nomencladorData;
  }
  
  getParametroData() {
    return this.parametroData;
  }

  getPlanData() {
    return this.planData;
  }

  getRecomendacionData() {
    return this.recomendacionData;
  }

  getAnalisisData() {
    return this.analisisData;
  }

  getActividadData() {
    return this.actividadData;
  }

}
