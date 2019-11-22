import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth/auth.service';
import Swal from 'sweetalert2';
import { PlanificacionService } from 'src/app/dashboard/services/planificacion/planificacion.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-planificacion-final',
  templateUrl: './planificacion-final.component.html'
})
export class PlanificacionFinalComponent implements OnInit {
  rol: string;
  visible: boolean;
  mostrarTablaParcelas = false;

  dummyDataCultivo = [
    "Tomate", "Lechuga", "Zanahoria", "Calabaza", "Cebolla"
  ];

  tableDataHeader = ['Parcela', 'Cuadros']
  parcelaArray = []

  constructor(private auth: AuthService, private _planificacionService: PlanificacionService, private router: Router) { }

  ngOnInit() {
    this.visible = false;
    this.rol = this.auth.getRol();
    console.log(this.rol)
    this.parcelaArray.push(this.tableDataHeader)
    this.parcelaArray.push(
      ['Parcela 1', '1,2,3'],
      ['Parcela 2', '2,3,4'])
    this.mostrarTablaParcelas = true;

  }

  finalizar() {
    this.visible = true;
  }

  async agregarCuadros() {


    this.mostrarTablaParcelas = false;
    const { value: formValues } = await Swal.fire({
      title: 'Seleccione los cuadros:',
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      backdrop: true,
      html:
        ` <h4>Parcela 1</h4>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1"> 1
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2"> 2
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 3
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2"> 4
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 5
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 6
              <span class="form-check-sign"></span>
            </label>
          </div>

          <h4>Parcela 2</h4>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1"> 1
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2"> 2
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 3
              <span class="form-check-sign"></span>
            </label>
          </div>
          <div class="form-check form-check-inline">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3"> 4
              <span class="form-check-sign"></span>
            </label>
          </div>
    `
      ,
      focusConfirm: false,
      confirmButtonText: 'Agregar',
      showCancelButton: true,
      cancelButtonText: 'Cancelar',
      reverseButtons: true,
      preConfirm: () => {
        // Aqui se debe realizar la validacion de todos los campos seleccionados
        this.parcelaArray = [];
        this.parcelaArray.push(this.tableDataHeader)
        this.parcelaArray.push(['Parcela 1', '1,3']);
        this.parcelaArray.push(['Parcela 2', '3,4']);
        this.mostrarTablaParcelas = true;

      }
    });
  }

  onSubmit(){
    this._planificacionService.guardarPlanificacion('final');
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
      },
      buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
      title: '¡Exito!',
      text: 'Se creo la planificación final correctamente.',
      type: 'success',
      confirmButtonText: 'Salir',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {
        this.router.navigate(['planificacion/verPlanificacionFinal']);
      }
    });
  }


}
