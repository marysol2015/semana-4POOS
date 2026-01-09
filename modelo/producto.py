from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, modelo: str, stock: int, precio_base: float):
        self.modelo = modelo
        self.stock = stock
        self.__precio_base = precio_base  # Encapsulamiento
        self.disponible = stock > 0

    def get_precio_base(self):
        return self.__precio_base

    @abstractmethod
    def calcular_precio_total(self):
        pass

class Laptop(Producto):
    def __init__(self, modelo, stock, precio_base, ram):
        super().__init__(modelo, stock, precio_base)
        self.ram = ram

    def calcular_precio_total(self):
        # Polimorfismo: Cálculo (IVA 15%)
        return round(self.get_precio_base() * 1.15, 2)