import { Component, OnInit } from '@angular/core';
import { ProductosService } from './productos.service';


@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.css']
})
export class ProductosComponent implements OnInit {

  productos: any[];


  constructor(private ProductosService: ProductosService) {
    this.productos = [];
  }
  ngOnInit() {
    this.ProductosService.getProductos()
      .subscribe(data => {
        this.productos = data.productos;
      });
  }
}
