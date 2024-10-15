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
        self.fases = [self._if, self.id, self.ex, self.mem, self.wb]
        self.raw = False

    def empezar_segmentacion(self, un_paso):
        ciclo = 0
        while(True):
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

            if self.if_id is None and self.id_ex is None and self.ex_mem is None and self.mem_wb is None:
                return ciclo
            else:
                ciclo+=1

            if un_paso:
                return 1
                break

    def check_raw(self):
        if self.id_ex is not None:
            if self.ex_mem is not None:
                if self.ex_mem.operacion.esta_registro_en_destino(self.id_ex.valor.registros_operandos()):
                    return True
            if self.mem_wb is not None:
                if self.mem_wb.operacion.esta_registro_en_destino(self.id_ex.valor.registros_operandos()):
                    return True
        return False

    def devolver_registro_acoplamiento_string(self, registro_acoplamiento, nombre_registro):
        aux = ""
        if not registro_acoplamiento:
            aux += f"{nombre_registro}: el registro de acoplamiento esta vacio"
        else:
            if isinstance(registro_acoplamiento, dict):
                aux += f"{nombre_registro}" + f"salto a: {registro_acoplamiento['direccion']}"
            else:
                aux += f"{nombre_registro}: " + registro_acoplamiento.devolver_string()

        return aux    