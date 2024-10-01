from instrucciones.instruccion_aritmetico_logica import InstruccionAritmeticaLogica
from instrucciones.instruccion_salto import InstruccionSalto
from instrucciones.intruccion_memoria import InstruccionMemoria


class ID:
    def __init__(self):
        pass


    def identificar_etiquetas(self, linea, pc_actual):
        if(self.is_etiqueta(linea)):
            self.crear_etiqueta(linea, pc_actual)
        else:
            self.crear_instruccion(linea, pc_actual)
    
    def crear_instruccion(self, linea, pc_actual):
        nombre_instruccion, operandos = self.dividir_linea(linea)

        if nombre_instruccion in ['add', 'sub', 'mul', 'div', 'and', 'or', 'xor', 'nor']:
            elemento = InstruccionAritmeticaLogica(nombre_instruccion, operandos)
        elif nombre_instruccion in ['bne', 'beq']:
            elemento = InstruccionSalto(nombre_instruccion,operandos)
        elif nombre_instruccion == 'j':
            elemento = InstruccionSalto(nombre_instruccion, operandos)
        elif nombre_instruccion in ['sw', 'sb', 'lb', 'lw']:
            elemento = InstruccionMemoria(nombre_instruccion, operandos)

        self.elementos[pc_actual] = elemento


    def dividir_linea(self, texto):
        tokens = texto.split()
        nombre_instruccion = tokens.pop(0)
        operandos = tokens
        return nombre_instruccion, operandos
    
