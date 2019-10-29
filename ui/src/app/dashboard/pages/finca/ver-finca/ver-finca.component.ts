import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { FincaService } from 'src/app/dashboard/services/finca.service';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { AuthService } from 'src/app/auth/auth.service';

@Component({
  selector: 'app-ver-finca',
  templateUrl: './ver-finca.component.html'
})
export class VerFincaComponent implements OnInit, OnDestroy {

  subscriptions: Subscription[] = [];

  fincaForm: FormGroup;

  // error flags 
  postSuccess = false;
  postError = false;
  postErrorMessage = '';

  constructor(private fb: FormBuilder,
    private _fincaService: FincaService,
    private router: Router,
    private auth: AuthService) { }

  ngOnInit() {
    console.log(this.auth.getRol());
    console.log(this.auth.getNombreFinca());
    if( this.auth.getRol() == 'encargadofinca' && this.auth.getNombreFinca() == null ){
      this.router.navigate(['/finca/crearFinca']);        
    }

  }

  onHttpError(errorResponse: any) {
    this.postError = true;
    this.postSuccess = false;
    this.postErrorMessage = errorResponse.message;
  }

  ngOnDestroy() {
    this.subscriptions.forEach((subscription) => subscription.unsubscribe());
  }

}
