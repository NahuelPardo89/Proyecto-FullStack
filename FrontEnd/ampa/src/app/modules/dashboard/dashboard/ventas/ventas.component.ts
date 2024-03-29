import { Component, OnInit} from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Producto } from 'src/app/modules/productos/interfaces/producto.interface';
import { Categoria } from 'src/app/modules/productos/interfaces/categoria.interface';
import { ProductosService } from 'src/app/modules/dashboard/services/productos.service';

@Component({
  selector: 'app-ventas',
  templateUrl: './ventas.component.html',
  styleUrls: ['./ventas.component.css']
})
export class VentasComponent implements OnInit {
  productos: Producto[] = [];
  categorias: Categoria[] = [];
  editing: boolean = false;
  editingProductoId: number | null = null;
  editingCategoriaId: number | null = null;
  productoForm: FormGroup;
  categoriaForm: FormGroup;
  mostrarFormulario = false;
  mostrarFormCategorias = false;
  imagenSeleccionada: File | null = null;
  
  constructor(private productosService: ProductosService, private fb: FormBuilder) {
    this.productoForm = this.fb.group({
      nombre: ['', Validators.required],
      marca: ['', Validators.required],
      descripcion: ['', Validators.required],
      precio: [, Validators.required],
      stock: [, Validators.required],
      categoria: [, Validators.required],
      
      // Añade los otros campos aquí.
    });

    this.categoriaForm = this.fb.group({
      nombre: ['', Validators.required],
    });
  }

  ngOnInit(): void {
    this.fetchData();
  }

  fetchData(): void {
    this.productosService.getProductos().subscribe(data => {
      this.productos = data;
    });

    this.productosService.getCategorias().subscribe(data => {
      this.categorias = data;
    });
  }

  agregarProducto(): void {
    if (this.editing) {
      const productoToUpdate: Producto = { ...this.productoForm.value, id: this.editingProductoId };
      this.productosService.updateProducto(productoToUpdate).subscribe(updatedProducto => {
        const index = this.productos.findIndex(p => p.id === updatedProducto.id);
        this.productos[index] = updatedProducto;
        this.productoForm.reset();
        this.editing = false;
        this.editingProductoId = null;
        this.mostrarFormulario = true;
      });
    } else {
      this.mostrarFormulario = true;
      const nuevoProducto: Producto = this.productoForm.value;
      this.productosService.addProducto(nuevoProducto).subscribe(producto => {
        this.productos.push(producto);
        this.productoForm.reset();
      });
    }
  }

  editarProducto(producto: Producto): void {
    this.editing = true;
    this.editingProductoId = producto.id;
    this.productoForm.patchValue(producto);
    this.mostrarFormulario = true;
  }

  borrarProducto(producto: Producto): void {
    this.productosService.deleteProducto(producto.id).subscribe(() => {
      const index = this.productos.findIndex(p => p.id === producto.id);
      this.productos.splice(index, 1);
    });
  }

  agregarCategoria(): void {
    if (this.editing) {
      const categoriaToUpdate: Categoria = { ...this.categoriaForm.value, id: this.editingCategoriaId };
      this.productosService.updateCategoria(categoriaToUpdate).subscribe(updatedCategoria => {
        const index = this.categorias.findIndex(c => c.id === updatedCategoria.id);
        this.categorias[index] = updatedCategoria;
        this.categoriaForm.reset();
        this.editing = false;
        this.editingCategoriaId = null;
      });
    } else {
      this.mostrarFormCategorias = true;
      const nuevaCategoria: Categoria = this.categoriaForm.value;
      this.productosService.addCategoria(nuevaCategoria).subscribe(categoria => {
        this.categorias.push(categoria);
        this.categoriaForm.reset();
      });
    }
  }

  editarCategoria(categoria: Categoria): void {
    this.categoriaForm.patchValue(categoria);
    this.editing = true;
    this.editingCategoriaId = categoria.id;
  }

  borrarCategoria(categoria: Categoria): void {
    this.productosService.deleteCategoria(categoria.id).subscribe(() => {
      const index = this.categorias.findIndex(c => c.id === categoria.id);
      this.categorias.splice(index, 1);
    });
  }

  ocultarForm() {
    setTimeout(() => {
      this.mostrarFormulario = false;
    }, 300);
  }

  ocultarCategoria() {
    setTimeout(() => {
      this.mostrarFormCategorias = false;
    }, 100);
  }

  cancelarEdicion(): void {
    this.editing = false;
    this.editingProductoId = null;
    this.editingCategoriaId = null;
    this.productoForm.reset();
    this.categoriaForm.reset();
    this.mostrarFormulario = false;
    this.mostrarFormCategorias = false;
  }

  
  
  
}
