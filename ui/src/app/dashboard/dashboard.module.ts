import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { CoreCommonModule } from '../core-common/core-common.module';


/* main pages */
import { ActividadPageComponent } from './pages/actividad-page/actividad-page.component';
import { PlanificacionPageComponent } from './pages/planificacion-page/planificacion-page.component';
import { RecursosPageComponent } from './pages/recursos-page/recursos-page.component';
import { FincasPageComponent } from './pages/fincas-page/fincas-page.component';
import { RecomendacionesPageComponent } from './pages/recomendaciones-page/recomendaciones-page.component';
import { SeguridadPageComponent } from './pages/seguridad-page/seguridad-page.component';
import { ConfiguracionPageComponent } from './pages/configuracion/configuracion-page/configuracion-page.component';
import { ReportesPageComponent } from './pages/reportes-page/reportes-page.component';
import { DashboardPageComponent } from './pages/dashboard-page/dashboard-page.component';

/* Actividad */
import { LibroDeCampoComponent } from './components/actividad/libro-de-campo/libro-de-campo.component';

/* Configuracion */
import { ListarRecomendacionesComponent } from './pages/configuracion/asociar/recomendacion/listar-recomendaciones/listar-recomendaciones.component';
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
    EditarPlanAsociadoComponent
  ],
  imports: [
    CommonModule,
    CoreCommonModule,
    RouterModule,
    FormsModule,
    FontAwesomeModule,
    ReactiveFormsModule,
    NgbModule
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
