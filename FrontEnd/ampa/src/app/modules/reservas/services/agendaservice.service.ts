import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
interface Reserva {
  idReserva: number;
  fecha: string;
  hora: string;
  costo: string;
  usuario: string; 
  instalaciones: string; 
}

@Injectable({
  providedIn: 'root'
})
export class AgendaserviceService {

  constructor(private http: HttpClient) { }
  
  crearReserva(reserva: any) {
    return this.http.post('http://127.0.0.1:8000/reservas/reservas/', reserva);
  }


  obtenerReservasUsuario(userId: number): Observable<Reserva[]> {
    const url = `http://127.0.0.1:8000/reservas/reservas/?usuario=${userId}`;
    return this.http.get<Reserva[]>(url);
  }
  

  obtenerInstalaciones(): Observable<any[]> {
    const url = `http://127.0.0.1:8000/instalaciones/`;
    return this.http.get<any[]>(url);
  }
  
  obtenerTodasLasReservas(): Observable<Reserva[]> {
  const url = 'http://127.0.0.1:8000/reservas/reservas/';
  return this.http.get<Reserva[]>(url);
}

eliminarReserva(idReserva: number): Observable<any> {
  const url = `http://127.0.0.1:8000/reservas/reservas/${idReserva}/`;
  return this.http.delete(url);
}

obtenerTodosLosUsuarios(): Observable<any[]> {
  const url = 'http://127.0.0.1:8000/usuarios/usuarios/';
  return this.http.get<any[]>(url);
}
}
