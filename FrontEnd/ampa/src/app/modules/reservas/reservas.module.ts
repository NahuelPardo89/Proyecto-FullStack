import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReservasRoutingModule } from './reservas-routing.module';
import { InstalacionesComponent } from './components/instalaciones/instalaciones.component';
import { AgendaComponent } from './components/agenda/agenda.component';
import {MatDatepickerModule} from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';

@NgModule({
  declarations: [
    InstalacionesComponent,
    AgendaComponent,
  ],
  imports: [
    CommonModule,
    ReservasRoutingModule,
    MatDatepickerModule,
    MatNativeDateModule,
  
  ],
  exports: [
    MatDatepickerModule,
    MatNativeDateModule,

  ]
})
export class ReservasModule { }
