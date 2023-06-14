import { Component } from '@angular/core';
import { User } from 'src/app/modules/auth/interfaces/user.interface';
import { Subscription } from 'rxjs';
import { AuthService } from 'src/app/modules/auth/services/auth.service';
import { InstalacionesService } from '../instalaciones/service/instalaciones.service';
import { AgendaserviceService } from './service/agendaservice.service';
import { DatePipe } from '@angular/common';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-agenda',
  templateUrl: './agenda.component.html',
  styleUrls: ['./agenda.component.css']
})
export class AgendaComponent {
  user: User | null = null;
  subscription!: Subscription;
  instalaciones: any[] = [];
  hora: string = '';
  InstalacionSeleccionada: string = '';
  fecha: Date | null = null;
  selectedTime: string = '';
  
  //prueba

  //variable fecha y selector
  date: Date = new Date();
  selectedDate: Date | null = null;
  //variable hora y minutos y selector
  selectedHour: string = '';
  selectedMinute: string = '';

  onHourChange(event: any) {
    this.selectedHour = event.target.value;
    // Realiza acciones adicionales con la hora seleccionada
  }

  onMinuteChange(event: any) {
    this.selectedMinute = event.target.value;
    // Realiza acciones adicionales con los minutos seleccionados
  }





  constructor(
    private authService: AuthService,
    private instalacionesService: InstalacionesService,
    private agendaService: AgendaserviceService,
    private datePipe: DatePipe,
    private snackBar: MatSnackBar
  ) {}

  ngOnInit(): void {
    this.subscription = this.authService.currentUser.subscribe(user => {
      this.user = user;
      this.instalaciones = [];
      this.instalacionesService.getInstalaciones().subscribe(instalaciones => {
        this.instalaciones = instalaciones;
      });
    });
  }

  guardarReserva() {
    console.log('Valor de fecha:', this.selectedDate);
    const formattedDate = this.datePipe.transform(this.selectedDate, 'yyyy-MM-dd');
    console.log('Fecha formateada:', formattedDate);

    const horaCompleta = this.selectedHour + ':' + this.selectedMinute;

    const reserva = {
      fecha: formattedDate,
      hora: horaCompleta,
      usuario: this.user?.id,
      instalaciones: this.InstalacionSeleccionada,
    };
  
    this.agendaService.crearReserva(reserva).subscribe(
      response => {
        console.log('Reserva creada exitosamente', response);
        this.mostrarSnackbar('Reserva creada exitosamente');
        // Realizar cualquier acción adicional después de crear la reserva
      },
      error => {
        console.error('Error al crear la reserva', error);
        this.mostrarErrorSnackbar('Error al crear la reserva, verifique los campos seleccionados.');
        // Manejar el error de acuerdo a tus necesidades
      }
    );
  }
  
  filtroFecha = (fecha: Date | null) => {
    // Define aquí cualquier filtro de fechas que desees aplicar
    // Puedes retornar true si deseas permitir todas las fechas
    // o false para deshabilitar fechas específicas.
    return true;
  }

  mostrarSnackbar(mensaje: string) {
    this.snackBar.open(mensaje, 'Cerrar', {
      duration: 3000, // Duración en milisegundos
      horizontalPosition: 'center',
      verticalPosition: 'bottom'
    });
  }
  mostrarErrorSnackbar(mensaje: string) {
    this.snackBar.open(mensaje, 'Cerrar');
  }
}