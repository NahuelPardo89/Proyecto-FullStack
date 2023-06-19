import { Component } from '@angular/core';
import { FacturaService } from './factura.service';

@Component({
  selector: 'app-factura',
  templateUrl: './factura.component.html',
  styleUrls: ['./factura.component.css']
})
export class FacturaComponent {
  facturas: any[];
  constructor(private facturaService: FacturaService){
    this.facturas = [];
  }
  ngOnInit() {
    this.facturaService.getFacturas()
      .subscribe(data => {
        this.facturas = data;
        
        
      });
  }
}
