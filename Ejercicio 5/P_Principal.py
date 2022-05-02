from ManejadorPlanAhorro import Manejador
from ClaseMenu import Menu

if __name__ ==  '__main__':
    
    manejador = Manejador()
    manejador.testArchivo()
    
    menu = Menu()
    salir = False
    while not salir:
        print('\n______________ Menu ______________\n')
        print('[1]   Actualizar el valor del vehículo de cada plan')
        print('[2]   Dado un valor, mostrar datos de plan')
        print('[3]   Mostrar el monto que se debe haber pagado para licitar el vehículo')
        print('[4]   Código de plan y modificar cantidad de cuotas que debe tener pagas para licitar')
        print('[5]   Salir')
        print()
        op = input('Seleccione una opcion: ')
        menu.opcion(op, manejador)
        salir = op == '5'