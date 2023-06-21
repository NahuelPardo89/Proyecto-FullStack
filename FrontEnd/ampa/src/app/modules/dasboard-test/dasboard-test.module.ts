import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DasboardTestRoutingModule } from './dasboard-test-routing.module';
import { DashboardAdminComponent } from './dashboard-admin/dashboard-admin.component';
import { ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatTableModule } from '@angular/material/table';
import {MatButtonModule} from '@angular/material/button';

  
@NgModule({
  declarations: [
    DashboardAdminComponent,
    
  ],
  imports: [
    CommonModule,
    DasboardTestRoutingModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatTableModule,
    MatButtonModule

  ]
})
export class DasboardTestModule { }
