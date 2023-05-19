/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { InstalacionesService } from './instalaciones.service';

describe('Service: Instalaciones', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [InstalacionesService]
    });
  });

  it('should ...', inject([InstalacionesService], (service: InstalacionesService) => {
    expect(service).toBeTruthy();
  }));
});
