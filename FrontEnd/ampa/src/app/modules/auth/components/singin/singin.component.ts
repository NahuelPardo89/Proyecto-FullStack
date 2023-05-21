import { Component } from '@angular/core';
import { FormBuilder,  FormGroup,  Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { SinginService } from '../../services/singin.service';

@Component({
  selector: 'app-singin',
  templateUrl: './singin.component.html',
  styleUrls: ['./singin.component.css']
})
export class SinginComponent {
  registroForm:FormGroup;

  constructor(private formBuilder: FormBuilder,private singinService: SinginService,
    private router: Router) {
    this.registroForm = this.formBuilder.group({
    dni:[,[Validators.required,Validators.pattern("^[0-9]*$"),Validators.min(1),Validators.max(999000000)] ],
    nombre:['', [Validators.required,]],
    apellido:['', [Validators.required,]],
    email:['', [Validators.required,Validators.email]],
    telefono:['', [Validators.pattern("^[0-9]*$"),]],
    direccion:['', [Validators.required,]],
    ciudad:['', [Validators.required,Validators.pattern("^[0-9]*$"),]],
    password:['', [Validators.required,Validators.minLength(8)]],
    });
  }
  

  ngOnInit(): void {}

  onSubmit(): void {
    if (this.registroForm.valid) {
      const usuario = this.registroForm.value;
      console.log('Usuario registrado:', usuario);
      this.singinService.registerUser(usuario).subscribe(
        (res) => {
          console.log('Usuario registrado:', res);
          
          this.router.navigate(['/dasboard']);
        },
        (err) => {
          // Trata los errores de la petición aquí
          console.log(err);
        }
      );
    
  }}

  getErrorMessage(fieldName: string): string {
    const field = this.registroForm.get(fieldName);
  
    if (!field) {
      return '';
    }
  
    const errors = field.errors;
  
    if (!errors) {
      return '';
    }
  
    const errorMessages: { [key: string]: string | ((fieldName: string) => string) } = {
      required: 'Este campo es requerido',
      email: 'Por favor, introduce un email válido',
      minlength: 'La contraseña debe tener al menos 8 caracteres',
      pattern: (fieldName: string) => {
        switch (fieldName) {
          case 'telefono':
          case 'ciudad':
            return 'Solo se permiten números';
          case 'dni':
            return 'DNI inválido';
          default:
            return '';
        }
      },
      min: 'DNI inválido',
      max: 'DNI inválido',
    };
  
    for (const errorKey in errors) {
      const errorMessage = errorMessages[errorKey];
      
      if (typeof errorMessage === 'function') {
        return errorMessage(fieldName);
      }
  
      if (errorMessage) {
        return errorMessage;
      }
    }
  
    return '';
  }
  
  
}

  
  

