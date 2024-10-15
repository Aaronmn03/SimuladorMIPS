class Instruccion:
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        pass

    def devolver_string(self):
        return self.nombre