import { TestBed } from '@angular/core/testing';

import { AgendaserviceService } from './agendaservice.service';

describe('AgendaserviceService', () => {
  let service: AgendaserviceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AgendaserviceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
