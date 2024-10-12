from fases._if import IF
from fases.ex import EX
from fases.id import ID
from fases.mem import MEM
from fases.wb import WB
from instrucciones.instruccion_aritmetico_logica import InstruccionAritmeticaLogica
from instrucciones.intruccion_memoria import InstruccionMemoria
from registros_acoplamiento_segmentacion.ex_mem import EX_MEM
from registros_acoplamiento_segmentacion.registro_acoplamiento import RegistroAcoplamiento


class Segmentacion:
    def __init__(self, unidad_procesamiento):
        self.if_id = None
        self.id_ex = None
        self.ex_mem = None
        self.mem_wb = None
        self.unidad_procesamiento = unidad_procesamiento
        self._if = IF(self.unidad_procesamiento.pc, self.unidad_procesamiento.memoria_instrucciones)
        self.id = ID(self.unidad_procesamiento.registros, self.unidad_procesamiento.memoria_instrucciones)
        self.ex = EX(self.unidad_procesamiento.alu)
        self.mem = MEM(self.unidad_procesamiento.memoria_datos)
        self.wb = WB(self.unidad_procesamiento.registros)

    def empezar_segmentacion(self):
        i = 0
        while(True):
            i+=1
            print("Estas en el paso: "+ str(i) + " con pc: " + str(self.unidad_procesamiento.pc.valor))
            self.wb.ejecutar(self.mem_wb)
            ex_aux = self.ex.ejecutar(self.id_ex)
            self.mem_wb = self.mem.ejecutar(self.ex_mem)
            self.ex_mem = ex_aux
            if isinstance(self.ex_mem,dict):
                if self.ex_mem['salto'] == True:
                    self.id_ex = None
                    self.unidad_procesamiento.pc.cambiar_pc(self.ex_mem['direccion'])
            else:
                self.id_ex = self.id.ejecutar(self.if_id)
            
            if(self.check_raw()):
                self.id_ex = None
            else:
                self.if_id = self._if.ejecutar()

            self.imprimir_fases()
            
            if self.if_id is None and self.id_ex is None and self.ex_mem is None and self.mem_wb is None:
                break

        self.unidad_procesamiento.registros.mostrar_registros()
        self.unidad_procesamiento.memoria_datos.mostrar_variables()

    def check_raw(self):
        if self.id_ex is not None:
            if self.ex_mem is not None:
                if self.ex_mem.operacion.esta_registro_en_destino(self.id_ex.valor.registros_operandos()):
                    return True
            if self.mem_wb is not None:
                if self.mem_wb.operacion.esta_registro_en_destino(self.id_ex.valor.registros_operandos()):
                    return True
        return False

    def imprimir_fases(self):
        if not self.ex_mem:
            print("Salida ALU: None")
        else:
            if isinstance(self.ex_mem,dict):
                print("Salida ALU(salto) a: ", str(self.ex_mem['direccion']))
            else:
                print("Salida ALU: "+ str(self.ex_mem.valor))

        if self.mem_wb is not None:
           print("Salida Memoria Datos: " + str(self.mem_wb.valor))

        if self.id_ex is None:
            print("No transformamos nada")
        else:
            print("Transformamos: " + str(self.id_ex.valor.imprimir()))
                

        if self.if_id is not None: 
            print("Leemos: " + str(self.if_id.valor))

        print("\n")
