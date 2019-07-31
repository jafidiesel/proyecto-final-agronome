import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LibroDeCampoComponent } from './libro-de-campo.component';

describe('LibroDeCampoComponent', () => {
  let component: LibroDeCampoComponent;
  let fixture: ComponentFixture<LibroDeCampoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LibroDeCampoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LibroDeCampoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
