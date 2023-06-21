import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class InstalacionesService {
  private apiUrl = "http://127.0.0.1:8000/instalaciones/instalaciones/";

  constructor(private http: HttpClient) { }

  getInstalaciones(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl).pipe(
      map(response => response)
    );
  }

  editarInstalacion(idInstalacion: number, formData: FormData): Observable<any> {
    const url = `${this.apiUrl}${idInstalacion}/`;

    const headers = new HttpHeaders();
    headers.append('enctype', 'multipart/form-data');

    return this.http.put(url, formData, { headers: headers });
  }

  agregarInstalacion(instalacion: FormData): Observable<any> {
    const headers = new HttpHeaders();
    headers.append('enctype', 'multipart/form-data');

    return this.http.post(this.apiUrl, instalacion, { headers: headers });
  }

  eliminarInstalacion(idInstalacion: number): Observable<any> {
    const url = `${this.apiUrl}${idInstalacion}/`;
    return this.http.delete(url);
  }
}
