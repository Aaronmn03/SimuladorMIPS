from memoria.memoria import Memoria


class MemoriaDatos(Memoria):
    def __init__(self):
        super().__init__()
        print("de datos")

    def cargar_datos(self,datos):
        variables = datos.split('\n')
        for linea in variables:
            if linea not in ['.data', '']:
                self.dividir_linea(linea.split('    '))

    def dividir_linea(self, texto):
        division_dos_puntos = texto[1].split(': ')
        nombre = division_dos_puntos[0]
        tipo = division_dos_puntos[1].split(' ')[0][1:]
        valor = division_dos_puntos[1].split(' ')[1]
        self.añadir_dato(nombre, tipo, valor)
                
    def añadir_dato(self,nombre_variable, tipo, valor):
        self.elementos[nombre_variable] = {'tipo' : tipo, 'valor' : valor}

    def mostrar_variables(self):
        for variable in self.elementos:
            print(str(variable) + " -> " + str(self.elementos[variable]['valor']))