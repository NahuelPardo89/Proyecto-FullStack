import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AgendaserviceService {

  constructor(private http: HttpClient) { }
  
  crearReserva(reserva: any) {
    return this.http.post('http://127.0.0.1:8000/reservas/reservas/', reserva);
  }


  obtenerReservasUsuario() {
    return this.http.get('http://127.0.0.1:8000/reservas/reservas/');
  }
  
}
