import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-libro-de-campo',
  templateUrl: './libro-de-campo.component.html',
  styleUrls: ['./libro-de-campo.component.css']
})
export class LibroDeCampoComponent implements OnInit {
  cantLC: any[] = [1, 2, 3, 4, 5];

  constructor() { }

  ngOnInit() {
  }

}
