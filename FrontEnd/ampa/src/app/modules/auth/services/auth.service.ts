import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable,Output, EventEmitter } from '@angular/core';
import { Observable } from 'rxjs';

import { JwtResponse } from '../interfaces/jwtResponse.interface';
import { LoginUser } from '../interfaces/login.interface';
import { RegisterUser } from '../interfaces/register.interface';
import { tap } from 'rxjs/operators'; 
import { BehaviorSubject } from 'rxjs';
import { User } from '../interfaces/user.interface';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private loginUrl = 'http://localhost:8000/usuarios/login/';
  private registerUrl = 'http://localhost:8000/usuarios/register/';
  private logoutUrl = 'http://localhost:8000/usuarios/logout/';
  
  // Añadir esto
  private currentUserSubject: BehaviorSubject<User | null> = new BehaviorSubject<User | null>(null);
  public readonly currentUser = this.currentUserSubject.asObservable();

  
  constructor(private http: HttpClient) {
    const user = localStorage.getItem('user');
    if (user) {
      this.currentUserSubject.next(JSON.parse(user));
    }
  }
  login(user: LoginUser): Observable<JwtResponse> {
    return this.http.post<JwtResponse>(this.loginUrl, user).pipe(
      tap(response => {
        // Cuando un usuario inicia sesión, actualiza currentUserSubject.
        localStorage.setItem('user', JSON.stringify(response.user));
        this.currentUserSubject.next(response.user);
        
        
      })
    );
  }
 
  register(user: RegisterUser): Observable<JwtResponse> {
    return this.http.post<JwtResponse>(this.registerUrl, user).pipe(
      tap(response => {
        // Cuando un usuario se registra, actualiza currentUserSubject.
        this.currentUserSubject.next(response.user);
        
        
      })
    );
  }

  logout(refreshToken: string): Observable<void> {
    const headers = new HttpHeaders().set('Authorization', 'Bearer ' + localStorage.getItem('access_token'));
    return this.http.post<void>(this.logoutUrl, { refresh: refreshToken }, { headers: headers }).pipe(
      tap(() => {
        this.currentUserSubject.next(null);
      })
    );
  }
}