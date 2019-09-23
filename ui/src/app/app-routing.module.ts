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
import { ListarRecomendacionesComponent } from './dashboard/pages/configuracion/listar-recomendaciones/listar-recomendaciones.component';
import { ListarPlanesComponent } from './dashboard/pages/configuracion/listar-planes/listar-planes.component';
import { ListarAnalisisComponent } from './dashboard/pages/configuracion/listar-analisis/listar-analisis.component';
import { ListarParametrosComponent } from './dashboard/pages/configuracion/parametro/listar-parametros/listar-parametros.component';
import { CrearParametroComponent } from './dashboard/pages/configuracion/parametro/crear-parametro/crear-parametro.component';
import { EditarParametroComponent } from './dashboard/pages/configuracion/parametro/editar-parametro/editar-parametro.component';
import { ListarNomencladoresComponent } from './dashboard/pages/configuracion/nomenclador/listar-nomencladores/listar-nomencladores.component';
import { CrearNomencladorComponent } from './dashboard/pages/configuracion/nomenclador/crear-nomenclador/crear-nomenclador.component';
import { EditarNomencladorComponent } from './dashboard/pages/configuracion/nomenclador/editar-nomenclador/editar-nomenclador.component';
import { ListarActividadesAsociadasComponent } from './dashboard/pages/configuracion/asociar/actividad/listar-actividades-asociadas/listar-actividades-asociadas.component';
import { AsociarActividadComponent } from './dashboard/pages/configuracion/asociar/actividad/asociar-actividad/asociar-actividad.component';
import { EditarActividadAsociadaComponent } from './dashboard/pages/configuracion/asociar/actividad/editar-actividad-asociada/editar-actividad-asociada.component';


const routes: Routes = [
  { path: 'actividades', component: ActividadPageComponent },
  { path: 'planificacion', component: PlanificacionPageComponent },
  { path: 'finca', component: FincasPageComponent },
  { path: 'recomendaciones', component: RecomendacionesPageComponent },
  { path: 'recursos', component: RecursosPageComponent },
  { path: 'seguridad', component: SeguridadPageComponent },
  /* Modulo Configuracion */
  { path: 'configuracion', component: ConfiguracionPageComponent },
  { path: 'configuracion/listarRecomendaciones', component: ListarRecomendacionesComponent },
  { path: 'configuracion/listarPlanes', component: ListarPlanesComponent },
  { path: 'configuracion/listarAnalisis', component: ListarAnalisisComponent },
  /* Modulo Configuracion - Asociar */
  { path: 'configuracion/asociar/listarActividades', component: ListarActividadesAsociadasComponent },
  { path: 'configuracion/asociar/asociarActividad', component: AsociarActividadComponent },
  { path: 'configuracion/asociar/editarActividad/:id', component: EditarActividadAsociadaComponent },
  /* Modulo Configuracion - Nomencladores */
  { path: 'configuracion/listarNomencladores', component: ListarNomencladoresComponent },
  { path: 'configuracion/crearNomenclador', component: CrearNomencladorComponent },
  { path: 'configuracion/editarNomenclador/:tipoNomenclador/:id', component: EditarNomencladorComponent },
  { path: 'configuracion/editarNomenclador', component: EditarNomencladorComponent },
  /* Modulo Configuracion - Parametros */
  { path: 'configuracion/listarParametros', component: ListarParametrosComponent },
  { path: 'configuracion/crearParametro', component: CrearParametroComponent },
  { path: 'configuracion/editarParametro/:id', component: EditarParametroComponent },
  /* Modulo Reportes */
  { path: 'reportes', component: ReportesPageComponent },
  /* { path: '**', pathMatch: 'full', redirectTo: 'configuracion' } */
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
