import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlanificacionInicialComponent } from './planificacion-inicial.component';

describe('PlanificacionInicialComponent', () => {
  let component: PlanificacionInicialComponent;
  let fixture: ComponentFixture<PlanificacionInicialComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlanificacionInicialComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlanificacionInicialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
