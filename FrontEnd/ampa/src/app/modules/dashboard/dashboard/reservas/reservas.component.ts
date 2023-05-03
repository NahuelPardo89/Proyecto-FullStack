import { Component } from '@angular/core';

@Component({
  selector: 'app-reservas',
  templateUrl: './reservas.component.html',
  styleUrls: ['./reservas.component.css']
})
export class ReservasComponent {
  
  
  
  //Aquí deberían ir datos de Back
  futbol = [
    {hora: "14",nombre: "Gustavo Recatti", cancha: 1},
    {hora: "16", nombre: "Osvaldo Portero", cancha: 1},
    {hora: "20", nombre: "Silvia Molina", cancha: 2}
  ]

  tenis= [{}

  ]

  padel = [{}

  ]

}
