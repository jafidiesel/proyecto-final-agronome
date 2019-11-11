import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth/auth.service';
import { PlanificacionService } from 'src/app/dashboard/services/planificacion/planificacion.service';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';

@Component({
  selector: 'app-planificacion-supervisada',
  templateUrl: './planificacion-supervisada.component.html',
})

export class PlanificacionSupervisadaComponent implements OnInit {
  rol: string;
  visible: boolean;

  dummyDataCultivo = [
    "Tomate","Lechuga","Zanahoria", "Calabaza", "Cebolla"
  ];

  tableDataHeader = ['Parcela', 'Cuadros']
  parcelaArray = []

  constructor(private auth: AuthService, private _planificacionService: PlanificacionService, private router: Router) { }

  ngOnInit() {
    this.visible = false;
    this.rol = this.auth.getRol();
    this.parcelaArray.push(this.tableDataHeader)
    this.parcelaArray.push(
      ['Parcela 1','1,2,3'],
    ['Parcela 2', '2,3,4'])
  }

  supervisar(){
    this.visible = true;

  }

  
  onSubmit(){
    this._planificacionService.guardarPlanificacion('supervisada');
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
      },
      buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
      title: '¡Exito!',
      text: 'Se creo la planificación supervisada correctamente.',
      type: 'success',
      confirmButtonText: 'Salir',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {
        this.router.navigate(['planificacion/verPlanificacionSupervisada']);
      }
    });


  }

}
