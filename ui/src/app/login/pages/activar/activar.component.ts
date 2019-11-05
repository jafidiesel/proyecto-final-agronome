import { Component, OnInit, EventEmitter, Output, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import Swal from 'sweetalert2';
import { Subscription } from 'rxjs';
import { LoginService } from '../../login.service';

@Component({
  selector: 'app-activar',
  templateUrl: './activar.component.html'
})
export class ActivarComponent implements OnInit, OnDestroy {

  @Output() ValidateTokenFather = new EventEmitter();
  
  subscriptions: Subscription[] = [];

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private _loginService: LoginService, private router: Router,
    private activatedRoute: ActivatedRoute
    ) { }

  ngOnInit() {
    this.subscriptions.push(
      this.activatedRoute.params.subscribe(params => {
        this._loginService.getActivar(params['token']).subscribe(
          result =>{
            console.log(result);
            this.postSuccess = true;
            this.postError = false;
            this.postErrorMessage = '';
          },
          error => this.onHttpError({ message: "Ocurrió un inconveniente al activar el usuario." })
        )

      })
    );

  }

  irLogin(){
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
        cancelButton: 'btn btn-danger mr-1'
      },
      buttonsStyling: false
    })
    swalWithBootstrapButtons.fire({
      title: '¡Exito!',
      text: 'Se activó su usuario correctamente.',
      type: 'success',
      confirmButtonText: 'Salir',
      reverseButtons: true
    })
    this.ValidateTokenFather.emit('login');


  }

  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }
  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }

}
