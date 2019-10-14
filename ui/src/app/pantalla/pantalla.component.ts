import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-pantalla',
  templateUrl: './pantalla.component.html'
})
export class PantallaComponent implements OnInit {

  tokenExist = false;

  constructor(private router: Router) { 
    if( localStorage.getItem('token') ){
      this.tokenExist = true;
      this.router.navigateByUrl('/home');
    }
    console.log(this.tokenExist);

  }

  ngOnInit() {
    
  }

  validateToken(event){
    console.log(event);

    if( localStorage.getItem('token') ){
      this.tokenExist = true;
      //this.router.navigateByUrl('/actividades');
      this.router.navigate(['/actividades/listarActividades']);
    }else{
      this.tokenExist = false;
    }
    return this.tokenExist;

  }
}