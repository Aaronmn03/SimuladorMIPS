from instrucciones.instruccion_aritmetico_logica import InstruccionAritmeticaLogica
from instrucciones.instruccion_salto import InstruccionSalto
from instrucciones.intruccion_memoria import InstruccionMemoria
from memoria.memoria import Memoria


class MemoriaInstrucciones(Memoria):
    def __init__(self):
        super().__init__()
        self.etiquetas = dict()
        print("de instrucciones")

    def cargar_datos(self,datos):
        lineas = datos.splitlines()
        lineas_filtradas = [linea for linea in lineas if linea.strip() != '']
        for indice, linea in enumerate(lineas_filtradas):
            linea_aux = linea.strip()
            pc_actual = (indice - len(self.etiquetas) + 1) * 4
            self.identificar_etiquetas(linea_aux,pc_actual)
        self.mostrar_instrucciones()
        self.mostrar_etiquetas()

    def is_etiqueta(self, linea):
        if ':' in linea:
            return True
        return False

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
            elemento = InstruccionSalto(nombre_instruccion, [])
        elif nombre_instruccion in ['sw', 'sb', 'lb', 'lw']:
            elemento = InstruccionMemoria(nombre_instruccion, operandos)

        self.elementos[pc_actual] = elemento


    def crear_etiqueta(self, linea, pc_actual):
        self.etiquetas[linea[:-1]] = pc_actual

    def dividir_linea(self, texto):
        tokens = texto.split()
        nombre_instruccion = tokens.pop(0)
        operandos = tokens
        return nombre_instruccion, operandos
    
    def mostrar_instrucciones(self):
        for instruccion in self.elementos:
            print(str(instruccion) + ' -> ' + str(self.elementos[instruccion].nombre))

    def mostrar_etiquetas(self):
        print(self.etiquetas)
