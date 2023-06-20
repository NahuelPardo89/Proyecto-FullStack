import { Component } from '@angular/core';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  ventasVisible = false;
  usuariosVisible = false;
  reservasVisible = false;
  instalacionesVisible = false;
  productosVisible = false;

  constructor(private breakpointObserver: BreakpointObserver) {}

  mostrarProductos() {
    this.productosVisible = !this.productosVisible;
  }
  mostrarVentas(){
    this.ventasVisible = !this.ventasVisible;
  }


  mostrarUsuarios() {
    this.usuariosVisible = !this.usuariosVisible;
  }

  mostrarReservas() {
    this.reservasVisible = !this.reservasVisible;
  }

  mostrarInstalaciones() {
    this.instalacionesVisible = !this.instalacionesVisible;
  }
}
