import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { AuthService } from '../../auth/services/auth.service';
import { User } from 'src/app/modules/auth/interfaces/user.interface';
import { AgendaserviceService } from '../../reservas/components/agenda/service/agendaservice.service';
import { InstalacionesService } from '../../reservas/components/instalaciones/service/instalaciones.service';

@Component({
  selector: 'app-dashboard-user',
  templateUrl: './dashboard-user.component.html',
  styleUrls: ['./dashboard-user.component.css']
})
export class DashboardUserComponent implements OnInit {
  
  loggedInUser: User | null = null;

  compras = "No hay compras a tu nombre";
  reservas: any[] = [];
  instalaciones: any[] = [];
  instalacionesMap: { [id: number]: string } = {}; // Mapa para almacenar los nombres de las instalaciones

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

  constructor(
    private breakpointObserver: BreakpointObserver,
    private authService: AuthService,
    private agendaService: AgendaserviceService,
    private instalacionesService: InstalacionesService
  ) {
    this.instalaciones = [];
  }

  ngOnInit(): void {
    // Suscribirse a los cambios en el usuario actual
    this.authService.currentUser.subscribe(user => {
      this.loggedInUser = user;

      if (user) {
        this.obtenerReservasUsuario();
      }
    });

    // Obtener las instalaciones disponibles
    this.instalacionesService.getInstalaciones().subscribe(instalaciones => {
      this.instalaciones = instalaciones;
      
      // Crear un mapa de instalaciones utilizando el ID como clave y el nombre como valor
      this.instalacionesMap = instalaciones.reduce((map, instalacion) => {
        map[instalacion.idInstalacion] = instalacion.nombre;
        return map;
      }, {});
    });
  }

  // Obtener las reservas del usuario actual
  obtenerReservasUsuario() {
    if (this.loggedInUser) {
      const userId = this.loggedInUser.id;
  
      this.agendaService.obtenerReservasUsuario(userId).subscribe((reservas: any) => {
        this.reservas = reservas.length > 0 ? reservas : "No hay reservas a tu nombre";
        console.log(reservas);
      });
    }
  }
  
  // Obtener el nombre de la instalación según su ID
  obtenerNombreInstalacion(idInstalacion: number): string {
    return this.instalacionesMap[idInstalacion] || '';
  }
}
