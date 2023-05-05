import { Component } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';

@Component({
  selector: 'app-dashboard-user',
  templateUrl: './dashboard-user.component.html',
  styleUrls: ['./dashboard-user.component.css']
})
export class DashboardUserComponent {
  /** Based on the screen size, switch from standard to one column per row */
  cards = this.breakpointObserver.observe(Breakpoints.Handset).pipe(
    map(({ matches }) => {
      if (matches) {
        return [
          { title: 'Mi cuenta', cols: 1, rows: 1 },
          { title: 'Productos', cols: 1, rows: 1 },
          { title: 'Servicios', cols: 1, rows: 1 }
        ];
      }

      return [
        { title: 'Mi cuenta', cols: 2, rows: 1 },
        { title: 'Productos', cols: 1, rows: 1 },
        { title: 'Servicios', cols: 1, rows: 1 }
      ];
    })
  );

  constructor(private breakpointObserver: BreakpointObserver) {}
}
