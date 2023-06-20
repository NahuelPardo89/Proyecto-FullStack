import { Component } from '@angular/core';
import { Carrito2Service } from '../carrito2/carrito2.service';
import { PagosService } from '../../services/pagos.service';




@Component({
  selector: 'app-pasarela-pagos',
  templateUrl: './pasarela-pagos.component.html',
  styleUrls: ['./pasarela-pagos.component.css']
})
export class PasarelaPagosComponent {
  carrito: any = null;

  constructor(private carritoService: Carrito2Service,private pagos:PagosService) { }

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
    
  }
  
    //function to close dialog
    cerrarDialog(){
    
    }

    
  
}
