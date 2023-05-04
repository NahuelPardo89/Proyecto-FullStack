import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InstalacionesComponent } from './modules/reservas/components/instalaciones/instalaciones.component';
import { AgendaComponent } from './modules/reservas/components/agenda/agenda.component';
import { ContactoComponent } from './modules/home/components/contacto/contacto.component';
import { ProductosComponent } from './modules/productos/components/productos/productos.component';
import { CarritoComponent } from './modules/productos/components/carrito/carrito.component';
import { AboutusComponent } from './modules/home/components/aboutus/aboutus.component';
const routes: Routes = [
  {path: 'home',loadChildren: () => import('./modules/home/home.module').then(m => m.HomeModule)},
  {path: 'dashboard',loadChildren: () => import('./modules/dashboard/dashboard.module').then(m => m.DashboardModule)},
  {path: 'auth',loadChildren: () => import('./modules/auth/auth.module').then(m => m.AuthModule)},
  {path: 'reservas', component: InstalacionesComponent },
  {path:'reservas/agenda', component: AgendaComponent },
  {path: 'contacto', component: ContactoComponent },
  {path: 'productos', component: ProductosComponent},
  {path: 'productos/carrito', component: CarritoComponent},
  {path:'**', redirectTo:'/home'},
  {path:'home/aboutus', component:AboutusComponent}
 ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
