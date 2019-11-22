import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';
import { PlanificacionService } from 'src/app/dashboard/services/planificacion/planificacion.service';

@Component({
  selector: 'app-planificacion-inicial',
  templateUrl: './planificacion-inicial.component.html'
})
export class PlanificacionInicialComponent implements OnInit {

  mostrarTablaParcelas = false;
  mostrarCultivo = false;

  dummyDataCultivo = [
     "Lechuga", "Tomate","Zanahoria", "Calabaza", "Cebolla"
  ];

  tableDataHeader = ['Parcela', 'Cuadros']
  parcelaArray = []

  constructor(private router: Router, private _planificacionService: PlanificacionService) { }

  ngOnInit() {
    this.parcelaArray.push(this.tableDataHeader);
    //this.parcelaArray.push([ 'Parcela 1', '1,2,3' ]);
    this.mostrarTablaParcelas = true;
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
        this.parcelaArray.push(['Parcela 1', '1,2,3']);
        this.parcelaArray.push(['Parcela 2', '2,3,4']);
        this.mostrarTablaParcelas = true;

      }
    });
  }

  agregarCultivo() {
    this.mostrarCultivo = true;
  }
  
  quitarCultivo(){
    this.mostrarCultivo = false;

  }

 
  onSubmit(){
    this._planificacionService.guardarPlanificacion('inicial');
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success ml-1',
      },
      buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
      title: '¡Exito!',
      text: 'Se creo la planificación inicial correctamente.',
      type: 'success',
      confirmButtonText: 'Salir',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {
        this.router.navigate(['/planificacion/verPlanificacionInicial']);
      }
    });


  }


}
