import { Component, OnInit } from '@angular/core';
import { faEdit, faFileMedical, faSpinner } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-reportes-page',
  templateUrl: './reportes-page.component.html'
})
export class ReportesPageComponent implements OnInit {

  faEdit = faEdit;
  faFileMedical = faFileMedical;
  faSpinner = faSpinner;

  configurationButtons: any[] = [
    ['Reporte de Actividad', '/reportes/reporteActividad', faEdit],
    ['Reporte de Recomendación', '/reportes/reporteRecomendacion', faFileMedical],
    ['Reporte de Siembra', '/reportes/reportesiembra', faSpinner],
  ];

  constructor() { }

  ngOnInit() {
  }

}
