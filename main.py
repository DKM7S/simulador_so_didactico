from memoria.gestor_memoria import GestorMemoria
from procesos.planificador import Planificador
from procesos.proceso import Proceso
from interfaz.panel import mostrar_estado

# 🔧 Crear procesos con parámetros definidos
def crear_procesos():
    return [Proceso(1, 5, 4), Proceso(2, 3, 2)]

# 🟢 Simulación Round Robin
def ejecutar_round_robin():
    print("\n--- 🟢 Simulación Round Robin ---\n")
    gestor_memoria_rr = GestorMemoria(tamaño_total=400, tamaño_bloque=100)
    procesos_rr = crear_procesos()
    planificador_rr = Planificador(quantum=2)

    for p in procesos_rr:
        planificador_rr.agregar_proceso(p)
        gestor_memoria_rr.asignar({"id": f"P{p.pid}", "num_paginas": p.paginas})

    planificador_rr.ejecutar_round_robin()
    mostrar_estado(procesos_rr)
    gestor_memoria_rr.mostrar_tabla_paginas()
    gestor_memoria_rr.visualizar_ascii()

# 🔵 Simulación FCFS
def ejecutar_fcfs():
    print("\n--- 🔵 Simulación FCFS ---\n")
    gestor_memoria_fcfs = GestorMemoria(tamaño_total=400, tamaño_bloque=100)
    procesos_fcfs = crear_procesos()
    planificador_fcfs = Planificador(quantum=2)  # Quantum no se usa en FCFS

    for p in procesos_fcfs:
        planificador_fcfs.agregar_proceso(p)
        gestor_memoria_fcfs.asignar({"id": f"P{p.pid}_FCFS", "num_paginas": p.paginas})

    planificador_fcfs.ejecutar_fcfs()
    mostrar_estado(procesos_fcfs)
    gestor_memoria_fcfs.mostrar_tabla_paginas()
    gestor_memoria_fcfs.visualizar_ascii()

# 🧠 Menú interactivo CLI – Semana 6
def mostrar_menu():
    print("\n Simulador de Planificación y Memoria")
    print("1. Ejecutar Round Robin")
    print("2. Ejecutar FCFS")
    print("3. Salir")

def ejecutar_simulacion(opcion):
    if opcion == "1":
        ejecutar_round_robin()
    elif opcion == "2":
        ejecutar_fcfs()
    elif opcion == "3":
        print("👋 Simulador finalizado.")
        exit()
    else:
        print("❌ Opción inválida. Intenta de nuevo.")

# 🚀 Bucle principal
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        ejecutar_simulacion(opcion)