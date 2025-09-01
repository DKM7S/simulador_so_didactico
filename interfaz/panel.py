from rich.console import Console
console = Console()

def mostrar_estado(procesos):
    for p in procesos:
        console.print(f"[bold cyan]PID {p.pid}[/] - Estado: {p.estado}")