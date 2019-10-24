import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http'

import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { LoginPageComponent } from './login-page/login-page.component';


@NgModule({
  declarations: [
    HomeComponent,
    LoginComponent,
    LoginPageComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
  ],
  exports: [LoginComponent]
})
export class LoginModule { }
