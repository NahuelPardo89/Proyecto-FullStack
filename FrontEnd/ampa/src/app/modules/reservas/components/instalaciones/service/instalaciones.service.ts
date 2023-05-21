import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InstalacionesService {
  //archivo json que se consume
  private apiUrl = '../../../../../../assets/data/instalaciones.json';
  //constructor
  constructor(private http: HttpClient) { }
  //metodo para obtener los datos del json
  getInstalaciones(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

}
