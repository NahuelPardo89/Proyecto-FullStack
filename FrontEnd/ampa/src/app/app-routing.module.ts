import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InstalacionesComponent } from './modules/reservas/components/instalaciones/instalaciones.component';


const routes: Routes = [
  {path: 'home',loadChildren: () => import('./modules/home/home.module').then(m => m.HomeModule)},
  {path: 'dashboard',loadChildren: () => import('./modules/dashboard/dashboard.module').then(m => m.DashboardModule)},
  {path: 'auth',loadChildren: () => import('./modules/auth/auth.module').then(m => m.AuthModule)},
  {path: 'reservas', component: InstalacionesComponent },
  {path:'**', redirectTo:'/home'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
