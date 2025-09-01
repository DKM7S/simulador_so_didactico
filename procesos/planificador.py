class Planificador:
    def __init__(self, quantum):
        self.cola = []
        self.quantum = quantum

    def agregar_proceso(self, proceso):
        self.cola.append(proceso)

    def ejecutar(self):
        while self.cola:
            actual = self.cola.pop(0)
            print(f"Ejecutando PID {actual.pid}")
            actual.tiempo -= self.quantum
            if actual.tiempo > 0:
                self.cola.append(actual)
            else:
                actual.estado = "Terminado"