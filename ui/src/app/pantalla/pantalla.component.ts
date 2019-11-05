import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-pantalla',
  templateUrl: './pantalla.component.html'
})
export class PantallaComponent implements OnInit {

  tokenExist = false;
  
  activar = false;
  recuperar = false;
  login = false;


  constructor(private router: Router) { 
    if( localStorage.getItem('token') ){
      this.tokenExist = true;
      this.router.navigateByUrl('/home');
    }

  }

  ngOnInit() {
    console.log(window.location.pathname)

    /* if((window.location.pathname).includes("activar")){
      this.activar = true;
    }else if((window.location.pathname).includes("recuperar") ){
      this.recuperar = true;
    }else {
      this.login = true;
    } */
    
  }

  validateToken(event){
    console.log('event',event);

    if( localStorage.getItem('token') ){
      this.tokenExist = true;
      //this.router.navigateByUrl('/actividades');
      if (localStorage.getItem('rol') == 'encargadofinca' && parseInt(localStorage.getItem('cantFincas')) == 0 ) {
        this.router.navigate(['/finca/crearFinca']);        
      }else{
        this.tokenExist = false;
        this.router.navigate(['/actividades/listarActividades']);
      }
    }else {
    }/* if(event == "login"){
      
      this.activar = false;
      this.recuperar = false;
      this.login = true;
      this.tokenExist = false;
    } */
    return this.tokenExist;

  }

  irLogin(event){
    console.log('event',event);
  }
}