import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ContactoComponent } from './components/contacto/contacto.component';
import { AboutusComponent } from './components/aboutus/aboutus.component';

const routes: Routes = [
  {path:'', component:HomeComponent},
  {path:'contacto', component:ContactoComponent},
  {path:'aboutus', component:AboutusComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomeRoutingModule { }
