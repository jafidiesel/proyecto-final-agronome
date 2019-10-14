import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-dashboard-page',
  templateUrl: './dashboard-page.component.html',
  styleUrls: ['./dashboard-page.component.css']
})
export class DashboardPageComponent implements OnInit {

  tokenExist = false;

  constructor(private router: Router) { 
    if( localStorage.getItem('token') ){
      this.tokenExist = true;
      console.log(this.tokenExist);
      //this.router.navigateByUrl('/actividades');
    }

  }

  ngOnInit() {
    
  }

}
