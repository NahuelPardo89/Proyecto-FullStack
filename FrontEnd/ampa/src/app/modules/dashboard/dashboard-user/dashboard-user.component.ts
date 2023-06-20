import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { AuthService } from '../../auth/services/auth.service';
import { User } from 'src/app/modules/auth/interfaces/user.interface';
import { AgendaserviceService } from '../../reservas/components/agenda/service/agendaservice.service';
import { InstalacionesService } from '../../reservas/components/instalaciones/service/instalaciones.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatDialog } from '@angular/material/dialog';
import { DialogEdicionComponent } from './dialog-edicion/dialog-edicion.component';
import { ReservaNotificacionService } from '../../shared/components/nav/services/notificacion-reserva.service';
import { FacturaService } from '../dashboard/factura/factura.service';



@Component({
  selector: 'app-dashboard-user',
  templateUrl: './dashboard-user.component.html',
  styleUrls: ['./dashboard-user.component.css']
})
export class DashboardUserComponent implements OnInit {
  
  
  loggedInUser: User | null = null;
  updatedUser: User | null = null;
  
  compras = "No hay compras a tu nombre";
  facturas: any[] = [];
  reservas: any[] = [];
  instalaciones: any[] = [];
  instalacionesMap: { [id: number]: string } = {};

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
    private instalacionesService: InstalacionesService,
    private snackBar: MatSnackBar,
    private dialog: MatDialog,
    private reservaNotificacionService: ReservaNotificacionService,
    private facturaService: FacturaService
  ) {
    this.instalaciones = [];
    
  }

  ngOnInit(): void {
    // Suscribirse a los cambios en el usuario actual
    this.authService.currentUser.subscribe(user => {
      this.loggedInUser = user;

      if (user) {
        this.obtenerReservasUsuario();
        this.facturaService.getFacturasPorUsuario(this.loggedInUser!.id).subscribe(facturas => {
          this.facturas = facturas;
          console.log(this.facturas)
        });
      }
    });

    // Obtener las instalaciones disponibles
    this.instalacionesService.getInstalaciones().subscribe(instalaciones => {
      this.instalaciones = instalaciones;
      
      
      this.instalacionesMap = instalaciones.reduce((map, instalacion) => {
        map[instalacion.idInstalacion] = instalacion.nombre;
        return map;
      }, {});

       
    });
  }
  // Editar datos de usuario actual
  editarDatos() {
    const dialogRef = this.dialog.open(DialogEdicionComponent, {
      width: '400px',
      data: this.loggedInUser
    });
  
    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        // Actualiza los datos del loggedInUser solo si el diálogo se cerró con éxito
        this.authService.getCurrentUser().subscribe(
          user => {
            if (user) {
              this.actualizarDatosUsuario(user); // Actualiza los datos del usuario en el componente
            } else {
              console.error('No se pudo obtener el usuario actual');
            }
          },
          error => {
            console.error('Error al obtener los datos del usuario:', error);
          }
        );
      }
      
      dialogRef.componentInstance.resetForm();
    });
  }
  
  actualizarDatosUsuario(user: User) {
    this.loggedInUser = user;
    
    
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

  eliminarReserva(idReserva: number) {
    this.agendaService.eliminarReserva(idReserva).subscribe(
      () => {
        this.reservas = this.reservas.filter(reserva => reserva.idReserva !== idReserva);
  
        this.snackBar.open('Reserva eliminada exitosamente', 'Cerrar', {
          duration: 3000, 
          horizontalPosition: 'center', 
          verticalPosition: 'bottom' 
        });
        this.reservaNotificacionService.notificarReservaGuardada();
      },
      error => {
        console.error('Error al eliminar la reserva:', error);
      }
    );
  }
  
}
