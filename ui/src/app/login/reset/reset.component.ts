import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-reset',
  templateUrl: './reset.component.html'
})
export class ResetComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  token: string;
  url: string;

  constructor() { }

  ngOnInit() {
    this.url = window.location.pathname;
    this.token = this.url.slice(11, this.url.length);
    console.log('url',this.url);
    console.log('token', this.token);
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }

}
