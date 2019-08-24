import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TableComponent } from './table/table.component';
import { NavbarComponent } from './navbar/navbar.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { RouterModule } from '@angular/router';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { TablePaneComponent } from './table-pane/table-pane.component';


@NgModule({
  declarations: [
    TableComponent,
    NavbarComponent,
    SidebarComponent,
    TablePaneComponent

  ],
  imports: [
    CommonModule,
    RouterModule,
    FontAwesomeModule
  ],
  exports: [
    TableComponent,
    NavbarComponent,
    SidebarComponent,
    TablePaneComponent
  ]
})
export class CoreCommonModule { }
