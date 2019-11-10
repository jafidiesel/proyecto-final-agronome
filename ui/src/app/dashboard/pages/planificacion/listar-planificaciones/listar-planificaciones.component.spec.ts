import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarPlanificacionesComponent } from './listar-planificaciones.component';

describe('ListarPlanificacionesComponent', () => {
  let component: ListarPlanificacionesComponent;
  let fixture: ComponentFixture<ListarPlanificacionesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListarPlanificacionesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListarPlanificacionesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
