import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistroNoConvencionalesComponent } from './registro-no-convencionales.component';

describe('RegistroNoConvencionalesComponent', () => {
  let component: RegistroNoConvencionalesComponent;
  let fixture: ComponentFixture<RegistroNoConvencionalesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegistroNoConvencionalesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistroNoConvencionalesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
