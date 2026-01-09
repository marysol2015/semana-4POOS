class ServicioVenta:
    @staticmethod
    def procesar_pedido(producto):
        print(f"--- Realizando venta de: {producto.modelo} ---")
        precio = producto.calcular_precio_total()
        
        if producto.disponible:
            return f"Venta exitosa. Total a cobrar: ${precio}"
        else:
            return "Error: No hay stock suficiente."
        