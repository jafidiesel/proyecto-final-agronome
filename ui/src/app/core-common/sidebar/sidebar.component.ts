import { Component, OnInit } from '@angular/core';
import { faEdit, faListAlt, faFileMedical, faChartPie, faLock, faCogs, faMapMarkedAlt } from '@fortawesome/free-solid-svg-icons';
import { AuthService } from 'src/app/auth/auth.service';


@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css'] // no borrar
})
export class SidebarComponent implements OnInit {

  rol: string;
  
  faEdit = faEdit;
  faListAlt = faListAlt;
  faFileMedical = faFileMedical;
  faChartPie = faChartPie;
  faLock = faLock;
  faCogs = faCogs;
  faMapMarkedAlt = faMapMarkedAlt;

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.rol = this.auth.getRol();
  }

}
