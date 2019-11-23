import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { LoginService } from '../services/login.service';

@Component({
  selector: 'app-activar',
  templateUrl: './activar.component.html'
})
export class ActivarComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  token: string;
  url: string;

  response: boolean = false;
  userActivated:boolean;

  constructor(
    private activatedRoute: ActivatedRoute,
    private router: Router,
     private _loginService: LoginService ) { }

  ngOnInit() {
    this.url = window.location.pathname;
    this.token = this.url.slice(9, this.url.length);
    //this.url.toLocaleLowerCase().indexOf('activar')

    if(this.token != '' || this.token != null){
      this.activateUser(this.token);
    }
   
  }

  activateUser(token: string) {
    this.subscriptions.push(
      this._loginService.activateUser(token).subscribe(
        result =>{
          this.userActivated = true;
          this.response = true;
        },
        error => {
          this.userActivated = false;
          this.response = true;
        }
      )
    );
  }

  navigateLogin(){
    this.router.navigate(['/login']);
    setTimeout(() => this.router.navigate(['/login']) );

  }

  
  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }

}
