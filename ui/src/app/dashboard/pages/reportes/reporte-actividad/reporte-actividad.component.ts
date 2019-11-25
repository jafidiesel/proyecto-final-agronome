import { Component, OnInit, OnDestroy } from '@angular/core';
import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import * as pluginDataLabels from 'chartjs-plugin-datalabels';
import { Label } from 'ng2-charts';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';
import { ReportesService } from 'src/app/dashboard/services/reportes/reportes.service';

@Component({
  selector: 'app-reporte-actividad',
  templateUrl: './reporte-actividad.component.html'
})
export class ReporteActividadComponent implements OnInit, OnDestroy {

  fechaDesde: any;
  fechaHasta: any;

  subscriptions: Subscription[] = [];

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';


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
      this._reportesService.getReporteActividad(this.fechaDesde, this.fechaHasta).subscribe(
        result => {
          this.initDataset(result);
        },
        error => this.onHttpError({ message: "Debe ingresar ambas fechas." })
      )
    );

  }


  initDataset(form){
    this.barChartData = [];
    this.barChartData.push(
      {
        data: form.dataset.data, label: "Número de actividades"
      }
    );
    this.barChartLabels = form.label;
    this.mostrarGrafico = true;

  }

  mostrar(){
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
