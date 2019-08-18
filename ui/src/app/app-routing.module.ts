import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ActividadPageComponent } from './dashboard/pages/actividad-page/actividad-page.component';
import { PlanificacionPageComponent } from './dashboard/pages/planificacion-page/planificacion-page.component';
import { FincasPageComponent } from './dashboard/pages/fincas-page/fincas-page.component';
import { RecomendacionesPageComponent } from './dashboard/pages/recomendaciones-page/recomendaciones-page.component';
import { RecursosPageComponent } from './dashboard/pages/recursos-page/recursos-page.component';
import { SeguridadPageComponent } from './dashboard/pages/seguridad-page/seguridad-page.component';
import { ConfiguracionPageComponent } from './dashboard/pages/configuracion/configuracion-page/configuracion-page.component';
import { ReportesPageComponent } from './dashboard/pages/reportes-page/reportes-page.component';
import { ListarActividadesComponent } from './dashboard/pages/configuracion/listar-actividades/listar-actividades.component';
import { ListarRecomendacionesComponent } from './dashboard/pages/configuracion/listar-recomendaciones/listar-recomendaciones.component';
import { ListarPlanesComponent } from './dashboard/pages/configuracion/listar-planes/listar-planes.component';
import { ListarAnalisisComponent } from './dashboard/pages/configuracion/listar-analisis/listar-analisis.component';
import { ListarNomencladoresComponent } from './dashboard/pages/configuracion/listar-nomencladores/listar-nomencladores.component';
import { ListarParametrosComponent } from './dashboard/pages/configuracion/listar-parametros/listar-parametros.component';


const routes: Routes = [
  { path: 'actividades', component: ActividadPageComponent },
  { path: 'planificacion', component: PlanificacionPageComponent },
  { path: 'finca', component: FincasPageComponent },
  { path: 'recomendaciones', component: RecomendacionesPageComponent },
  { path: 'recursos', component: RecursosPageComponent },
  { path: 'seguridad', component: SeguridadPageComponent },
  /* Modulo Configuracion */
  { path: 'configuracion', component: ConfiguracionPageComponent },
  { path: 'configuracion/listarActividades', component: ListarActividadesComponent },
  { path: 'configuracion/listarRecomendaciones', component: ListarRecomendacionesComponent },
  { path: 'configuracion/listarPlanes', component: ListarPlanesComponent },
  { path: 'configuracion/listarAnalisis', component: ListarAnalisisComponent },
  { path: 'configuracion/listarNomencladores', component: ListarNomencladoresComponent },
  { path: 'configuracion/listarParametros', component: ListarParametrosComponent },
  /* Modulo Reportes */
  { path: 'reportes', component: ReportesPageComponent },
  { path: '**', pathMatch: 'full', redirectTo: 'configuracion' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
