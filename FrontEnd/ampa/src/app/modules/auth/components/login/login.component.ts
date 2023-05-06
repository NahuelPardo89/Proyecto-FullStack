import { Component } from '@angular/core';
import { FormBuilder,  Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login.service';
import { LoginRequest } from '../../interfaces/loginRequest.interface';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  form=this.fb.group({
    dni:[,[Validators.required,Validators.pattern("^[0-9]*$"),Validators.min(1),Validators.max(999000000)] ],
    password:['', [Validators.required,Validators.minLength(8)]],
  })
  constructor(private fb:FormBuilder,  private _router:Router, private loginService:LoginService){
    
  }

  get dni() { 
    return this.form.controls.dni;
  }

  get password() { 
    return  this.form.controls.password; }

  login(){
    if (this.form.valid){
      this.loginService.login(this.form.value as LoginRequest).subscribe({
        next: (userData) => {
          console.log(userData)
          this.loginService.loggedInUserDni = this.form.value.dni ?? null;
        },
        error:(errorData) => {
          console.log(errorData)
        },
        complete:() => {
          console.log("login successful");
          this._router.navigateByUrl("/dashboard");
          this.form.reset();
        }
      })
      
    }
    else {
      
      this.error("asd")
    }
  }

  error(errorParams:string){
    
  }

}
