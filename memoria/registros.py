from memoria.memoria import Memoria


class Registros(Memoria):
    def __init__(self):
        super().__init__()
        self.inicializar()

    def inicializar(self):
        self.elementos = {
            '$s1' : 0,
            '$s2' : 0,
            '$s3' : 0,
            '$s4' : 0,
            '$s5' : 0,
            '$s6' : 0,
            '$s7' : 0,
            '$t0' : 0,
            '$t1' : 0,
            '$t2' : 0,
            '$t3' : 0,
            '$t4' : 0,
            '$t5' : 0,
            '$t6' : 0,
            '$t7' : 0,
            '$t8' : 0,
            '$t9' : 0
        }

    def procesar_registros(self, direcciones):
        direcciones[1] = self.elementos[direcciones[1]]
        direcciones[2] = self.elementos[direcciones[2]]
        return direcciones
    
    def devolver_registro(self, registro):
        return self.elementos[registro]
    
    def cargar_dato(self, direccion_memoria, dato):
        self.elementos[direccion_memoria] = int(dato)

    def mostrar_registros(self):
        for elem in self.elementos:
            print(str(elem) + " -> "+ str(self.elementos[elem]))