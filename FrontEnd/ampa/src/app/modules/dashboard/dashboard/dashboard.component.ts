import { Component } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';





@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  /** Based on the screen size, switch from standard to one column per row */
  
  ventas:boolean = false;
  mostrarVentas(){
    this.ventas = !this.ventas;
  }

  usuarios:boolean = false;
  mostrarUsuarios() {
    this.usuarios = !this.usuarios;
  }
    
  
  
  //----------------------------
  //CLIENTES

   



  
  constructor(private breakpointObserver: BreakpointObserver) {}
}


