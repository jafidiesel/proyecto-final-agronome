import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SeguridadPageComponent } from './seguridad-page.component';

describe('SeguridadPageComponent', () => {
  let component: SeguridadPageComponent;
  let fixture: ComponentFixture<SeguridadPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SeguridadPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SeguridadPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
