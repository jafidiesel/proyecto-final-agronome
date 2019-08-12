import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RecomendacionesPageComponent } from './recomendaciones-page.component';

describe('RecomendacionesPageComponent', () => {
  let component: RecomendacionesPageComponent;
  let fixture: ComponentFixture<RecomendacionesPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecomendacionesPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecomendacionesPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
