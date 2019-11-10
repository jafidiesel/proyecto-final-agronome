import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlanificacionSupervisadaComponent } from './planificacion-supervisada.component';

describe('PlanificacionSupervisadaComponent', () => {
  let component: PlanificacionSupervisadaComponent;
  let fixture: ComponentFixture<PlanificacionSupervisadaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlanificacionSupervisadaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlanificacionSupervisadaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
