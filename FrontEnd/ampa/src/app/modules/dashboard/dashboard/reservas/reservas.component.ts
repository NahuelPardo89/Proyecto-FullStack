import { Component } from '@angular/core';

@Component({
  selector: 'app-reservas',
  templateUrl: './reservas.component.html',
  styleUrls: ['./reservas.component.css']
})
export class ReservasComponent {
  
  
  
  //Aquí deberían ir datos de Back
  futbol = [
    {hora: "14:00",nombre: "Gustavo Recatti", cancha: 1},
    {hora: "16:00", nombre: "Osvaldo Portero", cancha: 1},
    {hora: "20:30", nombre: "Silvia Molina", cancha: 2}
  ]

  tenis= [
    {hora: "15:30",nombre: "Jorge Salinas", cancha: 1},
    {hora: "17:00", nombre: "Morena Ruxeman", cancha: 1},
    {hora: "21:00", nombre: "Paula Robledo", cancha: 2}
  ]

  padel = [
    {hora: "10:00",nombre: "Alejandro Galan", cancha: 1},
    {hora: "18:00", nombre: "Agustin Tapia", cancha: 1},
    {hora: "22:30", nombre: "Nicolas Bustos", cancha: 2}
    ]

  deporte:number = 1

  cambiarDeporte(n:number) {
    this.deporte = n
  }
}
