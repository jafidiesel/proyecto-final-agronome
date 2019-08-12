import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlanificacionPageComponent } from './planificacion-page.component';

describe('PlanificacionPageComponent', () => {
  let component: PlanificacionPageComponent;
  let fixture: ComponentFixture<PlanificacionPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlanificacionPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlanificacionPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
