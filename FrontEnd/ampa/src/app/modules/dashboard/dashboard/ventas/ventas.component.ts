import { Component } from '@angular/core';

@Component({
  selector: 'app-ventas',
  templateUrl: './ventas.component.html',
  styleUrls: ['./ventas.component.css']
})
export class VentasComponent {
  
  //LOS PRODUCTOS VENDIDOS LLEGAN COMO OBJETO AQUI
  ventas = [
    {
      nombre:"Nike Air",
      categoria: "Zapatillas",
      img: "../../../../assets/img/nike-airmax-correlate.jpg",
      precio: "45.000"
    },
    {
      nombre:"Wilson Roland Garros",
      categoria:"Raquetas",
      img: "../../../../assets/img/WILSON-Roland-Garros.jpg",
      precio: "85.000"
    }
  ]


}
