import { Component, ViewChild } from '@angular/core';
import { carrito } from './interfaces/carrito';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { CarritoService } from './services/carrito.service';
import { MatSnackBar } from '@angular/material/snack-bar';

 



@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent {
  
  listaProductos: carrito[] = [];
  displayedColumns: string[] = ['id', 'producto', 'cantidad', 'precio', 'acciones'];
  dataSource!: MatTableDataSource<any>;
  
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;
  
  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }
  

  constructor(private _carritoService: CarritoService, private _snackBar: MatSnackBar) {
  }

//se inicializa el metodo al cargar la pagina
ngOnInit(): void {
  this.cargarProductos();
}
//metodo para cargar productos el el template cuando carga
cargarProductos(){
  this.listaProductos = this._carritoService.getProducto();
  this.dataSource = new MatTableDataSource(this.listaProductos)
}


//Metodo para eliminar producto (por ahora es un index pero luego deber cambiar por ID que es el id de producto de la BD - cambiar tambien en el html)
eliminarProducto(index: number){
  console.log(index);
  this._carritoService.eliminarProducto(index);
  this.cargarProductos();
  //mensajito de eliminacion
  this._snackBar.open('El producto fue eliminado de su carrito','',{
    duration: 2000,
    horizontalPosition: 'center',
    verticalPosition: 'bottom'
  })
}



}
