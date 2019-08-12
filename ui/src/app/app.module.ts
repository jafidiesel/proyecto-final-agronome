import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

/* own imports */
import { ActividadesModule } from './actividades/actividades.module';
import { CoreCommonModule  } from './core-common/core-common.module';
import { DashboardModule } from './dashboard/dashboard.module';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CoreCommonModule, // Common purpouse components
    DashboardModule, // App main module
   // ActividadesModule // Feature Module
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
