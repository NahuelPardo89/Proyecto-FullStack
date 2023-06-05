import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Usuario } from 'src/app/modules/productos/interfaces/usuario.interface';
import { UsuariosService } from '../../usuarios.service';

@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.css']
})
export class ClientesComponent implements OnInit {
  
  usuarios: Usuario[] = [];
  usuarioForm: FormGroup;
  mostrarFormulario = false;

  constructor(private usuariosService: UsuariosService, private fb: FormBuilder) {
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

  editarUsuario(usuario: Usuario): void {
    this.usuarioForm.patchValue(usuario);
    this.mostrarFormulario = true;
  }

  borrarUsuario(usuario: Usuario): void {
    this.usuariosService.deleteUser(usuario.id).subscribe(() => {
      const index = this.usuarios.findIndex(u => u.id === usuario.id);
      this.usuarios.splice(index, 1);
      // Obtener la lista actualizada de usuarios
      this.fetchData();
    });
  }

  ocultarForm() {
    setTimeout(() => {
      this.mostrarFormulario = false;
    }, 300);
  }
}