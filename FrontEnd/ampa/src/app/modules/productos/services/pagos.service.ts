import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class PagosService {

  private API_URL = 'http://127.0.0.1:8000/tienda/pagos/';  

  constructor(private http: HttpClient) { }

  realizarPago(pago: any): Observable<any> {
    return this.http.post<any>(this.API_URL, pago);
  }
}
