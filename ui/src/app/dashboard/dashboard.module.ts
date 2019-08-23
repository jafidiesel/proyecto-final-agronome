import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

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
import { ListarActividadesComponent } from './pages/configuracion/listar-actividades/listar-actividades.component';
import { ListarRecomendacionesComponent } from './pages/configuracion/listar-recomendaciones/listar-recomendaciones.component';
import { ListarPlanesComponent } from './pages/configuracion/listar-planes/listar-planes.component';
import { ListarAnalisisComponent } from './pages/configuracion/listar-analisis/listar-analisis.component';
import { ListarNomencladoresComponent } from './pages/configuracion/listar-nomencladores/listar-nomencladores.component';
import { ListarParametrosComponent } from './pages/configuracion/parametro/listar-parametros/listar-parametros.component';
import { CrearParametroComponent } from './pages/configuracion/parametro/crear-parametro/crear-parametro.component';
import { ModificarParametroComponent } from './pages/configuracion/parametro/modificar-parametro/modificar-parametro.component';



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
    ListarActividadesComponent,
    ListarRecomendacionesComponent,
    ListarPlanesComponent,
    ListarAnalisisComponent,
    ListarNomencladoresComponent,
    ListarParametrosComponent,
    CrearParametroComponent,
    ModificarParametroComponent
  ],
  imports: [
    CommonModule,
    CoreCommonModule,
    RouterModule,
    
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
