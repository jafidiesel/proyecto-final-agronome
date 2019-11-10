import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlanificacionFinalComponent } from './planificacion-final.component';

describe('PlanificacionFinalComponent', () => {
  let component: PlanificacionFinalComponent;
  let fixture: ComponentFixture<PlanificacionFinalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlanificacionFinalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlanificacionFinalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
