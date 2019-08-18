import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarParametrosComponent } from './listar-parametros.component';

describe('ListarParametrosComponent', () => {
  let component: ListarParametrosComponent;
  let fixture: ComponentFixture<ListarParametrosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListarParametrosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListarParametrosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
