import { Component, OnInit, Output, EventEmitter, OnDestroy } from '@angular/core';
import { NgForm } from '@angular/forms';
import { UsuarioModel } from 'src/app/models/usuario.model';
import Swal from 'sweetalert2';
import { AuthService } from 'src/app/auth/auth.service';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit, OnDestroy {

  @Output() ValidateTokenFather = new EventEmitter();

  subscriptions: Subscription[] = [];

  usuario: UsuarioModel;

  constructor(private auth: AuthService,
    private router: Router) { }

  ngOnInit() {
    this.usuario = new UsuarioModel();
  }

  login(form: NgForm) {

    if (form.valid) {

      Swal.fire({
        allowOutsideClick: false,
        type: 'info',
        text: 'Espere por favor'
      });
      Swal.showLoading();

      this.subscriptions.push(
        this.auth.login(this.usuario).subscribe(
          resp => {
            Swal.close();
            this.ValidateTokenFather.emit('login');
            //this.router.navigate(['/home']);

          },
          err => {
            Swal.fire({
              allowOutsideClick: true,
              type: 'error',
              title: 'Error',
              text: 'Usuario y/o contrasña invalida.'
            });
          }
        )
      );

    }

  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
