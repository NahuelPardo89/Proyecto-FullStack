import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReservaNotificacionService {
  private reservaGuardadaSource = new Subject<void>();
  reservaGuardada$ = this.reservaGuardadaSource.asObservable();

  notificarReservaGuardada() {
    this.reservaGuardadaSource.next();
  }
}
