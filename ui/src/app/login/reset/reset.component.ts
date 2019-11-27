import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { NgForm } from '@angular/forms';
import { LoginService } from '../services/login.service';

@Component({
  selector: 'app-reset',
  templateUrl: './reset.component.html'
})
export class ResetComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  token: string;
  url: string;

  usuario: string;
  password1: string;
  password2: string;
  firstPassword = false;
  passwordsMatch = false;


  constructor(private _loginService: LoginService) { }

  ngOnInit() {
    this.url = window.location.pathname;
    this.token = this.url.slice(11, this.url.length);
    console.log('url', this.url);
    console.log('token', this.token);
  }

  reset( form: NgForm ) {
    if (this.token == '') {
      this.resetUser(form);
    }else{
      this.resetPassword(form);
    }
  }


  resetUser(form: NgForm) {

    if (form.valid) {

      Swal.fire({
        allowOutsideClick: false,
        type: 'info',
        text: 'Espere por favor'
      });
      Swal.showLoading();

      this.subscriptions.push(
        this._loginService.sendRecover(this.usuario).subscribe(
          result => {
            Swal.close();
            Swal.fire({
              allowOutsideClick: true,
              type: 'success',
              title: 'Recuperado',
              text: result.message
            });
          },
          error => {
            Swal.fire({
              allowOutsideClick: true,
              type: 'error',
              title: 'Error',
              text: error.error.message
            });
          }
        )
      );

    }

  }

  resetPassword(form: NgForm) {

    if (form.valid) {

      Swal.fire({
        allowOutsideClick: false,
        type: 'info',
        text: 'Espere por favor'
      });
      Swal.showLoading();

      this.subscriptions.push(
        this._loginService.confirmPassword(this.password1, this.password2, this.token).subscribe(
          result => {
            Swal.close();
            Swal.fire({
              allowOutsideClick: true,
              type: 'success',
              title: 'Recuperado',
              text: result.message
            });
          },
          error => {
            Swal.fire({
              allowOutsideClick: true,
              type: 'error',
              title: 'Error',
              text: error.error.message
            });
          }
        )
      );

    }

  }

  firstPasswordSet() {
    this.firstPassword = true;
    if (this.password1 != this.password2) this.passwordsMatch = false;
  }

  passwordMatch() {
    if (this.password1 == this.password2) {
      this.passwordsMatch = true;
    }
  }



  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }

}
