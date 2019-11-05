import { Component, OnInit } from '@angular/core';
import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import * as pluginDataLabels from 'chartjs-plugin-datalabels';
import { Label } from 'ng2-charts';

@Component({
  selector: 'app-reporte-actividad',
  templateUrl: './reporte-actividad.component.html'
})
export class ReporteActividadComponent implements OnInit {
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
  public barChartLabels: Label[] = ["riego"
    , "siembra"
    , "fertilización"
    , "preparación suelo"
    , "tratamiento fitosanitario"
    , "cosecha"
    , "detección catastrofe"
    , "detección fitosanitaria"
    , "fertirrigación"];
  public barChartType: ChartType = 'bar';
  public barChartLegend = true;
  public barChartPlugins = [pluginDataLabels];

  public barChartData: ChartDataSets[] = [
    { data: [2], label: "riego" },
    { data: [4], label: "siembra" },
    { data: [1], label: "fertilización" },
    { data: [1], label: "preparación suelo" },
    { data: [1], label: "tratamiento fitosanitario" },
    { data: [1], label: "cosecha" },
    { data: [2], label: "detección catastrofe" },
    { data: [2], label: "detección fitosanitaria" },
    { data: [0], label: "fertirrigación" }
  ];

  tempChartData = {
    dataset: [
      { data: [2], label: "riego" },
      { data: [4], label: "siembra" },
      { data: [1], label: "fertilización" },
      { data: [1], label: "preparación suelo" },
      { data: [1], label: "tratamiento fitosanitario" },
      { data: [1], label: "cosecha" },
      { data: [2], label: "detección catastrofe" },
      { data: [2], label: "detección fitosanitaria" },
      { data: [0], label: "fertirrigación" }
    ],
    label: "2019-01-01 00:00 - 2019-12-30 00:45"
  }


  constructor() { }

  ngOnInit() {
  }
  // events
  public chartClicked({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }

  public chartHovered({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }

  public randomize(): void {
    // Only Change 3 values
    const data = [
      Math.round(Math.random() * 100),
      59,
      80,
      (Math.random() * 100),
      56,
      (Math.random() * 100),
      40];
    this.barChartData[0].data = data;
  }

}
