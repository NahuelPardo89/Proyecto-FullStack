import { Injectable } from '@angular/core';
import { LoginRequest } from '../interfaces/loginRequest.interface';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, throwError, BehaviorSubject, tap } from 'rxjs';
import { User } from '../interfaces/user.interface';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  currentUserLoginON: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  currentUserData: BehaviorSubject<User> = new BehaviorSubject<User>({dni:0,nombre:'',apellido:'',teléfono:'',direccion:'',email:'',idCiudad:0,grupo:''})


  loggedInUserDni: number | null = null;
  constructor(private http:HttpClient,) { }

  login(credenciales:LoginRequest):Observable<User>{
    return this.http.get<User>('../../../../assets/data/data.json').pipe(
      tap(userData => {
        this.currentUserData.next(userData);
        this.currentUserLoginON.next(true);
      }),
      catchError(this.errorHandler)
    )
  }
  

  private errorHandler(error:HttpErrorResponse){
    if (error.status===0){
      console.error("se ha producido un error:",error.error)
    }
    else{
      console.error("el Backend retorno el código de estado:", error.status,error.error)
    }
    return throwError(()=> new Error('Algo falló. Por favor intente nuevamente'))
  }
  get userData(): Observable<User>{
    return this.currentUserData.asObservable();
  }
  get userLoginOn(): Observable<boolean>{
    return this.currentUserLoginON.asObservable();
  }
}
