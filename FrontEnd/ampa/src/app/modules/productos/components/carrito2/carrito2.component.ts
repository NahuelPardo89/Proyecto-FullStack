import { Component, OnInit } from '@angular/core';
import { Carrito2Service } from './carrito2.service';
import { DetalleCarritoService } from '../../services/detalle-carrito.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-carrito2',
  templateUrl: './carrito2.component.html',
  styleUrls: ['./carrito2.component.css']
})
export class Carrito2Component implements OnInit {

  carrito: any = null;

  constructor(private carritoService: Carrito2Service,private detalleCarritoService: DetalleCarritoService,private router: Router,) { }

  ngOnInit(): void {
    const usuarioString = localStorage.getItem('user');
     
    if (usuarioString !== null) {
      const usuario = JSON.parse(usuarioString);
      const usuarioId = usuario.id;
        
      this.carritoService.getCarrito(usuarioId).subscribe(data => {
        this.carrito = data;
        for (let detalle of this.carrito.detalles) {
          this.carritoService.getProductoDetails(detalle.producto).subscribe(producto => {
            detalle.producto = producto;
          });
        }
      });
    }
  }
  eliminarProducto(detalle: any) {
    this.detalleCarritoService.deleteDetalleCarrito(detalle.id).subscribe(() => {
      // Remover el detalle del arreglo local tras una eliminación exitosa
      this.carrito.detalles = this.carrito.detalles.filter((item: any) => item.id !== detalle.id);
    }, error => {
      console.log(error);
      // Manejar error aquí
    });
  }
  finalizarCompra(){
    this.router.navigateByUrl('dashboard/productos/pagos');
  }

}