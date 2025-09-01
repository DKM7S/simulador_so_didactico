class Archivo:
    def __init__(self, nombre, contenido=""):
        self.nombre = nombre
        self.tipo = "archivo"              # Identifica el tipo dentro del sistema
        self.contenido = contenido
        self.tamaño = len(contenido)       # Calcula el tamaño automáticamente

    def leer(self):
        return self.contenido

    def escribir(self, nuevo_contenido):
        self.contenido = nuevo_contenido
        self.tamaño = len(nuevo_contenido)