from ManejadorRegistro import ManejadorRegistro
from ClaseMenu import Menu

if __name__ == '__main__':
    
    manejador = ManejadorRegistro()
    manejador.testArchivo()
    menu = Menu()
    
    salir = False
    while not salir:
        print('\n_________________ Menu _________________\n')
        print('[1]   Mostrar para cada variable el día y hora de menor y mayor valor')
        print('[2]   Indicar la temperatura promedio mensual por cada hora')
        print('[3]   Ingresar día y listar los valores de las variables para cada hora')
        print('[4]   Salir')
        print()
        op = input('Seleccione una opcion: ')
        menu.opcion(op, manejador)
        salir = op == '4'
        