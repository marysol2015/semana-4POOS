from modelos.libro import Libro
from modelos.usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)

    def prestar(self, isbn, usuario: Usuario):
        for libro in self.libros:
            if libro.isbn == isbn:
                if libro.prestar():
                    return f"Libro prestado a {usuario.nombre}."
                return "El libro ya está préstado."
        return "Libro no encontrado." 