class Planificador:
    def __init__(self, quantum):
        self.cola = []
        self.quantum = quantum

    def agregar_proceso(self, proceso):
        self.cola.append(proceso)

    def ejecutar_round_robin(self):
        print("🟢 Algoritmo Round Robin:")
        while self.cola:
            actual = self.cola.pop(0)
            actual.estado = "Ejecutando"
            tiempo_ejecucion = min(actual.tiempo, self.quantum)
            print(f"{actual.pid} → Estado: {actual.estado} | Ejecutando {tiempo_ejecucion} unidades")
            actual.tiempo -= self.quantum
            if actual.tiempo > 0:
                actual.estado = "Listo"
                print(f"{actual.pid} → Estado: {actual.estado} | Tiempo restante: {actual.tiempo}")
                self.cola.append(actual)
            else:
                actual.estado = "Terminado"
                print(f"{actual.pid} → Estado: {actual.estado}")

    def ejecutar_fcfs(self):
        print("🔵 Algoritmo FCFS:")
        while self.cola:
            actual = self.cola.pop(0)
            actual.estado = "Ejecutando"
            print(f"{actual.pid} → Estado: {actual.estado} | Ejecutando {actual.tiempo} unidades")
            actual.estado = "Terminado"
            print(f"{actual.pid} → Estado: {actual.estado}")