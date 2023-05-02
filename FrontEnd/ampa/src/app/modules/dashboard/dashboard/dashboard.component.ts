import { Component } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';







@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  /** Based on the screen size, switch from standard to one column per row */
  cards = this.breakpointObserver.observe(Breakpoints.Handset).pipe(
    map(({ matches }) => {
      if (matches) {
        return [
          { title: 'Ventas', cols: 1, rows: 1 },
          { title: 'Reservas', cols: 1, rows: 1 },
          { title: 'Clientes', cols: 1, rows: 1 },
          { title: 'Ingresos', cols: 1, rows: 1 }
        ];
      }

      return [
        { title: 'Ventas', cols: 2, rows: 1 },
        { title: 'Reservas', cols: 1, rows: 1 },
        { title: 'Clientes', cols: 1, rows: 2 },
        { title: 'Ingresos', cols: 1, rows: 1 }
      ];
    })
  );
    
  
  
  //----------------------------
  //CLIENTES

   



  
  constructor(private breakpointObserver: BreakpointObserver) {}
}


