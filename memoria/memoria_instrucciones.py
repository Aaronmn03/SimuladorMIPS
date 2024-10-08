from memoria.memoria import Memoria


class MemoriaInstrucciones(Memoria):
    def __init__(self):
        super().__init__()
        self.etiquetas = dict()

    def cargar_datos(self,datos):
        lineas = datos.splitlines()
        lineas_filtradas = [linea for linea in lineas if linea.strip() != '']
        for indice, linea in enumerate(lineas_filtradas):
            linea_aux = linea.strip()
            pc_actual = (indice - len(self.etiquetas)) * 4
            if(self.is_etiqueta(linea_aux, pc_actual) == False):            
                self.elementos[pc_actual] = linea_aux
        #self.mostrar_instrucciones()

    def is_etiqueta(self, linea, pc):
        if ':' in linea:
            self.crear_etiqueta(linea, pc)
            return True
        return False
    
    
    def crear_etiqueta(self, linea, pc_actual):
        self.etiquetas[linea[:-1]] = pc_actual

    def mostrar_instrucciones(self):
        for instruccion in self.elementos:
            print(str(instruccion) + ' -> ' + str(self.elementos[instruccion]))
