import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


// MODULOS
import { SharedModule } from './modules/shared/shared.module';
import { ReservasModule } from './modules/reservas/reservas.module';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    SharedModule,
    ReservasModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
