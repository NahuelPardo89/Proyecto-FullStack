import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Usuario } from 'src/app/modules/productos/interfaces/usuario.interface';
import { UsuariosService } from '../../usuarios.service';
import { MatDialog } from '@angular/material/dialog';
import { ConfirmDialogComponent } from './confirm-dialog/confirm-dialog.component';

@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.css']
})
export class ClientesComponent implements OnInit {
  
  selectedUserId: number | undefined;
  editMode = false;
  usuarios: Usuario[] = [];
  usuarioForm: FormGroup;
  mostrarFormulario = false;

  constructor(private usuariosService: UsuariosService, private fb: FormBuilder, private dialog: MatDialog) {
    this.usuarioForm = this.fb.group({
      dni: ['', Validators.required],
      nombre: ['', Validators.required],
      apellido: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      telefono: ['', Validators.required],
      direccion: ['', Validators.required],
      is_active: [true],
      is_staff: [false],
    });
  }

  ngOnInit(): void {
    this.fetchData();
  }

  fetchData(): void {
    this.usuariosService.getUsers().subscribe(data => {
      this.usuarios = data;
    });
  }

  agregarUsuario(): void {
    const nuevoUsuario: Usuario = this.usuarioForm.value;
    this.usuariosService.addUser(nuevoUsuario).subscribe(usuario => {
      this.usuarios.push(usuario);
      this.usuarioForm.reset();
      // Obtener la lista actualizada de usuarios
      this.fetchData();
    });
  }

  editarUsuario(usuario: Usuario, id: number): void {
    this.editMode = true;
    this.usuarioForm.patchValue(usuario);
    this.selectedUserId = id;
    this.mostrarFormulario = true;
  }

  borrarUsuario(usuario: Usuario): void {
    const dialogRef = this.dialog.open(ConfirmDialogComponent, {
      data: {
        message: `Seguro quieres eliminar a ${usuario.nombre} ${usuario.apellido}? Se eliminará definitivamente.`
      }
    });
  
    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.usuariosService.deleteUser(usuario.id).subscribe(() => {
          const index = this.usuarios.findIndex(u => u.id === usuario.id);
          this.usuarios.splice(index, 1);
          // Obtener la lista actualizada de usuarios
          this.fetchData();
        });
      }
    });
  }

  guardarUsuario(): void {
    const usuario = this.usuarioForm.value;
    this.mostrarFormulario = !this.mostrarFormulario
    if (this.editMode) {
      if (this.selectedUserId) {
        usuario.id = this.selectedUserId; // Asignar el ID del usuario al objeto usuario
        this.usuariosService.updateUser(usuario).subscribe(updatedUser => {
          // Realizar cualquier acción adicional después de editar el usuario
          this.editMode = false;
          this.fetchData();
        });
      } else {
        console.error("El ID del usuario es indefinido.");
      }
    } else {
      this.usuariosService.addUser(usuario).subscribe(newUser => {
        // Realizar cualquier acción adicional después de agregar el usuario
        this.fetchData();
      });
    }
  }

  mostrarForm(){!this.mostrarFormulario};
  ocultarForm() {
    setTimeout(() => {
      this.mostrarFormulario = false;
    }, 300);
  }
}