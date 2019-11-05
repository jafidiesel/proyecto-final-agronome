import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RecursosPageComponent } from './recursos-page.component';

describe('RecursosPageComponent', () => {
  let component: RecursosPageComponent;
  let fixture: ComponentFixture<RecursosPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecursosPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecursosPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
