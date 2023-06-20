import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-compra-exitosa',
  templateUrl: './compra-exitosa.component.html',
  styleUrls: ['./compra-exitosa.component.css']
})
export class CompraExitosaComponent {
  constructor(private router: Router, public dialogRef: MatDialogRef<CompraExitosaComponent>) { }
  finalizarCompra(){
    this.router.navigateByUrl('dashboard');
    this.dialogRef.close();
  }

}
