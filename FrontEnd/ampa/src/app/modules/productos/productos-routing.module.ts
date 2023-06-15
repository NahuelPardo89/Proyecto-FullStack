import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductosComponent } from './components/productos/productos.component';
import { CarritoComponent } from './components/carrito/carrito.component';
import { Carrito2Component } from './components/carrito2/carrito2.component';

const routes: Routes = [
  {path: '', component: ProductosComponent},
  {path: 'carrito', component: CarritoComponent},
  {path: 'carrito2', component: Carrito2Component}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductosRoutingModule { }
