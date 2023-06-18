import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProductosRoutingModule } from './productos-routing.module';
import { ProductosComponent } from './components/productos/productos.component';
import { CarritoComponent } from './components/carrito/carrito.component';
import {MatTableModule} from '@angular/material/table';
import { MatIconModule } from '@angular/material/icon';
import {MatTooltipModule} from '@angular/material/tooltip';
import {MatPaginatorModule} from '@angular/material/paginator';
import {MatSortModule} from '@angular/material/sort';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import { Carrito2Component } from './components/carrito2/carrito2.component';
import { PasarelaPagosComponent } from './components/pasarela-pagos/pasarela-pagos.component';

@NgModule({
  declarations: [
    ProductosComponent,
    CarritoComponent,
    Carrito2Component,
    PasarelaPagosComponent
  ],
  imports: [
    CommonModule,
    ProductosRoutingModule,
    MatTableModule,
    MatIconModule,
    MatTooltipModule,
    MatPaginatorModule,
    MatSortModule,
    MatSnackBarModule,
    MatButtonModule,
    MatCardModule,
  ],
})
export class ProductosModule { }
