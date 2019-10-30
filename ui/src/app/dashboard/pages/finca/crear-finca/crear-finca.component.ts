import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FincaService } from 'src/app/dashboard/services/finca.service';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';

@Component({
  selector: 'app-crear-finca',
  templateUrl: './crear-finca.component.html'
})
export class CrearFincaComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  fincaForm: FormGroup;

  provinciasArray = [];
  provinciaName: string;
  municipiosArray = [{ nombre: "Seleccione una provincia", id: "0" }];
  municipioName: string;

  parcelasTabla = [];
  tableDataHeader = ['Parcela', 'Superficie', 'Cantidad Filas', 'Cantidad Columnas', 'Cantidad Cuadros', 'Activo', 'Rol', 'Editar'];
  mostrarTabla = false;

  // error flags 
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private fb: FormBuilder,
    private _fincaService: FincaService,
    private router: Router) { }

  ngOnInit() {

    this.parcelasTabla.push(this.tableDataHeader);
    this.mostrarTabla = true;

    this.subscriptions.push(
      this._fincaService.getProvincias().subscribe(
        (result: any) => {
          result.provincias.map(provincia => {
            this.provinciasArray.push({ nombre: provincia.nombre, id: provincia.id })

          });
        },
        error => this.onHttpError({ message: "Ocurrió un error al obtener las provincias de la api del gobierno de Mendoza." })
      )
    );

    this.initForm();
  }


  initForm() {
    this.fincaForm = this.fb.group({
      nombre: [null, Validators.required],
      superficie: [null, Validators.required],
      calle: [null, Validators.required],
      nro: [null, Validators.required],
      provincia: [null, Validators.required],
      provinciaCod: [null, Validators.required],
      localidad: [null, Validators.required],
      localidadCod: [null, Validators.required],
      parcelas: [null, Validators.required]
    });

  }

  seleccionProvincia(event) {
    this.municipiosArray = [];
    const selectEl = event.target;
    const optionValue = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const optionDataNombre = selectEl.options[selectEl.selectedIndex].getAttribute('data-nombre');
    const optionText = selectEl.options[selectEl.selectedIndex].innerText;

    this.fincaForm.patchValue({
      provinciaCod: optionValue,
      provincia: optionDataNombre
    });
    this.provinciaName = optionText;

    this.subscriptions.push(
      this._fincaService.getMunicipios(optionValue).subscribe(
        (result: any) => {
          result.municipios.map(municipio => {
            this.municipiosArray.push({ nombre: municipio.nombre, id: municipio.id })
          })
        },
        error => this.onHttpError(error)
      )
    );
  }

  seleccionMunicipio(event) {
    const selectEl = event.target;
    const optionValue = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const optionText = selectEl.options[selectEl.selectedIndex].innerText;

    this.municipioName = optionText;
    this.fincaForm.patchValue({
      localidad: optionText,
      localidadCod: optionValue
    });
  }

  async agregarParcelas() {
    this.mostrarTabla = false;
    const { value: formValues } = await Swal.fire({
      title: 'Agregar Parcela',
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      backdrop: true,
      html:
        '<p for="swal-input1">Nombre de la parcela</p>' +
        '<input id="swal-input1" class="swal2-input">' +
        '<p for="swal-input2">Superficie</p>' +
        '<input id="swal-input2" class="swal2-input" type="number">' +
        '<p for="swal-input3">Cantidad de filas</p>' +
        '<input id="swal-input3" class="swal2-input" type="number">' +
        '<p for="swal-input4">Cantidad de columnas</p>' +
        '<input id="swal-input4" class="swal2-input" type="number">'
      ,
      focusConfirm: false,
      confirmButtonText: 'Agregar',
      showCancelButton: true,
      cancelButtonText: 'Cancelar',
      reverseButtons: true,
      preConfirm: () => {

        if (
          (<HTMLInputElement>document.getElementById('swal-input1')).value == '' ||
          (<HTMLInputElement>document.getElementById('swal-input2')).value == '' ||
          (<HTMLInputElement>document.getElementById('swal-input3')).value == '' ||
          (<HTMLInputElement>document.getElementById('swal-input4')).value == ''
        ) {
          Swal.showValidationMessage("Campos incompletos: Debe ingresar todos los valores para poder agregar una parcela.")
          return false;
        } else {
          return {
            "nombre": (<HTMLInputElement>document.getElementById('swal-input1')).value,
            "superficie": (<HTMLInputElement>document.getElementById('swal-input2')).value,
            "cantFilas": (<HTMLInputElement>document.getElementById('swal-input3')).value,
            "cantColumnas": (<HTMLInputElement>document.getElementById('swal-input4')).value
          }
        }

      }
    });

    if (formValues) {
      let cantCuadros = formValues.cantFilas * formValues.cantColumnas;
      this.parcelasTabla = [...this.parcelasTabla, [formValues.nombre, formValues.superficie, formValues.cantFilas, formValues.cantColumnas, String(cantCuadros)]];

    }

    this.mostrarTabla = true;
  }

  formatFormToJson() {
    let parcelas = [];

    this.parcelasTabla.map((row, index) => {
      if (index != 0) {
        parcelas.push({
          "nombre": row[0],
          "superficie": parseFloat(row[1]),
          "filas": parseInt(row[2]),
          "columnas": parseInt(row[3]),
        });
      }
    });


    this.fincaForm.patchValue({
      superficie: parseFloat(this.fincaForm.get('superficie').value),
      nro: parseFloat(this.fincaForm.get('nro').value),
      parcelas: parcelas
    });


  }

  onSubmit() {
    this.formatFormToJson();

    if (this.fincaForm.status == 'VALID') {
      this.subscriptions.push(
        this._fincaService.postFinca(this.fincaForm.value).subscribe(
          result => {
            this.postSuccess = true;
            this.postError = false;
            this.postErrorMessage = '';

            const swalWithBootstrapButtons = Swal.mixin({
              customClass: {
                confirmButton: 'btn btn-success ml-1',
              },
              buttonsStyling: false
            })

            swalWithBootstrapButtons.fire({
              title: '¡Exito!',
              text: 'Se creo la finca correctamente.',
              type: 'warning',
              confirmButtonText: 'Salir',
              reverseButtons: true
            }).then((result) => {
              if (result.value) {
                this.router.navigate(['actividades/listarActividades']);
              }
            }
            )
          },
          error => this.onHttpError(error)
        )
      );

    } else {
      this.onHttpError({ message: "Complete todos los campos obligatorios." });
    }
  }


  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  imprimir() {
    console.warn('fincaForm', this.fincaForm.value);
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }
}
