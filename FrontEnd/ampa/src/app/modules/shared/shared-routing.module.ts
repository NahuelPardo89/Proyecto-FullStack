import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes } from '@angular/router';
import { HomeComponent } from '../home/components/home/home.component';
import { ContactoComponent } from '../home/components/contacto/contacto.component';
import { AboutusComponent } from '../home/components/aboutus/aboutus.component';
import { DashboardComponent } from '../dashboard/dashboard/dashboard.component';
import { LoginComponent } from '../auth/components/login/login.component';
import { SinginComponent } from '../auth/components/singin/singin.component';




const routes: Routes = [

  {path: 'home', component: HomeComponent },//inicio
  {path:'contacto', component: ContactoComponent },//contacto
  {path: 'aboutus', component: AboutusComponent }, //sobre nosotros
  {path: 'servicios', component: DashboardComponent }, //servicios
  {path:'login', component: LoginComponent },//iniciar sesion
  {path: 'singin', component: SinginComponent }, //registro

];

@NgModule({
  declarations: [
    HomeComponent,
    ContactoComponent,
    AboutusComponent,
    DashboardComponent,
    LoginComponent,
    SinginComponent

  ],
  imports: [
    
    CommonModule
  ]
})
export class SharedRoutingModuleTsModule { }
