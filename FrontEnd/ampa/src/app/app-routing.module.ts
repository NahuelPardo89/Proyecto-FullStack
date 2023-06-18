import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardUserComponent } from './modules/dashboard/dashboard-user/dashboard-user.component';

const routes: Routes = [
  {path: 'home',loadChildren: () => import('./modules/home/home.module').then(m => m.HomeModule)},
  {path: 'dashboard',loadChildren: () => import('./modules/dashboard/dashboard.module').then(m => m.DashboardModule)},
  {path: 'dashboard-test',loadChildren: () => import('./modules/dasboard-test/dasboard-test.module').then(m => m.DasboardTestModule)},
  {path: 'auth',loadChildren: () => import('./modules/auth/auth.module').then(m => m.AuthModule)},
  { path: 'dashboard-user', component: DashboardUserComponent },
  
  {path:'**', redirectTo:'/home'},
 ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
