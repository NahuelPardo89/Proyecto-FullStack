import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class FacturaService {

  private apiUrl = "http://127.0.0.1:8000/tienda/factura/"

  constructor(private http: HttpClient) {  }

  getFacturas(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
