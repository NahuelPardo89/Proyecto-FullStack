import { Component, OnInit } from '@angular/core';

import { ProductosService } from '../../services/productos.service';
import { Producto } from '../../interfaces/producto.interface';

import { DetalleCarritoProducto } from '../../interfaces/detalleCarrito.interface';
import { DetalleCarritoService } from '../../services/detalle-carrito.service';

@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css']
})
export class ProductosComponent implements OnInit {

  productos: Producto[];

  constructor(private productosService: ProductosService,private detalleCarritoService: DetalleCarritoService) {
    this.productos = [];
  }
  ngOnInit() {
    this.productosService.getProductos()
      .subscribe(data => {
        this.productos = data;
        console.log(this.productos)
      });
  }
  addToCart(producto: Producto) {
    // Obtiene el usuario desde localStorage
    const userItem = localStorage.getItem('user');
    if (!userItem) {
        // No hay un usuario logueado. Puedes manejar este caso como necesites.
        console.error('No hay un usuario logueado');
        return;
    }

    const usuario = JSON.parse(userItem);
    
    const detalle: DetalleCarritoProducto = {
      usuario: usuario.id,
      producto: producto.id,
      cantidad: 1, // puedes cambiarlo según sea necesario
    };

    this.detalleCarritoService.addProductoACarrito(detalle)
      .subscribe(() => {
        console.log(`Producto ${producto.nombre} añadido al carrito`);
        // Aquí puedes hacer algo más, como mostrar una notificación al usuario
      }, error => {
        console.error(error);
        // Aquí puedes manejar el error, por ejemplo mostrar un mensaje de error al usuario
      });
  }
}