import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FincasPageComponent } from './fincas-page.component';

describe('FincasPageComponent', () => {
  let component: FincasPageComponent;
  let fixture: ComponentFixture<FincasPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FincasPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FincasPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
