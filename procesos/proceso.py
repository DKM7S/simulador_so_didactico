class Proceso:
    def __init__(self, pid, tiempo_ejecucion, paginas):
        self.pid = pid
        self.tiempo = tiempo_ejecucion
        self.paginas = paginas
        self.estado = "Listo"
        self.tiempo_restante = tiempo_ejecucion  # Útil para Round Robin