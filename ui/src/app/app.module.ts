import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

/* own imports */
import { ActividadesModule } from './actividades/actividades.module';
import { CoreCommonModule  } from './core-common/core-common.module';

@NgModule({
  declarations: [
    AppComponent,


  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CoreCommonModule, // Con esto ya se puede utilizar los componentes que estan dentro de CoreCommonModule

    ActividadesModule // Feature Module
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
