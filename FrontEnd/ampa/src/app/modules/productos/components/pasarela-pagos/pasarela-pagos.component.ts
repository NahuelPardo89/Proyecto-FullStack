import { Component } from '@angular/core';
import { Carrito2Service } from '../../services/carrito2.service';
import { PagosService } from '../../services/pagos.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { CompraExitosaComponent } from './compra-exitosa/compra-exitosa.component';





@Component({
  selector: 'app-pasarela-pagos',
  templateUrl: './pasarela-pagos.component.html',
  styleUrls: ['./pasarela-pagos.component.css']
})
export class PasarelaPagosComponent {
  carrito: any = null;
  formulario: FormGroup;


  constructor(private carritoService: Carrito2Service, private pagos: PagosService, private formBuilder: FormBuilder, private dialog: MatDialog) {
    this.formulario = this.formBuilder.group({
      nombre: ['', Validators.required],
      apellido: ['', Validators.required],
      dni: ['', [Validators.required, Validators.pattern(/^\d{7,9}$/)]],
      nombreTitular: ['', Validators.required],
      numeroTarjeta: ['', [Validators.required, Validators.pattern(/^\d{16}$/)]],
      fecha: ['', [Validators.required, Validators.pattern(/^(0[1-9]|1[0-2])\/\d{2}$/)]],
      cvc: ['', [Validators.required, Validators.pattern(/^\d{3}$/)]],
      pais: ['', Validators.required],
      provincia: ['', Validators.required],
      localidad: ['', Validators.required],
      direccion: ['', Validators.required],
      terminos: [false, Validators.requiredTrue]
    });
  }

  ngOnInit(): void {
    const usuarioString = localStorage.getItem('user');
     
    if (usuarioString !== null) {
      const usuario = JSON.parse(usuarioString);
      const usuarioId = usuario.id;
        
      this.carritoService.getCarrito(usuarioId).subscribe(data => {
        this.carrito = data;
        
        for (let detalle of this.carrito.detalles) {
          this.carritoService.getProductoDetails(detalle.producto).subscribe(producto => {
            detalle.producto = producto;
          });
        }
      });
    }
  }
  pagar(){
    
    this.pagos.realizarPago({ usuario: this.carrito.usuario.id}).subscribe(
      res => {
        console.log('Pago realizado:', res);
        
        
        
      },
      err => {
        console.log('Hubo un error al realizar el pago:', err);
      }
      
    );
    if (this.formulario.valid) {
      // Realiza las acciones necesarias para procesar el pago
  
      // Abre el diálogo de compra exitosa
      const dialogRef = this.dialog.open(CompraExitosaComponent, {
        width: '60%',
        disableClose: true, // Impide cerrar el diálogo haciendo clic fuera de él
      });
  
      // Opcional: Realiza acciones adicionales después de que se cierre el diálogo
      dialogRef.afterClosed().subscribe(result => {
        // ...
      });
    } else {
      // El formulario no es válido, realiza acciones adicionales o muestra mensajes de error
    }
  
    
  }
  
    //function to close dialog
    cerrarDialog(){
    
    }

    
  
}
