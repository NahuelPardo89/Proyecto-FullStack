import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductosService {
 
  //archivo json que se consume
  private apiUrl = "../../../../../assets/data/productos.json"

  constructor(private http: HttpClient) {  }

  getProductos(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}
