import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LibroDeCampoComponent } from './libro-de-campo/libro-de-campo.component';
//import { TableComponent } from '../components/shared/table/table.component';



@NgModule({
  declarations: [
    LibroDeCampoComponent,
  ],
  imports: [
    CommonModule,
   // TableComponent,
  ],
  exports: [
    LibroDeCampoComponent // required to use the module component from the outside
  ]
})
export class ActividadesModule { }
