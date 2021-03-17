import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PaperLeagueComponent } from './paper-league.component';

describe('PaperLeagueComponent', () => {
  let component: PaperLeagueComponent;
  let fixture: ComponentFixture<PaperLeagueComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PaperLeagueComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PaperLeagueComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
