import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DetalleCarritoProducto } from '../interfaces/detalleCarrito.interface';


@Injectable({
  providedIn: 'root'
})
export class DetalleCarritoService {
  private apiUrl = "http://127.0.0.1:8000/tienda/detalles-carrito/"
  

  constructor(private http: HttpClient) {  }

  getDetallesCarrito(usuarioId: number): Observable<DetalleCarritoProducto[]> {
    return this.http.get<DetalleCarritoProducto[]>(`${this.apiUrl}?usuario=${usuarioId}`);
  }

  addProductoACarrito(detalle: DetalleCarritoProducto): Observable<DetalleCarritoProducto> {
    return this.http.post<DetalleCarritoProducto>(this.apiUrl, detalle);
  }

  updateDetalleCarrito(id: number, detalle: DetalleCarritoProducto): Observable<DetalleCarritoProducto> {
    return this.http.put<DetalleCarritoProducto>(`${this.apiUrl}${id}/`, detalle);
  }

  deleteDetalleCarrito(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }
}

