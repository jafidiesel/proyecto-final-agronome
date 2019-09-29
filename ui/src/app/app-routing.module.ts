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
import { ListarRecomendacionesComponent } from './dashboard/pages/configuracion/asociar/recomendacion/listar-recomendaciones/listar-recomendaciones.component';
import { ListarParametrosComponent } from './dashboard/pages/configuracion/parametro/listar-parametros/listar-parametros.component';
import { CrearParametroComponent } from './dashboard/pages/configuracion/parametro/crear-parametro/crear-parametro.component';
import { EditarParametroComponent } from './dashboard/pages/configuracion/parametro/editar-parametro/editar-parametro.component';
import { ListarNomencladoresComponent } from './dashboard/pages/configuracion/nomenclador/listar-nomencladores/listar-nomencladores.component';
import { CrearNomencladorComponent } from './dashboard/pages/configuracion/nomenclador/crear-nomenclador/crear-nomenclador.component';
import { EditarNomencladorComponent } from './dashboard/pages/configuracion/nomenclador/editar-nomenclador/editar-nomenclador.component';
import { ListarActividadesAsociadasComponent } from './dashboard/pages/configuracion/asociar/actividad/listar-actividades-asociadas/listar-actividades-asociadas.component';
import { AsociarActividadComponent } from './dashboard/pages/configuracion/asociar/actividad/asociar-actividad/asociar-actividad.component';
import { EditarActividadAsociadaComponent } from './dashboard/pages/configuracion/asociar/actividad/editar-actividad-asociada/editar-actividad-asociada.component';
import { RegistrarActividadComponent } from './dashboard/pages/actividad/registrar-actividad/registrar-actividad.component';
import { EditarRecomendacionAsociadaComponent } from './dashboard/pages/configuracion/asociar/recomendacion/editar-recomendacion-asociada/editar-recomendacion-asociada.component';
import { AsociarRecomendacionComponent } from './dashboard/pages/configuracion/asociar/recomendacion/asociar-recomendacion/asociar-recomendacion.component';
import { ListarAnalisisComponent } from './dashboard/pages/configuracion/asociar/analisis/listar-analisis/listar-analisis.component';
import { AsociarAnalisisComponent } from './dashboard/pages/configuracion/asociar/analisis/asociar-analisis/asociar-analisis.component';
import { EditarAnalisisAsociadoComponent } from './dashboard/pages/configuracion/asociar/analisis/editar-analisis-asociado/editar-analisis-asociado.component';
import { ListarPlanComponent } from './dashboard/pages/configuracion/asociar/plan/listar-plan/listar-plan.component';
import { AsociarPlanComponent } from './dashboard/pages/configuracion/asociar/plan/asociar-plan/asociar-plan.component';
import { EditarPlanAsociadoComponent } from './dashboard/pages/configuracion/asociar/plan/editar-plan-asociado/editar-plan-asociado.component';


const routes: Routes = [
  /* Modulo Actividades */
  { path: 'actividades', component: ActividadPageComponent },
  { path: 'actividades/registrarActividad', component: RegistrarActividadComponent },
  /* Modulo Planificacion */
  { path: 'planificacion', component: PlanificacionPageComponent },
  /* Modulo Finca */
  { path: 'finca', component: FincasPageComponent },
  /* Modulo Recomendaciones */
  { path: 'recomendaciones', component: RecomendacionesPageComponent },
  /* Modulo Gestionar Recursos */
  { path: 'recursos', component: RecursosPageComponent },
  /* Modulo Seguridad */
  { path: 'seguridad', component: SeguridadPageComponent },
  /* Modulo Configuracion */
  { path: 'configuracion', component: ConfiguracionPageComponent },
  { path: 'configuracion/listarRecomendaciones', component: ListarRecomendacionesComponent },
  /* Modulo Configuracion - Asociar */
  { path: 'configuracion/asociar/listarActividades', component: ListarActividadesAsociadasComponent },
  { path: 'configuracion/asociar/asociarActividad', component: AsociarActividadComponent },
  { path: 'configuracion/asociar/editarActividad/:cod', component: EditarActividadAsociadaComponent },
  { path: 'configuracion/asociar/asociarRecomendacion', component: AsociarRecomendacionComponent},
  { path: 'configuracion/asociar/listarRecomendaciones', component: ListarRecomendacionesComponent},
  { path: 'configuracion/asociar/editarRecomendacion/:cod', component: EditarRecomendacionAsociadaComponent},
  { path: 'configuracion/asociar/listarAnalisis', component: ListarAnalisisComponent },
  { path: 'configuracion/asociar/asociarAnalisis', component: AsociarAnalisisComponent },
  { path: 'configuracion/asociar/editarAnalisis/:cod', component: EditarAnalisisAsociadoComponent },
  { path: 'configuracion/asociar/listarPlanes', component: ListarPlanComponent },
  { path: 'configuracion/asociar/asociarPlan', component: AsociarPlanComponent },
  { path: 'configuracion/asociar/editarPlan/:cod', component: EditarPlanAsociadoComponent },
  /* Modulo Configuracion - Nomencladores */
  { path: 'configuracion/listarNomencladores', component: ListarNomencladoresComponent },
  { path: 'configuracion/crearNomenclador', component: CrearNomencladorComponent },
  { path: 'configuracion/editarNomenclador/:tipoNomenclador/:cod', component: EditarNomencladorComponent },
  { path: 'configuracion/editarNomenclador', component: EditarNomencladorComponent },
  /* Modulo Configuracion - Parametros */
  { path: 'configuracion/listarParametros', component: ListarParametrosComponent },
  { path: 'configuracion/crearParametro', component: CrearParametroComponent },
  { path: 'configuracion/editarParametro/:cod', component: EditarParametroComponent },
  /* Modulo Reportes */
  { path: 'reportes', component: ReportesPageComponent },
  { path: '**', pathMatch: 'full', redirectTo: 'actividades' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
