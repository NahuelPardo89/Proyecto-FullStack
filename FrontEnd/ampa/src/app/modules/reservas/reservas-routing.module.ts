import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InstalacionesComponent } from './components/instalaciones/instalaciones.component';
import { AgendaComponent } from './components/agenda/agenda.component';

const routes: Routes = [
  {path:'', component:InstalacionesComponent},
  {path:'agenda', component:AgendaComponent}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ReservasRoutingModule { }
