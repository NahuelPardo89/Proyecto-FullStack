import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReservasRoutingModule } from './reservas-routing.module';
import { InstalacionesComponent } from './components/instalaciones/instalaciones.component';
import { AgendaComponent } from './components/agenda/agenda.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatNativeDateModule} from '@angular/material/core';
import { DatePipe } from '@angular/common';
import { MatSnackBarModule } from '@angular/material/snack-bar';
@NgModule({
  declarations: [
    InstalacionesComponent,
    AgendaComponent,
  ],
  imports: [
    CommonModule,
    ReservasRoutingModule,
    HttpClientModule,
    FormsModule,
    MatDatepickerModule,
    MatInputModule,
    MatFormFieldModule,
    MatNativeDateModule,
    MatSnackBarModule
  ],
  providers: [
    DatePipe // Agrega DatePipe en la lista de proveedores
  ]
})
export class ReservasModule { }
