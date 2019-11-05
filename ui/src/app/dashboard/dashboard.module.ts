import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { TokenInterceptor } from './../auth/token.interceptor';

import { CoreCommonModule } from '../core-common/core-common.module';

/* main pages */
import { ActividadPageComponent } from './pages/actividad-page/actividad-page.component';
import { PlanificacionPageComponent } from './pages/planificacion-page/planificacion-page.component';
import { RecursosPageComponent } from './pages/recursos-page/recursos-page.component';
import { SeguridadPageComponent } from './pages/seguridad-page/seguridad-page.component';
import { ConfiguracionPageComponent } from './pages/configuracion/configuracion-page/configuracion-page.component';
import { ReportesPageComponent } from './pages/reportes/reportes-page/reportes-page.component';
import { DashboardPageComponent } from './pages/dashboard-page/dashboard-page.component';

/* Actividad */
import { LibroDeCampoComponent } from './components/actividad/libro-de-campo/libro-de-campo.component';

/* Configuracion */
import { ListarRecomendacionesAsociadasComponent } from './pages/configuracion/asociar/recomendacion/listar-recomendaciones/listar-recomendaciones-asociadas.component';
import { ListarNomencladoresComponent } from './pages/configuracion/nomenclador/listar-nomencladores/listar-nomencladores.component';
import { ListarParametrosComponent } from './pages/configuracion/parametro/listar-parametros/listar-parametros.component';
import { CrearParametroComponent } from './pages/configuracion/parametro/crear-parametro/crear-parametro.component';
import { CrearNomencladorComponent } from './pages/configuracion/nomenclador/crear-nomenclador/crear-nomenclador.component';
import { EditarNomencladorComponent } from './pages/configuracion/nomenclador/editar-nomenclador/editar-nomenclador.component';
import { EditarParametroComponent } from './pages/configuracion/parametro/editar-parametro/editar-parametro.component';
import { ListarActividadesAsociadasComponent } from './pages/configuracion/asociar/actividad/listar-actividades-asociadas/listar-actividades-asociadas.component';
import { AsociarActividadComponent } from './pages/configuracion/asociar/actividad/asociar-actividad/asociar-actividad.component';
import { EditarActividadAsociadaComponent } from './pages/configuracion/asociar/actividad/editar-actividad-asociada/editar-actividad-asociada.component';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

// import pagination component
import { JwPaginationComponent } from 'jw-angular-pagination';
import { RegistrarActividadComponent } from './pages/actividad/registrar-actividad/registrar-actividad.component';
import { AsociarRecomendacionComponent } from './pages/configuracion/asociar/recomendacion/asociar-recomendacion/asociar-recomendacion.component';
import { EditarRecomendacionAsociadaComponent } from './pages/configuracion/asociar/recomendacion/editar-recomendacion-asociada/editar-recomendacion-asociada.component';
import { EditarAnalisisAsociadoComponent } from './pages/configuracion/asociar/analisis/editar-analisis-asociado/editar-analisis-asociado.component';
import { AsociarAnalisisComponent } from './pages/configuracion/asociar/analisis/asociar-analisis/asociar-analisis.component';
import { ListarPlanComponent } from './pages/configuracion/asociar/plan/listar-plan/listar-plan.component';
import { AsociarPlanComponent } from './pages/configuracion/asociar/plan/asociar-plan/asociar-plan.component';
import { EditarPlanAsociadoComponent } from './pages/configuracion/asociar/plan/editar-plan-asociado/editar-plan-asociado.component';
import { ListarAnalisisComponent } from './pages/configuracion/asociar/analisis/listar-analisis/listar-analisis.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CrearUsuarioComponent } from './pages/seguridad/crear-usuario/crear-usuario.component';
import { ListarUsuariosComponent } from './pages/seguridad/listar-usuarios/listar-usuarios.component';
import { ListarActividadesComponent } from './pages/actividad/listar-actividades/listar-actividades.component';
import { VerActividadComponent } from './pages/actividad/ver-actividad/ver-actividad.component';
import { EditarUsuarioComponent } from './pages/seguridad/editar-usuario/editar-usuario.component';
import { CrearFincaComponent } from './pages/finca/crear-finca/crear-finca.component';
import { EditarFincaComponent } from './pages/finca/editar-finca/editar-finca.component';
import { ListarRecomendacionesComponent } from './pages/recomendacion/listar-recomendaciones/listar-recomendaciones.component';
import { RegistrarRecomendacionComponent } from './pages/recomendacion/registrar-recomendacion/registrar-recomendacion.component';
import { VerRecomendacionComponent } from './pages/recomendacion/ver-recomendacion/ver-recomendacion.component';
import { ReporteActividadComponent } from './pages/reportes/reporte-actividad/reporte-actividad.component';
import { ChartsModule } from 'ng2-charts';
import { BackupComponent } from './pages/backup/backup.component';

@NgModule({
  declarations: [
    ActividadPageComponent,
    PlanificacionPageComponent,
    RecursosPageComponent,
    SeguridadPageComponent,
    ConfiguracionPageComponent,
    ReportesPageComponent,
    DashboardPageComponent,
    LibroDeCampoComponent,
    ListarActividadesAsociadasComponent,
    ListarRecomendacionesComponent,
    ListarNomencladoresComponent,
    ListarParametrosComponent,
    CrearParametroComponent,
    EditarParametroComponent,
    CrearNomencladorComponent,
    EditarNomencladorComponent,
    JwPaginationComponent,
    ListarActividadesAsociadasComponent,
    AsociarActividadComponent,
    EditarActividadAsociadaComponent,
    RegistrarActividadComponent,
    AsociarRecomendacionComponent,
    EditarRecomendacionAsociadaComponent,
    EditarAnalisisAsociadoComponent,
    AsociarAnalisisComponent,
    ListarPlanComponent,
    AsociarPlanComponent,
    EditarPlanAsociadoComponent,
    ListarAnalisisComponent,
    AsociarAnalisisComponent,
    EditarAnalisisAsociadoComponent,
    ListarPlanComponent,
    AsociarPlanComponent,
    EditarPlanAsociadoComponent,
    CrearUsuarioComponent,
    ListarUsuariosComponent,
    ListarActividadesComponent,
    VerActividadComponent,
    EditarUsuarioComponent,
    CrearFincaComponent,
    EditarFincaComponent,
    ListarRecomendacionesAsociadasComponent,
    RegistrarRecomendacionComponent,
    VerRecomendacionComponent,
    ReporteActividadComponent,
    BackupComponent,

  ],
  imports: [
    CommonModule,
    CoreCommonModule,
    RouterModule,
    FormsModule,
    FontAwesomeModule,
    ReactiveFormsModule,
    NgbModule,
    ChartsModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi: true
    }],
  exports: [
    ActividadPageComponent,
    PlanificacionPageComponent,
    RecursosPageComponent,
    DashboardPageComponent,
    SeguridadPageComponent,
    ConfiguracionPageComponent,
    ReportesPageComponent
  ],
})
export class DashboardModule { }
