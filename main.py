from modelo.producto import Laptop
from servicios.tienda import ServicioVenta

def ejecutar():
    # Creamos el objeto
    mi_equipo = Laptop("Lenovo Legion 7i", 10, 1300.90, 16)
    
    # Usamos el servicio para procesar
    resultado = ServicioVenta.procesar_pedido(mi_equipo)
    
    print(resultado)

if __name__ == "__main__":
    ejecutar()