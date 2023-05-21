import { Component, OnDestroy, OnInit } from '@angular/core';
import { LoginService } from 'src/app/modules/auth/services/login.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit, OnDestroy {
  userLoginOn:boolean = false;

  constructor(private _loginService:LoginService){}
  ngOnDestroy(): void {
    this._loginService.currentUserLoginON.unsubscribe();
  }

  ngOnInit(): void {
      this._loginService.currentUserLoginON.subscribe({
        next:(userLoginOn) =>{
          this.userLoginOn = userLoginOn;
        }
      })
  }
  // Revisar
  logout(){
    this.userLoginOn = false;
    
  }

  
}
