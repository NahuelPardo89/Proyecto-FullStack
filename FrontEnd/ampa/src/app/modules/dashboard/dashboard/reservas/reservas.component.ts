import { Component } from '@angular/core';
import { AgendaserviceService } from 'src/app/modules/reservas/components/agenda/service/agendaservice.service';
import { InstalacionesService } from 'src/app/modules/reservas/components/instalaciones/service/instalaciones.service';
import { MatSnackBar } from '@angular/material/snack-bar';


@Component({
  selector: 'app-reservas',
  templateUrl: './reservas.component.html',
  styleUrls: ['./reservas.component.css']
})
export class ReservasComponent {
  reservas: any[] = []; // Arreglo para almacenar las reservas
  instalaciones: any[] = [];
  instalacionesMap: { [id: number]: string } = {}; // Mapa para almacenar los nombres de las instalaciones

  usuarios: any[] = [];
  usuariosMap: { [id: number]: string } = {}; 


  constructor(
    private agendaService: AgendaserviceService,
    private snackBar: MatSnackBar,
    private instalacionesService: InstalacionesService) {
      this.instalaciones = [];
      this.usuarios = [];
    }

    ngOnInit() {
      // Obtener todas las reservas
      this.agendaService.obtenerTodasLasReservas().subscribe(
        (reservas: any[]) => {
          this.reservas = reservas;
          console.log('Reservas:', this.reservas);
        },
        (error) => {
          console.error('Error al obtener las reservas:', error);
        }
      );
      // Llamada al método obtenerTodosLosUsuarios()
      this.agendaService.obtenerTodosLosUsuarios().subscribe(
        usuarios => {
          console.log('Usuarios:', usuarios);
        },
        error => {
          console.error('Error al obtener usuarios:', error);
        }
      );
    
      // Obtener todas las reservas
      this.obtenerTodasLasReservas();
    
      this.agendaService.obtenerTodosLosUsuarios().subscribe(usuarios => {
        this.usuarios = usuarios;
        this.usuariosMap = usuarios.reduce((map, usuario) => {
          map[usuario.id] = `${usuario.nombre} ${usuario.apellido}`;
          return map;
        },{});
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
    
  obtenerTodasLasReservas() {
    this.agendaService.obtenerTodasLasReservas().subscribe(
      (reservas: any[]) => {
        this.reservas = reservas;
        // Imprimir el nombre de usuario para la primera reserva
        if (reservas.length > 0) {
          const primeraReserva = reservas[0];
          const nombreUsuario = this.obtenerNombreUsuario(primeraReserva.usuario);
          console.log('Nombre de Usuario:', nombreUsuario);
        }
      },
      (error) => {
        console.error(error);
      }
    );
  }
  
  eliminarReserva(idReserva: number) {
    this.agendaService.eliminarReserva(idReserva).subscribe(
      () => {
        this.reservas = this.reservas.filter(reserva => reserva.idReserva !== idReserva);
  
        this.snackBar.open('Reserva eliminada exitosamente', 'Cerrar', {
          duration: 3000, // Duración en milisegundos
          horizontalPosition: 'center', // Posición horizontal del Snackbar
          verticalPosition: 'bottom' // Posición vertical del Snackbar
        });
      },
      error => {
        console.error('Error al eliminar la reserva:', error);
      }
    );
  }
  
  // Obtener el nombre de la instalación según su ID
  obtenerNombreInstalacion(idInstalacion: number): string {
    return this.instalacionesMap[idInstalacion] || '';
  }

  obtenerNombreUsuario(userId: number): string {
    return this.usuariosMap[userId] || '';
  }
  
  
}
