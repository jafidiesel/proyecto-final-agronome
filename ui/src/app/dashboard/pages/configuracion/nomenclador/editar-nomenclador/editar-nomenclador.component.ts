import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-editar-nomenclador',
  templateUrl: './editar-nomenclador.component.html'
})
export class EditarNomencladorComponent implements OnInit {

  originalNomencladorAcargar = {
    nombre: '',
    tipoNomenclador: -1,
    isActiv: 0
  };

  nomencladorAcargar = { ...this.originalNomencladorAcargar };

  constructor() { }

  ngOnInit() {
  }

}
