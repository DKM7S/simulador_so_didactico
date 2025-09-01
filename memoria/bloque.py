class Bloque:
    def __init__(self, inicio, tamaño):
        self.inicio = inicio            # Dirección inicial del bloque en memoria
        self.tamaño = tamaño            # Tamaño del bloque (en bytes o unidades)
        self.ocupado = False            # Estado del bloque
        self.pagina_asignada = None     # ID de la página asignada (si existe)

    def asignar_pagina(self, id_pagina):
        """Asigna una página al bloque."""
        self.ocupado = True
        self.pagina_asignada = id_pagina

    def liberar(self):
        """Libera el bloque de memoria."""
        self.ocupado = False
        self.pagina_asignada = None

    def __repr__(self):
        estado = "Ocupado" if self.ocupado else "Libre"
        pagina = f"Página {self.pagina_asignada}" if self.pagina_asignada is not None else "Sin asignar"
        return f"[Bloque desde {self.inicio} tamaño {self.tamaño}] → {estado}, {pagina}"