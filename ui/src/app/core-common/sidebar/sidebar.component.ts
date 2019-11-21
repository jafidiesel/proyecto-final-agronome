import { Component, OnInit } from '@angular/core';
import { faEdit, faListAlt, faFileMedical, faChartPie, faLock, faCogs, faMapMarkedAlt, faDatabase } from '@fortawesome/free-solid-svg-icons';
import { AuthService } from 'src/app/auth/auth.service';


@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css'] // no borrar
})
export class SidebarComponent implements OnInit {

  rol: string;
  nombreFinca: string;
  
  faEdit = faEdit;
  faListAlt = faListAlt;
  faFileMedical = faFileMedical;
  faChartPie = faChartPie;
  faLock = faLock;
  faCogs = faCogs;
  faMapMarkedAlt = faMapMarkedAlt;
  faDatabase = faDatabase

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.rol = this.auth.getRol();
    this.actualizarNombreFinca();
  }

  actualizarNombreFinca(){
    this.nombreFinca =  (this.auth.getNombreFinca() == "false") ? "" : this.auth.getNombreFinca();
  }

  setActive(id){
    /* const selectEl = event.target;
    const valor = selectEl.value;
    const id = selectEl.id; */
    document.querySelectorAll('.elementMenu').forEach( element => {
      console.log(element.id,id);
      if(element.id == id){
        element.setAttribute('class','elementMenu active');
      }else{
        element.setAttribute('class','elementMenu');
      }
    } );

  }

}
