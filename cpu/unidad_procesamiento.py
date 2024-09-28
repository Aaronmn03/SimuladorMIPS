from alu.alu import ALU
from memoria.memoria_datos import MemoriaDatos
from memoria.memoria_instrucciones import MemoriaInstrucciones
from memoria.registros import Registros
from pc.pc import PC


class UnidadProcesamiento:
    def __init__(self):
        self.pc = PC()
        self.memoria_instrucciones = MemoriaInstrucciones()
        self.memoria_datos = MemoriaDatos()
        self.registros = Registros()
        self.alu = ALU()
        print("Se ha creado la Unidad de procesamiento")

    def cargar_memoria_datos(self,datos):
        self.memoria_datos.cargar_datos(datos)
        self.memoria_datos.mostrar_variables()