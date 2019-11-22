import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-libro-de-campo',
  templateUrl: './libro-de-campo.component.html'
})
export class LibroDeCampoComponent implements OnInit {
  cantLC: any[] = [1, 2];

  librosDeCampo = [];

  constructor() { }

  ngOnInit() {
    this.librosDeCampo.push( ["Lechuga MF-3", "10-01-2019", "/actividades/listarActividades"] );
    this.librosDeCampo.push( ["Tomate BC-3", "12-11-2019","" ] );

  }

}
