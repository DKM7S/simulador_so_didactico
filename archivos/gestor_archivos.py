from archivos.archivo import Archivo

class GestorArchivos:
    def __init__(self):
        self.archivos = {}  # Diccionario que simula el sistema de archivos plano

    def crear(self, nombre, contenido=""):
        if nombre not in self.archivos:
            self.archivos[nombre] = Archivo(nombre, contenido)
            print(f"✅ Archivo '{nombre}' creado")
        else:
            print(f"⚠️ El archivo '{nombre}' ya existe")

    def escribir(self, nombre, texto):
        if nombre in self.archivos:
            archivo = self.archivos[nombre]
            archivo.escribir(archivo.contenido + texto)
            print(f"✍️ Se escribió en '{nombre}'")
        else:
            print(f"❌ El archivo '{nombre}' no existe")

    def leer(self, nombre):
        if nombre in self.archivos:
            contenido = self.archivos[nombre].leer()
            print(f"📄 Contenido de '{nombre}': {contenido}")
        else:
            print(f"❌ El archivo '{nombre}' no existe")