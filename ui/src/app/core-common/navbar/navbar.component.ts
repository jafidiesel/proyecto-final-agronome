import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';
import { delay } from 'rxjs/operators';
import Swal from 'sweetalert2';
import { AuthService } from 'src/app/auth/auth.service';
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  rol: string;
  rolText: string;
  nombre: string;
  nombreFinca: string;
  arrayFincas = [];
  @Output() ValidateTokenFather2 = new EventEmitter();


  constructor(
    private router: Router,
    private auth: AuthService) {
  }

  ngOnInit() {
    this.rol = localStorage.getItem('rol');
    if (this.rol === "encargadofinca") this.rolText = "Encargado de Finca";
    if (this.rol === "ingeniero") this.rolText = "Ingeniero Agrónomo";
    this.nombre = this.auth.getNombre();
    this.arrayFincas = this.auth.getFincas();

    this.nombreFinca = this.auth.getCurrentNombreFinca();
    if(this.nombreFinca == '') this.initFincas();

  }

  logout() {

    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
        cancelButton: 'btn btn-danger mr-1'
      },
      buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
      title: '¿Deseas cerrar sesión?',
      type: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Si',
      cancelButtonText: 'No',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {
        this.router.navigate(['/login']);
        this.ValidateTokenFather2.emit('logout');
        this.auth.logoutLocalStorage();
        swalWithBootstrapButtons.fire({
          title: '¡Exito!',
          text: 'Se cerró sesión correctamente.',
          type: 'success',
          confirmButtonText: 'Salir',
          reverseButtons: true
        })
        setTimeout(() => this.ValidateTokenFather2.emit('logout'));
      }
    })

  }

  initFincas() {
    if (this.arrayFincas.length == 1) {
      this.nombreFinca = this.arrayFincas[0].nombreFinca;
      this.auth.setearFinca(this.arrayFincas[0].codFinca, this.arrayFincas[0].nombreFinca);

    } else if (this.arrayFincas.length > 1) {
      this.seleccionarFinca();
      //this.nombreFinca = this.arrayFincas[0].nombreFinca;
    }
  }

  seleccionarFinca() {
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
        cancelButton: 'btn btn-danger mr-1'
      },
      buttonsStyling: false
    });

    let fincas = {}
    this.arrayFincas.map((element:any) => {
      fincas[element.codFinca] = element.nombreFinca ;
    })

    swalWithBootstrapButtons.fire({
      title: 'Seleccione una finca para trabajar.',
      type: 'info',
      showCancelButton: false,
      confirmButtonText: 'Seleccionar',
      cancelButtonText: 'No',
      input: 'select',
      inputOptions: fincas,
      allowOutsideClick: false,
      allowEscapeKey: false,
      reverseButtons: true,

    }).then((result) => {
      if (result.value) {
        this.auth.setearFinca(result.value, fincas[result.value]);
        this.nombreFinca = fincas[result.value];

        swalWithBootstrapButtons.fire({
          title: '¡Exito!',
          text: 'Finca cambiada correctamente.',
          type: 'success',
          confirmButtonText: 'Salir',
          reverseButtons: true
        })

      }
    });
  }


}
