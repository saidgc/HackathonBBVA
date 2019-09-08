import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistroFisicaComponent } from './registro-fisica.component';

describe('RegistroFisicaComponent', () => {
  let component: RegistroFisicaComponent;
  let fixture: ComponentFixture<RegistroFisicaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegistroFisicaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistroFisicaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
