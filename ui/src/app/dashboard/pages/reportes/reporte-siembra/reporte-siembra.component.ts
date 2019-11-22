import { Component, OnInit, OnDestroy } from '@angular/core';
import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import * as pluginDataLabels from 'chartjs-plugin-datalabels';
import { Label } from 'ng2-charts';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';
import { ReportesService } from 'src/app/dashboard/services/reportes/reportes.service';

@Component({
  selector: 'app-reporte-siembra',
  templateUrl: './reporte-siembra.component.html'
})
export class ReporteSiembraComponent implements OnInit, OnDestroy {

  fechaDesde: any;
  fechaHasta: any;

  subscriptions: Subscription[] = [];

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';


  // Pie
  public barChartOptions: ChartOptions = {
    responsive: true,
    // We use these empty structures as placeholders for dynamic theming.
    scales: { xAxes: [{}], yAxes: [{}] },
    plugins: {
      datalabels: {
        anchor: 'end',
        align: 'end',
      }
    }
  };

  public barChartType: ChartType = 'bar';
  public barChartLegend = true;
  public barChartPlugins = [pluginDataLabels];

  public barChartLabels: Label[] = [];
  public barChartData: ChartDataSets[] = [];


  mostrarGrafico = false;

  constructor(private _reportesService: ReportesService, private router: Router) { }

  ngOnInit() {
  }
  // events
  public chartClicked({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }

  public chartHovered({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }


  onSubmit() {

    this.subscriptions.push(
      this._reportesService.getReporteSiembra(this.fechaDesde, this.fechaHasta).subscribe(
        result => {
          this.initDataset(result);
        },
        error => this.onHttpError({ message: "Debe ingresar ambas fechas." })
      )
    );

  }


  initDataset(form) {
    this.barChartData = [];
    this.barChartData.push(
      {
        data: form.dataset[0].data, label: form.dataset[0].label
      }
    );
    this.barChartData.push(
      {
        data: form.dataset[1].data, label: form.dataset[1].label
      }
    );
    this.barChartLabels = form.label.map(element => {
      switch (element) {
        case 1:
          return "Enero";
          break;
        case 2:
          return "Febrero";
          break;
        case 3:
          return "Marzo";
          break;
        case 4:
          return "Abril";
          break;
        case 5:
          return "Mayo";
          break;
        case 6:
          return "Junio";
          break;
        case 7:
          return "Julio";
          break;
        case 8:
          return "Agosto";
          break;
        case 9:
          return "Septiembre";
          break;
        case 10:
          return "Octubre";
          break;
        case 11:
          return "Noviembre";
          break;
        case 12:
          return "Diciembre";
          break;
      }
    });
    this.mostrarGrafico = true;

  }

  mostrar() {
    this.mostrarGrafico = !this.mostrarGrafico;
  }


  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}