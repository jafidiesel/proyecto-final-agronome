import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarRecomendacionesComponent } from './listar-recomendaciones.component';

describe('ListarRecomendacionesComponent', () => {
  let component: ListarRecomendacionesComponent;
  let fixture: ComponentFixture<ListarRecomendacionesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListarRecomendacionesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListarRecomendacionesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
