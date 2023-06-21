import { TestBed } from '@angular/core/testing';

import { Carrito2Service } from './carrito2.service';

describe('Carrito2Service', () => {
  let service: Carrito2Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Carrito2Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
