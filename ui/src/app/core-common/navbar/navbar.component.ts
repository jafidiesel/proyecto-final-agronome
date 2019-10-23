import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';
import { delay } from 'rxjs/operators';
import Swal from 'sweetalert2';
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  rol:string;
  nombre:string;
  @Output() ValidateTokenFather2 = new EventEmitter();


  constructor(private router: Router) { 
  }
  
  ngOnInit() {
    this.rol = localStorage.getItem('rol');
    this.nombre = localStorage.getItem('nombre');
  }
  
  logout(){
    
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
        this.router.navigate(['']);
        this.ValidateTokenFather2.emit('logout');
        localStorage.removeItem('rol');
        localStorage.removeItem('token');
        swalWithBootstrapButtons.fire({
          title: '¡Exito!',
          text: 'Se cerró sesión correctamente.',
          type: 'warning',
          confirmButtonText: 'Salir',
          reverseButtons: true
        })
        setTimeout(() => this.ValidateTokenFather2.emit('logout') );
      } 
    })

  }


}
