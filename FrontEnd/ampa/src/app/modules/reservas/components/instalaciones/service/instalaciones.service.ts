import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class InstalacionesService {
  //archivo json que se consume
  private apiUrl = "http://127.0.0.1:8000/instalaciones/instalaciones/";
  //constructor
  constructor(private http: HttpClient) { }
  //metodo para obtener los datos del json
  getInstalaciones(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl).pipe(
      map(response => response) // Extracción de los datos del objeto de respuesta
    );
  }
  

}
