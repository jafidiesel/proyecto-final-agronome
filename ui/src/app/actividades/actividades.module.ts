import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LibroDeCampoComponent } from './libro-de-campo/libro-de-campo.component';



@NgModule({
  declarations: [
    LibroDeCampoComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    LibroDeCampoComponent
  ]
})
export class ActividadesModule { }
