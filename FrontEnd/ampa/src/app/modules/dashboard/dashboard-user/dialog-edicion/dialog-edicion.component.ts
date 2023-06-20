import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Usuario } from 'src/app/modules/productos/interfaces/usuario.interface';
import { UsuariosService } from '../../services/usuarios.service';
import { AuthService } from 'src/app/modules/auth/services/auth.service';
import { User } from 'src/app/modules/auth/interfaces/user.interface';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-dialog-edicion',
  templateUrl: './dialog-edicion.component.html',
  styleUrls: ['./dialog-edicion.component.css']
})
export class DialogEdicionComponent implements OnInit {
  
  loggedInUser: User | null = null;
  usuarioForm: FormGroup;
  datosUser: User | null = null;

  constructor(private dialogRef: MatDialogRef<DialogEdicionComponent>,
    private usuariosService: UsuariosService, 
    private fb: FormBuilder, 
    private authService: AuthService,
    ){
    
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
  resetForm() {
    if (this.loggedInUser) {
      this.usuarioForm.patchValue({
        dni: this.loggedInUser.dni,
        nombre: this.loggedInUser.nombre,
        apellido: this.loggedInUser.apellido,
        email: this.loggedInUser.email,
        telefono: this.loggedInUser.telefono,
        direccion: this.loggedInUser.direccion,
        is_staff: this.loggedInUser.is_staff
      });
    }
  }
  
  
  editarDatos() {
    if (this.usuarioForm.invalid || !this.loggedInUser) {
      return;
    }
  
    const updatedUser: Usuario = {
      id: this.loggedInUser.id,
      ...this.usuarioForm.value
    };
  
    this.usuariosService.updateUser(updatedUser).subscribe(
      (response) => {
        console.log('Usuario actualizado:', response);
        // Realiza las acciones necesarias después de la actualización exitosa
      },
      (error) => {
        console.error('Error al actualizar el usuario:', error);
        // Maneja el error de actualización
      }
    );
    this.dialogRef.close();
  }
    
  
  
  
  ngOnInit(): void {
    this.authService.currentUser.subscribe((user) => {
      this.loggedInUser = user;
      
      if (user) {
        
        this.resetForm(); // Restablece los valores del formulario al abrir el diálogo
      }
    });
    
  }
}
