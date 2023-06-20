export interface Producto {
    id: number;
    nombre: string;
    marca: string;
    descripcion: string;
    precio: number;
    stock: number;
    foto: string | null;  // Ajustado para permitir null
    categoria: number;  // Ajustado para ser solo un ID de número, no un objeto de Categoria
    estaEnCarrito?: boolean;
  }