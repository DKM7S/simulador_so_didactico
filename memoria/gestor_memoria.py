from memoria.bloque import Bloque

class GestorMemoria:
    def __init__(self, tamaño_total, tamaño_bloque):
        self.tamaño_total = tamaño_total
        self.tamaño_bloque = tamaño_bloque
        self.bloques = []
        self.tabla_paginas = {}  # proceso_id → {pagina_id: inicio_bloque}
        self._crear_bloques()

    def _crear_bloques(self):
        num_bloques = self.tamaño_total // self.tamaño_bloque
        for i in range(num_bloques):
            inicio = i * self.tamaño_bloque
            bloque = Bloque(inicio, self.tamaño_bloque)
            self.bloques.append(bloque)

    def asignar(self, proceso):
        """Asigna páginas del proceso a bloques libres."""
        id_proceso = proceso["id"]
        num_paginas = proceso["num_paginas"]
        self.tabla_paginas[id_proceso] = {}

        asignadas = 0
        for bloque in self.bloques:
            if not bloque.ocupado and asignadas < num_paginas:
                bloque.asignar_pagina(f"{id_proceso}:{asignadas}")
                self.tabla_paginas[id_proceso][asignadas] = bloque.inicio
                asignadas += 1

        if asignadas < num_paginas:
            print(f"⚠️ Proceso {id_proceso} no pudo asignar todas sus páginas ({asignadas}/{num_paginas})")
        else:
            print(f"✅ Proceso {id_proceso} asignado completamente ({num_paginas} páginas)")

    def mostrar_tabla_paginas(self):
        print("\n📋 Tabla de Páginas:")
        for pid, paginas in self.tabla_paginas.items():
            print(f"Proceso {pid}:")
            for pag, inicio in paginas.items():
                print(f"  Página {pag} → Bloque en {inicio}")

    def visualizar_ascii(self):
        print("\n🧱 Estado de los bloques:")
        for bloque in self.bloques:
            if bloque.ocupado:
                print(f"[{bloque.inicio}] Página {bloque.pagina_asignada}")
            else:
                print(f"[{bloque.inicio}] Libre")