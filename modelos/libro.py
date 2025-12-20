class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def prestar(self):
        if self.prestado:
            return False
        self.prestado = True
        return True
    
    def devolver(self):
        if not self.prestado:
            return False
        self.prestado = False
        return True
    
    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Libro({self.titulo}, {estado})"