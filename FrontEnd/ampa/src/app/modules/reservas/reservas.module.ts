import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReservasRoutingModule } from './reservas-routing.module';
import { InstalacionesComponent } from './components/instalaciones/instalaciones.component';
import { AgendaComponent } from './components/agenda/agenda.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    InstalacionesComponent,
    AgendaComponent,
  ],
  imports: [
    CommonModule,
    ReservasRoutingModule,
    HttpClientModule
  ]
})
export class ReservasModule { }
