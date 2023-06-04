import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Producto } from '../productos/interfaces/producto.interface';
import { Observable } from 'rxjs';
import { Categoria } from '../productos/interfaces/categoria.interface';

@Injectable({
  providedIn: 'root'
})
export class ProductosService {

  private productosUrl = "http://127.0.0.1:8000/tienda/productos/";
  private categoriasUrl = "http://127.0.0.1:8000/tienda/categorias/";

  constructor(private http: HttpClient) {  }

  // Productos
  getProductos(): Observable<Producto[]> {
    return this.http.get<Producto[]>(this.productosUrl);
  }

  addProducto(producto: Producto): Observable<Producto> {
    return this.http.post<Producto>(this.productosUrl, producto);
  }

  updateProducto(producto: Producto): Observable<Producto> {
    const url = `${this.productosUrl}${producto.id}/`;
    return this.http.put<Producto>(url, producto);
  }

  deleteProducto(id: number): Observable<{}> {
    const url = `${this.productosUrl}${id}/`;
    return this.http.delete(url);
  }

  // Categorias
  getCategorias(): Observable<Categoria[]> {
    return this.http.get<Categoria[]>(this.categoriasUrl);
  }

  addCategoria(categoria: Categoria): Observable<Categoria> {
    return this.http.post<Categoria>(this.categoriasUrl, categoria);
  }

  updateCategoria(categoria: Categoria): Observable<Categoria> {
    const url = `${this.categoriasUrl}${categoria.id}/`;
    return this.http.put<Categoria>(url, categoria);
  }

  deleteCategoria(id: number): Observable<{}> {
    const url = `${this.categoriasUrl}${id}/`;
    return this.http.delete(url);
  }
}

