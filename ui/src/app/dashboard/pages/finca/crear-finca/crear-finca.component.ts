import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FincaService } from 'src/app/dashboard/services/finca.service';

@Component({
  selector: 'app-crear-finca',
  templateUrl: './crear-finca.component.html'
})
export class CrearFincaComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  fincaForm: FormGroup;

  provinciasArray = [];
  municipiosArray = [];

  // error flags
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private fb: FormBuilder,
    private _fincaService: FincaService) { }

  ngOnInit() {
    this.initForm();

    this.subscriptions.push(
      this._fincaService.getProvincias().subscribe(
        (result: any) => {
          console.log(result.provincias);
          result.provincias.map( provincia =>{
            this.provinciasArray.push({ nombre: provincia.nombre, id: provincia.id })

          });
        },
        error => console.log('error', error)
      )
    );


  }

  /* {
      "nombre": "3 huertas qweqwe con usuario",
      "superficie": 12341.00,
      "calle": "Alvarez",
      "nro": 2024,
      "localidad": "Las heras",
      "provincia": "Mendoza",
      "parcelas": [
          {
              "nombre": "A",
              "superficie": 123.3,
              "filas": 4,
              "columnas": 2
          },
          {
              "nombre": "B",
              "superficie": 12097.3,
              "filas": 7,
              "columnas": 1
          }
      ]
  } */

  initForm() {
    this.fincaForm = this.fb.group({
      nombre: [null, Validators.required],
      superficie: [null, Validators.required],
      calle: [null, Validators.required],
      nro: [null, Validators.required],
      provincia: [],
      localidad: [null, Validators.required],
      parcelas: [null]

    });

  }

  actualizarLocalidades(event){
    this.municipiosArray = [];
    const selectEl = event.target;
    const optionValue = parseInt(selectEl.options[selectEl.selectedIndex].getAttribute('value'));
    const optionText = selectEl.options[selectEl.selectedIndex].innerText;

    this.subscriptions.push(
      this._fincaService.getMunicipios(optionValue).subscribe(
        (result:any) => {
          result.municipios.map( municipio => {
            this.municipiosArray.push({nombre: municipio.nombre, id: municipio.id})
          })
        },
        error => this.onHttpError(error)
      )
    );

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
