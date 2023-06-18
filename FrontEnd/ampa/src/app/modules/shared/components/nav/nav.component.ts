import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { User } from 'src/app/modules/auth/interfaces/user.interface';
import { AuthService } from 'src/app/modules/auth/services/auth.service';
import { AgendaserviceService } from 'src/app/modules/reservas/components/agenda/service/agendaservice.service';
import { ReservaNotificacionService } from './services/notificacion-reserva.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit, OnDestroy {
  user: User | null = null;
  subscription!: Subscription;
  reservas: any[] = [];
  loggedInUser: User | null = null;
  totalReservations: number = 0;

  constructor(
    private authService: AuthService,
    private agendaService: AgendaserviceService,
    private reservaNotificacionService: ReservaNotificacionService
  ) {}

  ngOnInit(): void {
    this.subscription = this.authService.currentUser.subscribe(user => {
      this.user = user;
      this.loggedInUser = user; // Asignar el usuario actual a loggedInUser
      if (user) {
        this.obtenerReservasUsuario();
      }
    });

    this.reservaNotificacionService.reservaGuardada$.subscribe(() => {
      this.obtenerReservasUsuario();
    });
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  obtenerReservasUsuario() {
    if (this.loggedInUser) {
      const userId = this.loggedInUser.id;

      this.agendaService.obtenerReservasUsuario(userId).subscribe((reservas: any) => {
        this.reservas = reservas.length > 0 ? reservas : [];
        this.totalReservations = reservas.length;
        console.log(this.totalReservations);
      });
    }
  }

  logout() {
    const refreshToken = localStorage.getItem('refresh_token');
    if (refreshToken) {
      this.authService.logout(refreshToken).subscribe(() => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('user');
        this.user = null;
        this.loggedInUser = null; // Restablecer loggedInUser al cerrar sesión
      });
    }
  }
}
