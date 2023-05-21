import { Component } from '@angular/core';
import {MatTableModule} from '@angular/material/table';



export interface Cliente {
  name: string;
  dni: number;
  lastName: string;
  socio: boolean;
}

const ELEMENT_DATA: Cliente[] = [
  {dni: 19232198, name: 'Isaias', lastName: "Barrios" , socio: true},
  {dni: 22451158, name: 'Adalberto', lastName: "Tevez", socio: false},
  {dni: 32112341, name: 'Joao', lastName: "Gonzalez", socio: true},
  {dni:34884453, name: "Catriel", lastName: "Pardo", socio: true},
  ];


  @Component({
    selector: 'app-clientes',
    templateUrl: './clientes.component.html',
    styleUrls: ['./clientes.component.css']
  })
export class ClientesComponent {
  displayedColumns: string[] = ['dni', 'name', 'lastName', 'socio'];
  dataSource = ELEMENT_DATA;
}
