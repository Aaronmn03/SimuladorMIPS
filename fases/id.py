from instrucciones.instruccion_aritmetico_logica import InstruccionAritmeticaLogica
from instrucciones.instruccion_salto import InstruccionSalto
from instrucciones.intruccion_memoria import InstruccionMemoria
from registros_acoplamiento_segmentacion.registro_acoplamiento import RegistroAcoplamiento


class ID:
    def __init__(self, registros):
        self.registros = registros

    def ejecutar(self,linea):
        if(linea is not None):
            return self.crear_instruccion(linea)
        
        
   
    def crear_instruccion(self, registro):
        if registro is not None:
            print(registro)
            nombre_instruccion, operandos = self.dividir_linea(registro.valor)

            if nombre_instruccion in ['add', 'sub', 'mul', 'div', 'and', 'or', 'xor', 'nor']:
                parametros = self.registros.procesar_registros(operandos)
                instruccion = InstruccionAritmeticaLogica(nombre_instruccion, parametros)
            elif nombre_instruccion in ['bne', 'beq']:
                instruccion = InstruccionSalto(nombre_instruccion,operandos)
            elif nombre_instruccion == 'j':
                instruccion = InstruccionSalto(nombre_instruccion, operandos)
            elif nombre_instruccion in ['sw', 'sb', 'lb', 'lw']:
                if nombre_instruccion in ['sw', 'sb']:
                    
                    operandos[0] = self.registros.devolver_registro(operandos[0])
                instruccion = InstruccionMemoria(nombre_instruccion, operandos)
            return RegistroAcoplamiento(instruccion)
        return None


    def dividir_linea(self, texto):
        tokens = texto.split()
        nombre_instruccion = tokens.pop(0)
        operandos = [operando.strip(',') for operando in tokens]
        return nombre_instruccion, operandos
    
