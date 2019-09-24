import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-libro-de-campo',
  templateUrl: './libro-de-campo.component.html'
})
export class LibroDeCampoComponent implements OnInit {
  cantLC: any[] = [1, 2, 3, 4];

  constructor() { }

  ngOnInit() {
  }

}
