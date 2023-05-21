import { Component } from '@angular/core';

@Component({
  selector: 'app-ingresos',
  templateUrl: './ingresos.component.html',
  styleUrls: ['./ingresos.component.css']
})
export class IngresosComponent {
  ingresos:[number] = [0]


  sumarProductos(productos:number[]): number {
    return productos.reduce((total,producto) => total + producto, 0)
  }
  productos = [45000,85000]
  sumaProd = this.sumarProductos(this.productos)
  //Por Cada producto vendido debería llegar su valor aquí
  


  //Por Cada turno alquilado debería llegar su valor aquí
  servicios = [2400,2400,1800,2400,1800,2600,2400]
  sumaServ = this.sumarProductos(this.servicios)

  total = this.sumaProd + this.sumaServ

  
}
