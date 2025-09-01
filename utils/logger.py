def log_event(mensaje):
    with open("log.txt", "a") as f:
        f.write(mensaje + "\n")