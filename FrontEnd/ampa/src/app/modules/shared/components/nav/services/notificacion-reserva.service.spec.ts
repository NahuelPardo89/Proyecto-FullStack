import { TestBed } from '@angular/core/testing';

import { NotificacionReservaService } from './notificacion-reserva.service';

describe('NotificacionReservaService', () => {
  let service: NotificacionReservaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(NotificacionReservaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
