import { Component, OnInit } from '@angular/core';
import { LibroDeCampoComponent } from '../../components/actividad/libro-de-campo/libro-de-campo.component';
import { ActividadService } from '../../services/actividad/actividad.service';


@Component({
  selector: 'app-actividad-page',
  templateUrl: './actividad-page.component.html',
  styleUrls: ['./actividad-page.component.css']
})
export class ActividadPageComponent implements OnInit {

  constructor( private _actividadService: ActividadService ){}


  ngOnInit() {
  }

}
