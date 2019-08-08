import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TableComponent } from './table/table.component';
import { NavbarComponent } from './navbar/navbar.component';
import { SidebarComponent } from './sidebar/sidebar.component';


@NgModule({
  declarations: [
    TableComponent,
    NavbarComponent,
    SidebarComponent

  ],
  imports: [
    CommonModule
  ],
  exports: [
    TableComponent,
    NavbarComponent,
    SidebarComponent
  ]
})
export class CoreCommonModule { }
