from procesos.planificador import Planificador
from procesos.proceso import Proceso
from interfaz.panel import mostrar_estado

if __name__ == "__main__":
    p1 = Proceso(1, 5)
    p2 = Proceso(2, 3)

    planificador = Planificador(quantum=2)
    planificador.agregar_proceso(p1)
    planificador.agregar_proceso(p2)
    planificador.ejecutar_round_robin()

    mostrar_estado([p1, p2])