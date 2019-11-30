import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ActividadPageComponent } from './dashboard/pages/actividad-page/actividad-page.component';
import { ConfiguracionPageComponent } from './dashboard/pages/configuracion/configuracion-page/configuracion-page.component';
import { ReportesPageComponent } from './dashboard/pages/reportes/reportes-page/reportes-page.component';
import { ListarRecomendacionesAsociadasComponent } from './dashboard/pages/configuracion/asociar/recomendacion/listar-recomendaciones/listar-recomendaciones-asociadas.component';
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
import { CrearUsuarioComponent } from './dashboard/pages/seguridad/crear-usuario/crear-usuario.component';
import { ListarUsuariosComponent } from './dashboard/pages/seguridad/listar-usuarios/listar-usuarios.component';
import { ListarActividadesComponent } from './dashboard/pages/actividad/listar-actividades/listar-actividades.component';
import { VerActividadComponent } from './dashboard/pages/actividad/ver-actividad/ver-actividad.component';
import { EditarUsuarioComponent } from './dashboard/pages/seguridad/editar-usuario/editar-usuario.component';
import { LoginComponent } from './login/pages/login/login.component';
import { DashboardPageComponent } from './dashboard/pages/dashboard-page/dashboard-page.component';
import { PantallaComponent } from './pantalla/pantalla.component';
import { LoginPageComponent } from './login/login-page/login-page.component';
import { CrearFincaComponent } from './dashboard/pages/finca/crear-finca/crear-finca.component';
import { EditarFincaComponent } from './dashboard/pages/finca/editar-finca/editar-finca.component';
import { ListarRecomendacionesComponent } from './dashboard/pages/recomendacion/listar-recomendaciones/listar-recomendaciones.component';
import { VerRecomendacionComponent } from './dashboard/pages/recomendacion/ver-recomendacion/ver-recomendacion.component';
import { RegistrarRecomendacionComponent } from './dashboard/pages/recomendacion/registrar-recomendacion/registrar-recomendacion.component';
import { ReporteActividadComponent } from './dashboard/pages/reportes/reporte-actividad/reporte-actividad.component';
import { ReporteRecomendacionComponent } from './dashboard/pages/reportes/reporte-recomendacion/reporte-recomendacion.component';
import { ReporteSiembraComponent } from './dashboard/pages/reportes/reporte-siembra/reporte-siembra.component';
import { ReporteRiegoComponent } from './dashboard/pages/reportes/reporte-riego/reporte-riego.component';
import { BackupComponent } from './dashboard/pages/backup/backup.component';
import { ActivarComponent } from './login/activar/activar.component';
import { ResetComponent } from './login/reset/reset.component';
import { ListarPlanificacionesComponent } from './dashboard/pages/planificacion/listar-planificaciones/listar-planificaciones.component';
import { PlanificacionInicialComponent } from './dashboard/pages/planificacion/planificacion-inicial/planificacion-inicial.component';
import { PlanificacionSupervisadaComponent } from './dashboard/pages/planificacion/planificacion-supervisada/planificacion-supervisada.component';
import { PlanificacionFinalComponent } from './dashboard/pages/planificacion/planificacion-final/planificacion-final.component';
import { VerPlanificacionFinalComponent } from './dashboard/pages/planificacion/ver-planificacion-final/ver-planificacion-final.component';
import { LibroDeCampoRecomendacionComponent } from './dashboard/pages/recomendacion/libro-de-campo-recomendacion/libro-de-campo-recomendacion.component';


const routes: Routes = [
  
  /* Modulo Login */
  { path: '', component: PantallaComponent },
  { path: 'home', component: DashboardPageComponent },
  { path: 'login', component: LoginPageComponent },
  /* Modulo Actividades */
  { path: 'actividades/libroDeCampo', component: ActividadPageComponent },
  { path: 'actividades/registrarActividad', component: RegistrarActividadComponent },
  /* { path: 'actividades/listarActividades', component: ListarActividadesComponent }, */
  { path: 'actividades/listarActividades/:cod', component: ListarActividadesComponent },
  { path: 'actividades/verActividad/:cod', component: VerActividadComponent },
  /* Modulo Planificacion */
  { path: 'planificacion/listarPlanificaciones', component: ListarPlanificacionesComponent },
  { path: 'planificacion/crearPlanificacionInicial', component: PlanificacionInicialComponent },
  { path: 'planificacion/verPlanificacionInicial', component: PlanificacionSupervisadaComponent },
  { path: 'planificacion/verPlanificacionSupervisada', component: PlanificacionFinalComponent },
  { path: 'planificacion/verPlanificacionFinal', component: VerPlanificacionFinalComponent},
  /* Modulo Finca */
  { path: 'finca/listarFinca', component: CrearFincaComponent },
  { path: 'finca/crearFinca', component: CrearFincaComponent },
  { path: 'finca/editarFinca', component: EditarFincaComponent },
  /* Modulo Recomendaciones */
  // #TODO: Refactor this librodecampocomponentName, or reuse it in activity and recomendation
  { path: 'recomendaciones/libroDeCampo', component: LibroDeCampoRecomendacionComponent },
  { path: 'recomendaciones/listarRecomendaciones/:cod', component: ListarRecomendacionesComponent },
  { path: 'recomendaciones/verRecomendacion/:codAct/:codRec', component: VerRecomendacionComponent },
  { path: 'recomendaciones/registrarRecomendacion/:codAct', component: RegistrarRecomendacionComponent },
  /* Modulo Seguridad */
  //{ path: 'seguridad', component: SeguridadPageComponent },
  { path: 'seguridad', component: ListarUsuariosComponent },
  { path: 'seguridad/crearUsuario', component: CrearUsuarioComponent },
  { path: 'seguridad/editarUsuario/:cod', component: EditarUsuarioComponent },
  /* Modulo Configuracion */
  { path: 'configuracion', component: ConfiguracionPageComponent },
  { path: 'configuracion/listarRecomendaciones', component: ListarRecomendacionesComponent },
  /* Modulo Configuracion - Asociar */
  { path: 'configuracion/asociar/listarActividades', component: ListarActividadesAsociadasComponent },
  { path: 'configuracion/asociar/asociarActividad', component: AsociarActividadComponent },
  { path: 'configuracion/asociar/editarActividad/:cod', component: EditarActividadAsociadaComponent },
  { path: 'configuracion/asociar/asociarRecomendacion', component: AsociarRecomendacionComponent},
  { path: 'configuracion/asociar/listarRecomendaciones', component: ListarRecomendacionesAsociadasComponent},
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
  { path: 'reportes/reporteActividad', component: ReporteActividadComponent },
  { path: 'reportes/reporteRecomendacion', component: ReporteRecomendacionComponent },
  { path: 'reportes/reporteSiembra', component: ReporteSiembraComponent },
  { path: 'reportes/reporteRiego', component: ReporteRiegoComponent },
  
  /* Backup */
  { path: 'backup', component: BackupComponent },
  { path: 'activar/:token', component: ActivarComponent },
  { path: 'recuperar', component: ResetComponent },
  { path: 'recuperar/:token', component: ResetComponent },
  
  { path: '**', pathMatch: 'full', redirectTo: '/home' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
