from cpu.cpu import CPU
from interfaz.menu import Menu

def main():  
    cpu = CPU()
    cpu.leer_fichero("archivos_auxiliares/instrucciones.txt")
    #menu = Menu(cpu.unidad_procesamiento.registros, cpu.unidad_control.segmentacion)
    cpu.empezar_segmentacion()    

    
if __name__ == "__main__":
    main()