import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

/* own imports */
import { SidebarComponent } from './components/shared/sidebar/sidebar.component';
import { NavbarComponent } from './components/shared/navbar/navbar.component';
import { ActividadesModule } from './actividades/actividades.module';
import { TableComponent } from './components/shared/table/table.component';

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    NavbarComponent,
    TableComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ActividadesModule // Feature Module
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
