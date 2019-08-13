import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CoreCommonModule } from '../core-common/core-common.module';

import { ActividadPageComponent } from './pages/actividad-page/actividad-page.component';
import { PlanificacionPageComponent } from './pages/planificacion-page/planificacion-page.component';
import { RecursosPageComponent } from './pages/recursos-page/recursos-page.component';
import { FincasPageComponent } from './pages/fincas-page/fincas-page.component';
import { RecomendacionesPageComponent } from './pages/recomendaciones-page/recomendaciones-page.component';
import { SeguridadPageComponent } from './pages/seguridad-page/seguridad-page.component';
import { ConfiguracionPageComponent } from './pages/configuracion-page/configuracion-page.component';
import { ReportesPageComponent } from './pages/reportes-page/reportes-page.component';
import { DashboardPageComponent } from './pages/dashboard-page/dashboard-page.component';
import { RouterModule } from '@angular/router';

/* Actividad */
import { LibroDeCampoComponent } from './components/actividad/libro-de-campo/libro-de-campo.component';



@NgModule({
  declarations: [
    ActividadPageComponent,
    PlanificacionPageComponent,
    RecursosPageComponent,
    FincasPageComponent,
    RecomendacionesPageComponent,
    SeguridadPageComponent,
    ConfiguracionPageComponent,
    ReportesPageComponent,
    DashboardPageComponent,
    LibroDeCampoComponent
  ],
  imports: [
    CommonModule,
    CoreCommonModule,
    RouterModule
  ],
  exports: [
    ActividadPageComponent,
    PlanificacionPageComponent,
    RecursosPageComponent,
    DashboardPageComponent,
    FincasPageComponent,
    RecomendacionesPageComponent,
    SeguridadPageComponent,
    ConfiguracionPageComponent,
    ReportesPageComponent
  ]
})
export class DashboardModule { }
