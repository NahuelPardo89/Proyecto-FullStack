export interface Producto {
    id: number;
    nombre: string;
    marca: string;
    descripcion: string;
    precio: number;
    stock: number;
    foto: string | null;  
    categoria: number;  
    estaEnCarrito?: boolean;
  }