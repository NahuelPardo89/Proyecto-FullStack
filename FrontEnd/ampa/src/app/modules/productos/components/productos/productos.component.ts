import { Component, OnInit } from '@angular/core';

import { ProductosService } from '../../services/productos.service';
import { Producto } from '../../interfaces/producto.interface';

import { DetalleCarritoProducto } from '../../interfaces/detalleCarrito.interface';
import { DetalleCarritoService } from '../../services/detalle-carrito.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css']
})
export class ProductosComponent implements OnInit {

  productos: Producto[];
  

  constructor(private productosService: ProductosService,private detalleCarritoService: DetalleCarritoService,private router: Router) {
    this.productos = [];
  }
  ngOnInit() {
    this.productosService.getProductos()
      .subscribe(data => {
        this.productos = data.map(producto => ({ 
          ...producto, 
          estaEnCarrito: false ,
        
        }));
        
      });
  }
  addToCart(producto: Producto) {
    // Obtiene el usuario desde localStorage
    const userItem = localStorage.getItem('user');
    if (!userItem) {
       
        console.error('No hay un usuario logueado');
        return;
    }

    const usuario = JSON.parse(userItem);
    
    const detalle: DetalleCarritoProducto = {
      usuario: usuario.id,
      producto: producto.id,
      cantidad: 1, 
    };

    this.detalleCarritoService.addProductoACarrito(detalle)
      .subscribe(() => {
        console.log(`Producto ${producto.nombre} añadido al carrito`);
        producto.estaEnCarrito = true;
        
      }, error => {
        console.error(error);
       
      });
  }
  carro(){
    this.router.navigate(['/dashboard/productos/carrito2'])
  }
}