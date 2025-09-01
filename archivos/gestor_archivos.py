from archivos.archivo import Archivo

class GestorArchivos:
    def __init__(self):
        self.archivos = {}

    def crear(self, nombre):
        self.archivos[nombre] = Archivo(nombre)

    def escribir(self, nombre, texto):
        if nombre in self.archivos:
            self.archivos[nombre].contenido += texto