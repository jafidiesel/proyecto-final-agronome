import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarAnalisisComponent } from './listar-analisis.component';

describe('ListarAnalisisComponent', () => {
  let component: ListarAnalisisComponent;
  let fixture: ComponentFixture<ListarAnalisisComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListarAnalisisComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListarAnalisisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
