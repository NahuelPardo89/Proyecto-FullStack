import { Injectable } from '@angular/core';
import { LoginRequest } from '../interfaces/loginRequest.interface';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';
import { User } from '../interfaces/user.interface';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http:HttpClient) { }

  login(credenciales:LoginRequest):Observable<User>{
    return this.http.get<User>('../../../../assets/data/data.json').pipe(
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
}
