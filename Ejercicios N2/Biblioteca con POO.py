class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.prestados = set()

    def agregar_libro(self, titulo):
        self.libros[titulo] = True

    def eliminar_libro(self, titulo):
        if titulo in self.libros:
            del self.libros[titulo]
            if titulo in self.prestados:
                self.prestados.remove(titulo)

    def prestar_libro(self, titulo):
        if titulo in self.libros and titulo not in self.prestados:
            self.prestados.add(titulo)

    def devolver_libro(self, titulo):
        if titulo in self.prestados:
            self.prestados.remove(titulo)

# Ejemplo de uso:
biblioteca = Biblioteca()
biblioteca.agregar_libro("Python 101")
biblioteca.agregar_libro("Algoritmos Avanzados")
biblioteca.prestar_libro("Python 101")
biblioteca.devolver_libro("Python 101")
