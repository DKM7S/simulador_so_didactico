class Proceso:
    def __init__(self, pid, tiempo_ejecucion):
        self.pid = pid
        self.tiempo = tiempo_ejecucion
        self.estado = "Listo"