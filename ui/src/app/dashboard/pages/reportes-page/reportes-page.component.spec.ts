import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReportesPageComponent } from './reportes-page.component';

describe('ReportesPageComponent', () => {
  let component: ReportesPageComponent;
  let fixture: ComponentFixture<ReportesPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReportesPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReportesPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
