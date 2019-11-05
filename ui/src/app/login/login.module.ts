import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http'

import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { ResetComponent } from './pages/reset/reset.component';
import { ActivarComponent } from './pages/activar/activar.component';


@NgModule({
  declarations: [
    HomeComponent,
    LoginComponent,
    LoginPageComponent,
    ResetComponent,
    ActivarComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
  ],
  exports: [
    LoginComponent,
    ResetComponent,
    ActivarComponent
  ]
})
export class LoginModule { }