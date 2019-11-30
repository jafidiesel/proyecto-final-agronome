import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-pantalla',
  templateUrl: './pantalla.component.html'
})
export class PantallaComponent implements OnInit {

  tokenExist = false;

  url: string;

  action: string;


  constructor(private router: Router) {
    // #TODO: Improve session detection
    if (localStorage.getItem('token')) {
      this.tokenExist = true;
      this.router.navigateByUrl('/home');
    }

  }

  ngOnInit() {
    this.url = window.location.pathname;

    if (this.url.toLocaleLowerCase().indexOf('activar') == 1) {
      this.action = "activar";
      return false;
      //this.router.navigateByUrl('/activar');
    } else if (this.url.toLocaleLowerCase().indexOf('login') == 1) {
      this.action = "login";
      return false;
    } if (this.url.toLocaleLowerCase().indexOf('recuperar') == 1) {
      this.action = "recuperar";
      console.log('recuperar');
      return false;
    } else if(this.tokenExist){
      this.action = "dashboard";
      return false;
    }else{
      this.action = "login";
      return false;
    }

  }

  validateToken(event) {

    if (localStorage.getItem('token')) {
      this.tokenExist = true;
      this.action = "dashboard";
      //this.router.navigateByUrl('/actividades');
      if (localStorage.getItem('rol') == 'encargadofinca' && parseInt(localStorage.getItem('cantFincas')) == 0) {
        this.router.navigate(['/finca/crearFinca']);
      } else {
        this.router.navigate(['/actividades/libroDeCampo']);
      }
    } else {
      this.action = "login";
      this.tokenExist = false;
    }
    return this.tokenExist;

  }
}