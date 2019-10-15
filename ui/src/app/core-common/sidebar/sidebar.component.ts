import { Component, OnInit } from '@angular/core';
import { faEdit, faListAlt, faFileMedical, faChartPie, faLock, faCogs, faMapMarkedAlt } from '@fortawesome/free-solid-svg-icons';


@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css'] // no borrar
})
export class SidebarComponent implements OnInit {

  faEdit = faEdit;
  faListAlt = faListAlt;
  faFileMedical = faFileMedical;
  faChartPie = faChartPie;
  faLock = faLock;
  faCogs = faCogs;
  faMapMarkedAlt = faMapMarkedAlt;

  constructor() { }

  ngOnInit() {
  }

}
