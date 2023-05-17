import { Injectable } from '@angular/core';
import { carrito } from '../interfaces/carrito';

@Injectable({
  providedIn: 'root'
})
export class CarritoService {
  
  listaProductos: carrito[] = [
    {id: 1, producto: 'Pelota de futbol', cantidad: 1, precio: 280},
    {id: 2, producto: 'Raqueta de tenis', cantidad: 1, precio: 3500},
    {id: 5, producto: 'Nike AirMax', cantidad: 1, precio: 10500},
    {id: 8, producto: 'Medias deportivas', cantidad: 1, precio: 2800},
    {id: 4, producto: 'Botella de agua deportiva', cantidad: 1, precio: 1500},
    {id: 7, producto: 'Remera antisudor deportiva', cantidad: 1, precio: 1700},
   
  ];
  constructor() { }
//metodo para obtener todos los productos de la tabla del carrito
  getProducto(){
    return this.listaProductos.slice();
  }
//metodo para eliminar producto del tabla del carrito y BD(proximamente)
eliminarProducto(index: number){
  this.listaProductos.splice(index, 1);
}


}
