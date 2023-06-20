import { Component } from '@angular/core';
import { InstalacionesService } from 'src/app/modules/reservas/components/instalaciones/service/instalaciones.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-instalaciones',
  templateUrl: './instalaciones.component.html',
  styleUrls: ['./instalaciones.component.css']
})
export class InstalacionesComponent {
  instalaciones: any[] = [];
  mostrarFormulario: boolean = false;
  nuevaInstalacion: any = {
    nombre: '',
    descripcion: '',
    foto: null,
    editandoInstalacion: true
  };

  constructor(private instalacionesService: InstalacionesService, private snackBar: MatSnackBar) {}

  ngOnInit() {
    this.actualizarListaInstalaciones();
  }

  actualizarListaInstalaciones() {
    this.instalacionesService.getInstalaciones().subscribe(instalaciones => {
      this.instalaciones = instalaciones.map(instalacion => ({
        ...instalacion,
        editandoNombre: false,
        editandoDescripcion: false,
      }));
    });
  }

  editarInstalacion(instalacion: any) {
    instalacion.editandoNombre = true;
    instalacion.editandoDescripcion = true;
    instalacion.editandoInstalacion = true;
  }
  
  cancelarEdicion(instalacion: any) {
    instalacion.editandoInstalacion = false;
  }
  
  agregarInstalacion() {
    const formData = new FormData();
    formData.append('nombre', this.nuevaInstalacion.nombre);
    formData.append('descripcion', this.nuevaInstalacion.descripcion);
    if (this.nuevaInstalacion.foto) {
      formData.append('foto', this.nuevaInstalacion.foto, this.nuevaInstalacion.foto.name);
    }
  
    this.instalacionesService.agregarInstalacion(formData).subscribe(
      response => {
        console.log('Instalación agregada:', response);
        this.actualizarListaInstalaciones(); 
        this.nuevaInstalacion = {
          nombre: '',
          descripcion: '',
          foto: null,
          editandoInstalacion: true
        };
        this.mostrarFormulario = false;
  
       
        this.snackBar.open('Instalación creada correctamente', 'Cerrar', {
          duration: 3000, 
        });
      },
      error => {
        console.error('Error al agregar la instalación:', error);
      }
    );
  }
  

  guardarInstalacion(instalacion: any) {
    const formData = new FormData();
    formData.append('nombre', instalacion.nombre);
    formData.append('descripcion', instalacion.descripcion);
    if (instalacion.foto) {
      formData.append('foto', instalacion.foto, instalacion.foto.name);
    }
  
    this.instalacionesService.editarInstalacion(instalacion.idInstalacion, formData).subscribe(
      response => {
        console.log('Instalación actualizada:', response);
        this.actualizarListaInstalaciones(); 
  
        // Mostrar MatSnackBar
        this.snackBar.open('Instalación actualizada correctamente', 'Cerrar', {
          duration: 3000, 
        });
      },
      error => {
        console.error('Error al actualizar la instalación:', error);
      }
    );
  }
  
  eliminarInstalacion(instalacion: any) {
    this.instalacionesService.eliminarInstalacion(instalacion.idInstalacion).subscribe(
      response => {
        console.log('Instalación eliminada:', response);
        this.actualizarListaInstalaciones(); 

        
        this.snackBar.open('Instalación eliminada correctamente', 'Cerrar', {
          duration: 3000, 
        });
      },
      error => {
        console.error('Error al eliminar la instalación:', error);
      }
    );
  }
  
  onFileSelected(event: any, instalacion: any) {
    const file = event.target.files[0];
    instalacion.foto = file;
  }
}
