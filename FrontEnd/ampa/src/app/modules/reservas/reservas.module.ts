import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReservasRoutingModule } from './reservas-routing.module';
import { InstalacionesComponent } from './components/instalaciones/instalaciones.component';


@NgModule({
  declarations: [
    InstalacionesComponent
  ],
  imports: [
    CommonModule,
    ReservasRoutingModule
  ]
})
export class ReservasModule { }
