from procesos.planificador import Planificador
from procesos.proceso import Proceso
from interfaz.panel import mostrar_estado

def crear_procesos():
    return [Proceso(1, 5), Proceso(2, 3)]

if __name__ == "__main__":
    # 🟢 Simulación Round Robin
    print("\n--- 🟢 Simulación Round Robin ---\n")
    procesos_rr = crear_procesos()
    planificador_rr = Planificador(quantum=2)
    for p in procesos_rr:
        planificador_rr.agregar_proceso(p)
    planificador_rr.ejecutar_round_robin()
    mostrar_estado(procesos_rr)

    # 🔵 Simulación FCFS
    print("\n--- 🔵 Simulación FCFS ---\n")
    procesos_fcfs = crear_procesos()
    planificador_fcfs = Planificador(quantum=2)  # Quantum no se usa en FCFS
    for p in procesos_fcfs:
        planificador_fcfs.agregar_proceso(p)
    planificador_fcfs.ejecutar_fcfs()
    mostrar_estado(procesos_fcfs)