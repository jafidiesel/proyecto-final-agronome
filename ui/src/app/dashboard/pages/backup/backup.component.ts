import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-backup',
  templateUrl: './backup.component.html',
  styleUrls: ['./backup.component.css']
})
export class BackupComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  recuperacion(){
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
        cancelButton: 'btn btn-danger mr-1'
      },
      buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
      title: '¿Deseas recuperar el sistema?',
      type: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Si',
      cancelButtonText: 'No',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {
        Swal.showLoading() 
        swalWithBootstrapButtons.fire({
          title: 'Recuperando',
          type: 'info',
          showLoaderOnConfirm: true,
          text: 'Iniciando la recuperación del sistema.',
          reverseButtons: true,
          onBeforeOpen: () => {
            Swal.showLoading()
          },
        })
      }
    })



    
  }

}
