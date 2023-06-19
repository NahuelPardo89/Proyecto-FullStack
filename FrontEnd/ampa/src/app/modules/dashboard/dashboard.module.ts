import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';


import { DashboardRoutingModule } from './dashboard-routing.module';
import { DashboardNavComponent } from './dashboard-nav/dashboard-nav.component';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatCardModule } from '@angular/material/card';
import { MatMenuModule } from '@angular/material/menu';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatTableModule } from '@angular/material/table';
import { DashboardUserComponent } from './dashboard-user/dashboard-user.component';

import { ReactiveFormsModule } from '@angular/forms';

import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';

import { FormsModule } from '@angular/forms';
import { VentasComponent } from './dashboard/ventas/ventas.component';
import { ClientesComponent } from './dashboard/clientes/clientes.component';
import { ReservasComponent } from './dashboard/reservas/reservas.component';
import { IngresosComponent } from './dashboard/ingresos/ingresos.component';
import { ConfirmDialogComponent } from './dashboard/clientes/confirm-dialog/confirm-dialog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { InstalacionesComponent } from './dashboard/instalaciones/instalaciones/instalaciones.component';
import { FacturaComponent } from './dashboard/factura/factura.component';







@NgModule({
  declarations: [
    DashboardNavComponent,
    DashboardComponent,
    VentasComponent,
    ClientesComponent,
    ReservasComponent,
    IngresosComponent,
    DashboardUserComponent,
    ConfirmDialogComponent,
    InstalacionesComponent,
    FacturaComponent,
   
   
  
    
   
    
    
  ],
  imports: [
    CommonModule,
    DashboardRoutingModule,
    LayoutModule,
    MatToolbarModule,
    MatButtonModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatGridListModule,
    MatCardModule,
    MatMenuModule,
    MatFormFieldModule,
    MatTableModule,
    MatButtonModule,
    ReactiveFormsModule,
    MatInputModule,
    MatSelectModule,
    MatDialogModule,
    MatSnackBarModule,
    FormsModule,
    
    
    
  ]
})
export class DashboardModule { }
