import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Usuario } from '../productos/interfaces/usuario.interface';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuariosService {

  private usuariosUrl = "http://127.0.0.1:8000/usuarios/usuarios/";

  constructor(private http: HttpClient) { }

  addUser(usuario: Usuario): Observable<Usuario> {
    return this.http.post<Usuario>(this.usuariosUrl, usuario);
  }

  updateUser(usuario: Usuario): Observable<Usuario> {
    const url = `${this.usuariosUrl}${usuario.id}/`;
    return this.http.put<Usuario>(url, usuario);
  }

  deleteUser(id: number): Observable<any> {
    const url = `${this.usuariosUrl}${id}/`;
    return this.http.delete(url);
  }

  getUser(id: number): Observable<Usuario> {
    const url = `${this.usuariosUrl}/${id}/`;
    return this.http.get<Usuario>(url);
  }

  getUsers(): Observable<Usuario[]> {
    return this.http.get<Usuario[]>(this.usuariosUrl);
  }
}
