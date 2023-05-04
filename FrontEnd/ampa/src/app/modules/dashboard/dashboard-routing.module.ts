import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardNavComponent } from './dashboard-nav/dashboard-nav.component';


const routes: Routes = [
  {path:'admin', component: DashboardNavComponent},
  {path: 'productos',loadChildren: () => import('../productos/productos.module').then(m => m.ProductosModule)},
  {path: 'reservas',loadChildren: () => import('../reservas/reservas.module').then(m => m.ReservasModule)},
 
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardRoutingModule { }
