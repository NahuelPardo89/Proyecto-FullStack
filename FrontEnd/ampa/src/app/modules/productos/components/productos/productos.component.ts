import { Component, OnInit } from '@angular/core';

import { ProductosService } from './productos.service';
import { Producto } from '../../interfaces/producto.interface';

@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css']
})
export class ProductosComponent implements OnInit {

  productos: Producto[];

  constructor(private productosService: ProductosService) {
    this.productos = [];
  }
  ngOnInit() {
    this.productosService.getProductos()
      .subscribe(data => {
        this.productos = data;
        console.log(this.productos)
      });
  }
}