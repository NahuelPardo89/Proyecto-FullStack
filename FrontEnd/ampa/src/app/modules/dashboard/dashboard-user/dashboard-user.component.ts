import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { AuthService } from '../../auth/services/auth.service';
import { User } from 'src/app/modules/auth/interfaces/user.interface';

@Component({
  selector: 'app-dashboard-user',
  templateUrl: './dashboard-user.component.html',
  styleUrls: ['./dashboard-user.component.css']
})
export class DashboardUserComponent implements OnInit {
  
  loggedInUser: User | null = null;

  compras= "No hay compras a tu nombre"
  reservas= "No hay reservas a tu nombre"

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

  constructor(private breakpointObserver: BreakpointObserver, private authService: AuthService) {}

  ngOnInit(): void {
    this.authService.currentUser.subscribe(user => {
      this.loggedInUser = user;
    });
  }
}