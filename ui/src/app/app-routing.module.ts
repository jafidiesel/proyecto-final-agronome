import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ActividadPageComponent } from './dashboard/pages/actividad-page/actividad-page.component';
import { PlanificacionPageComponent } from './dashboard/pages/planificacion-page/planificacion-page.component';
import { FincasPageComponent } from './dashboard/pages/fincas-page/fincas-page.component';
import { RecomendacionesPageComponent } from './dashboard/pages/recomendaciones-page/recomendaciones-page.component';
import { RecursosPageComponent } from './dashboard/pages/recursos-page/recursos-page.component';
import { SeguridadPageComponent } from './dashboard/pages/seguridad-page/seguridad-page.component';
import { ConfiguracionPageComponent } from './dashboard/pages/configuracion-page/configuracion-page.component';
import { ReportesPageComponent } from './dashboard/pages/reportes-page/reportes-page.component';


const routes: Routes = [
  { path: 'actividades', component: ActividadPageComponent },
  { path: 'planificacion', component: PlanificacionPageComponent },
  { path: 'finca', component: FincasPageComponent },
  { path: 'recomendaciones', component: RecomendacionesPageComponent },
  { path: 'recursos', component: RecursosPageComponent },
  { path: 'seguridad', component: SeguridadPageComponent },
  { path: 'configuracion', component: ConfiguracionPageComponent },
  { path: 'reportes', component: ReportesPageComponent },
  { path: '**', pathMatch: 'full', redirectTo: 'actividades' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
