import { Component, OnInit, OnDestroy } from '@angular/core';
import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import * as pluginDataLabels from 'chartjs-plugin-datalabels';
import { Label } from 'ng2-charts';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';
import { ReportesService } from 'src/app/dashboard/services/reportes/reportes.service';

@Component({
  selector: 'app-reporte-recomendacion',
  templateUrl: './reporte-recomendacion.component.html'
})
export class ReporteRecomendacionComponent implements OnInit, OnDestroy {

  fechaDesde: any;
  fechaHasta: any;

  subscriptions: Subscription[] = [];

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';


  // Pie
  public pieChartOptions: ChartOptions = {
    responsive: true,
    legend: {
      position: 'top',
    },
    plugins: {
      datalabels: {
        formatter: (value, ctx) => {
          const label = ctx.chart.data.labels[ctx.dataIndex];
          return label;
        },
      },
    }
  };

  public pieChartLabels: Label[] = [];
  public pieChartData: number[] = [];
  public pieChartType: ChartType = 'pie';
  public pieChartLegend = true;
  public pieChartPlugins = [pluginDataLabels];
  public pieChartColors = [
    {
      backgroundColor: ['rgba(255,0,0,0.3)', 'rgba(0,255,0,0.3)', 'rgba(0,0,255,0.3)'],
    },
  ];


/*   public barChartType: ChartType = 'bar';
  public barChartLegend = true;
  public barChartPlugins = [pluginDataLabels];

  public barChartLabels: Label[] = [];


  public barChartData: ChartDataSets[] = []; */

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
      this._reportesService.getReporteRecomendacion(this.fechaDesde, this.fechaHasta).subscribe(
        result => {
          console.warn('result', result);
          this.initDataset(result);
        },
        error => this.onHttpError({ message: "Debe ingresar ambas fechas." })
      )
    );

  }


  initDataset(form) {
    this.pieChartData = [];
    let tempIntArray = form.dataset.number.map(element => parseInt(element));
    this.pieChartData.push( tempIntArray );
    let tempLabelArray = form.label.map(element => element == "activARecomendar" ? "Actividades a recomendar" : "Actividades recomendadas");
    this.pieChartLabels = tempLabelArray;
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