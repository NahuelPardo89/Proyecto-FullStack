import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReservasRoutingModule } from './reservas-routing.module';
import { InstalacionesComponent } from './components/instalaciones/instalaciones.component';
import { AgendaComponent } from './components/agenda/agenda.component';


@NgModule({
  declarations: [
    InstalacionesComponent,
    AgendaComponent,
  ],
  imports: [
    CommonModule,
    ReservasRoutingModule,
  
  ]
})
export class ReservasModule { }
