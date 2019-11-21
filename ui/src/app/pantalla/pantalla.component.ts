import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-pantalla',
  templateUrl: './pantalla.component.html'
})
export class PantallaComponent implements OnInit {

  tokenExist = false;

  constructor(private router: Router) { 
    // #TODO: Improve session detection
    if( localStorage.getItem('token') ){
      this.tokenExist = true;
      this.router.navigateByUrl('/home');
    }

  }

  ngOnInit() {
    
  }

  validateToken(event){

    if( localStorage.getItem('token') ){
      this.tokenExist = true;
      //this.router.navigateByUrl('/actividades');
      if (localStorage.getItem('rol') == 'encargadofinca' && parseInt(localStorage.getItem('cantFincas')) == 0 ) {
        this.router.navigate(['/finca/crearFinca']);        
      }else{
        this.router.navigate(['/actividades/listarActividades']);
      }
    }else{
      this.tokenExist = false;
    }
    return this.tokenExist;

  }
}