# Simulador SO Didáctico

Este proyecto simula componentes clave de un sistema operativo:

- 📋 Planificación de procesos (Round Robin)
- 🧠 Gestión de memoria (bloques simulados)
- 📁 Sistema de archivos (creación y escritura)
- 🖥️ Interfaz CLI con `rich`

## Estructura

Semana 1: Estructura base del simulador
🎯 Objetivo
Diseñar la arquitectura modular del simulador y definir los componentes principales.
📁 Módulos creados
- procesos: gestión de procesos y planificación
- memoria: simulación de bloques y asignación
- archivos: manejo de archivos simulados
- interfaz: salida visual y panel de control
- utils: utilidades como logger y helpers
📄 Archivos clave
- proceso.py: clase base de procesos
- bloque.py: clase de memoria
- archivo.py: clase de archivo
- logger.py: registro de eventos

Semana 2: Simulación de procesos y memoria
🎯 Objetivo
Implementar clases funcionales para procesos y bloques de memoria, con atributos y estados.
🧩 Implementaciones
- Proceso: PID, tiempo de ejecución, estado (Listo, Ejecutando, Terminado)
- Bloque: ID, tamaño, estado (Libre, Ocupado)
- GestorMemoria: asignación y liberación de bloques
- GestorArchivos: creación y lectura de archivos simulados
🧪 Pruebas realizadas
- Creación de procesos desde main.py
- Asignación de bloques de memoria
- Visualización de estados en consola

Semana 3: Planificación de procesos
🎯 Objetivo
Implementar algoritmos de planificación: FCFS y Round Robin.
🧠 Algoritmos
🔵 FCFS (First-Come, First-Served)
Ejecuta procesos en orden de llegada, sin interrupciones.

def ejecutar_fcfs(self):
    while self.cola:
        actual = self.cola.pop(0)
        actual.estado = "Ejecutando"
        print(f"{actual.pid} → Estado: {actual.estado} | Ejecutando {actual.tiempo} unidades")
        actual.estado = "Terminado"
        print(f"{actual.pid} → Estado: {actual.estado}")


🟢 Round Robin
Ejecuta procesos por bloques de tiempo (quantum). Si no terminan, se reencolan.
def ejecutar_round_robin(self):
    while self.cola:
        actual = self.cola.pop(0)
        actual.estado = "Ejecutando"
        tiempo_ejecucion = min(actual.tiempo, self.quantum)
        print(f"{actual.pid} → Estado: {actual.estado} | Ejecutando {tiempo_ejecucion} unidades")
        actual.tiempo -= self.quantum
        if actual.tiempo > 0:
            actual.estado = "Listo"
            self.cola.append(actual)
        else:
            actual.estado = "Terminado"

 Simulación desde main.py
 p1 = Proceso(1, 5)
p2 = Proceso(2, 3)
planificador = Planificador(quantum=2)
planificador.agregar_proceso(p1)
planificador.agregar_proceso(p2)
planificador.ejecutar_round_robin()

 Estado final
 PID 1 - Estado: Terminado
PID 2 - Estado: Terminado

✅ Resultado
Round Robin funcional con cambio de estado. FCFS listo para integrar. Visualización clara en consola.

semana 4

# 🧠 Módulo de Memoria con Paginación – Semana 4

Este módulo simula la gestión de memoria por paginación en un sistema operativo didáctico. Se integra con el planificador de procesos y permite visualizar cómo se asignan las páginas a bloques físicos.

## 📦 Estructura


## ⚙️ Clases principales

### `Bloque`
Representa un marco de memoria:
- `inicio`: dirección inicial
- `tamaño`: tamaño del bloque
- `ocupado`: estado del bloque
- `pagina_asignada`: ID de la página asignada

### `GestorMemoria`
Gestiona la asignación de páginas:
- `asignar(proceso)`: asigna páginas del proceso a bloques libres
- `mostrar_tabla_paginas()`: muestra la tabla de páginas
- `visualizar_ascii()`: muestra el estado de los bloques

## 🧪 Ejemplo de uso

```python
gestor = GestorMemoria(tamaño_total=400, tamaño_bloque=100)

proceso1 = {"id": "P1", "num_paginas": 3}
gestor.asignar(proceso1)

gestor.mostrar_tabla_paginas()
gestor.visualizar_ascii()
Integración con planificación

El módulo se conecta con el planificador (Round Robin y FCFS) para asignar memoria a cada proceso al momento de su creación.

