import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ProductosService } from '../../services/productos.service';

@Injectable({
  providedIn: 'root'
})
export class Carrito2Service {

  private API_URL = 'http://127.0.0.1:8000/tienda/carritos/';  

  constructor(private http: HttpClient,private productoService: ProductosService) { }

  getCarrito(usuarioId: number): Observable<any> {
    return this.http.get(`${this.API_URL}${usuarioId}/`);  
  }

  getProductoDetails(id: number): Observable<any> {
    return this.productoService.getProducto(id);
  }
}