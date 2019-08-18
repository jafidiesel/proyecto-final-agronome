import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarNomencladoresComponent } from './listar-nomencladores.component';

describe('ListarNomencladoresComponent', () => {
  let component: ListarNomencladoresComponent;
  let fixture: ComponentFixture<ListarNomencladoresComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListarNomencladoresComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListarNomencladoresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
