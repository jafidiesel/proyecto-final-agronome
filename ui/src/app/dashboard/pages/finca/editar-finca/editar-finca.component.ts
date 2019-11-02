import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FincaService } from 'src/app/dashboard/services/finca.service';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { AuthService } from 'src/app/auth/auth.service';
import Swal from 'sweetalert2';
import { faMapMarkedAlt } from '@fortawesome/free-solid-svg-icons';



@Component({
  selector: 'app-editar-finca',
  templateUrl: './editar-finca.component.html'
})
export class EditarFincaComponent implements OnInit, OnDestroy {

  nombreFinca: string;
  codFinca: number;
  urlMap: string;
  faMapMarkedAlt = faMapMarkedAlt;

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
    private router: Router,
    private auth: AuthService) { }

  ngOnInit() {
    if (this.auth.getRol() == 'encargadofinca' && this.auth.getNombreFinca() == null) {
      this.router.navigate(['/finca/crearFinca']);
    }
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

    let codFinca = this.auth.getcodFinca();
    this.subscriptions.push(
      this._fincaService.getFinca(codFinca).subscribe(
        (result: any) => {
          this.initForm(result.finca);
        },
        error => this.onHttpError({ message: "Ocurrió un error al obtener los datos de la finca" })
      )
    );

  }

  initForm(form) {
    this.nombreFinca = form.nombre;
    this.codFinca = parseInt(form.codFinca);
    this.urlMap = form.urlMaps;

    this.subscriptions.push(
      this._fincaService.getProvincia(form.provincia).subscribe(
        (resultProvincia: any) => {
          let provCod = resultProvincia.provincias[0].id;
          this.seleccionProvinciaPorId(form.provincia, parseInt(provCod));

          this.subscriptions.push(
            this._fincaService.getMunicipio(provCod, form.localidad).subscribe(
              (resultMunicipio: any) => {
                let muniCod = resultMunicipio.municipios[0].id;

                let parcelas = form.parcelas;
                let index = 0;
                parcelas.map(parcela => {
                  let cantCuadros = parseInt(parcela.filas) * parseInt(parcela.columnas);
                  this.parcelasTabla = [...this.parcelasTabla, [parcela.nombre, parcela.superficie, String(parcela.columnas), String(parcela.filas), String(cantCuadros), `./${index}`]];
                  index++;
                });

                this.fincaForm = this.fb.group({
                  nombre: [form.nombre, Validators.required],
                  superficie: [form.superficie, Validators.required],
                  calle: [form.calle, Validators.required],
                  nro: [form.nro, Validators.required],
                  provincia: [form.provincia, Validators.required],
                  provinciaCod: [provCod, Validators.required],
                  localidad: [form.localidad, Validators.required],
                  localidadCod: [muniCod, Validators.required],
                  parcelas: [null, Validators.required]
                });
              },
              error => this.onHttpError({ message: `Ocurrio un error al tratar de obtener los datos de ${form.localidad}` })
            )
          );


        },
        error => this.onHttpError({ message: `Ocurrio un error al tratar de obtener los datos de ${form.provincia}` })
      )
    );



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


  seleccionProvinciaPorId(nombre: string, id: number) {
    this.municipiosArray = [];

    this.provinciaName = nombre;

    this.subscriptions.push(
      this._fincaService.getMunicipios(id).subscribe(
        (result: any) => {
          result.municipios.map(municipio => {
            this.municipiosArray.push({ nombre: municipio.nombre, id: municipio.id })
          })
        },
        error => this.onHttpError(error)
      )
    );
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
        '<input id="swal-input2" min="1" class="swal2-input" type="number">' +
        '<p for="swal-input3">Cantidad de filas</p>' +
        '<input id="swal-input3" min="1" class="swal2-input" type="number">' +
        '<p for="swal-input4">Cantidad de columnas</p>' +
        '<input id="swal-input4" min="1" class="swal2-input" type="number">'
      ,
      focusConfirm: false,
      confirmButtonText: 'Agregar',
      showCancelButton: true,
      cancelButtonText: 'Cancelar',
      reverseButtons: true,
      preConfirm: () => {

        if (
          !(<HTMLInputElement>document.getElementById('swal-input2')).checkValidity() &&
          !(<HTMLInputElement>document.getElementById('swal-input3')).checkValidity() &&
          !(<HTMLInputElement>document.getElementById('swal-input4')).checkValidity()
        ) {
          Swal.showValidationMessage("Valores negativos: Debe ingresar valores mayores a cero para poder agregar una parcela.")
        } else if (
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
      this.parcelasTabla = [...this.parcelasTabla, [formValues.nombre, formValues.superficie, formValues.cantFilas, formValues.cantColumnas, String(cantCuadros), "./" + (parseInt(this.parcelasTabla[this.parcelasTabla.length - 1][5][2]) + 1)]];
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
  quitarFila(event) {
    let index = 0;
    this.parcelasTabla.map(parcela => {
      if (parcela[5][2] == event) {
        this.mostrarTabla = false;
        setTimeout(() => {
          this.habilitarTabla();
        }, 500);
      }
      index++;
    });

  }

  onSubmit() {
    this.formatFormToJson();

    if (this.fincaForm.status == 'VALID') {
      this.subscriptions.push(
        this._fincaService.putFinca(this.fincaForm.value, this.codFinca).subscribe(
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
              text: 'Se editó la finca correctamente.',
              type: 'success',
              confirmButtonText: 'Salir',
              reverseButtons: true
            }).then((result) => {
              if (result.value) {
                this.router.navigate(['home']);
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

  habilitarTabla() {
    this.mostrarTabla = true;
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
