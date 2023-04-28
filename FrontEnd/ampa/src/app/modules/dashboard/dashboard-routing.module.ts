import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {path: 'productos',loadChildren: () => import('../productos/productos.module').then(m => m.ProductosModule)},
  {path: 'reservas',loadChildren: () => import('../reservas/reservas.module').then(m => m.ReservasModule)},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardRoutingModule { }
