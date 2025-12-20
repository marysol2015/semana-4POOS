from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca 

def main():
    biblioteca = Biblioteca()

    # Crear algunos libros
    libro1 = Libro("Clean Code", "George Orwell", "111")
    Usuario1 = Usuario("Alice", "01826232")
    biblioteca.agregar_libro(libro1)

    print(biblioteca.prestar("111", Usuario1))  # Prestar libro existente
    print(biblioteca.prestar("111", Usuario1))  # Intentar prestar el mismo libro nuevamente

if __name__ == "__main__":
    main()