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

    def dividir_contenido_archivo(self,datos):
        datos_memoria = datos.split('.text',1)[0]
        instrucciones = datos.split('.text',1)[1]
        self.cargar_memoria_datos(datos_memoria)
        self.cargar_memoria_instrucciones(instrucciones)


    def cargar_memoria_datos(self,datos):
        self.memoria_datos.cargar_datos(datos)

    def cargar_memoria_instrucciones(self,instrucciones):
        self.memoria_instrucciones.cargar_datos(instrucciones)
