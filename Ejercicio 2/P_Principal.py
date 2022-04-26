from ManejadorViajeroFrecuente import ManejadorViajeroFrecuente
from ClaseMenu import Menu

if __name__ == '__main__':
    unmanejador = ManejadorViajeroFrecuente()
    unmanejador.testArchivo()
    unmanejador.mostrarLista()
    menu = Menu()
    nro = int(input('\nIngrese el número de un viajero frecuente: '))
    indice = unmanejador.buscarViajero(nro)
    if indice != None:
        print('Indice: ',indice)
        viajero = unmanejador.getViajero(indice)
        salir = False
        while not salir:
            print('\n______________ Menu ______________\n')
            print('[1]   Consultar el total de millas')
            print('[2]   Acumular millas')
            print('[3]   Canjear millas')
            print('[4]   Salir')
            print()
            op = input('Seleccione una opcion: ')
            menu.opcion(op, viajero)
            salir = op == '4'
    else:
        print('No se encontró el número de viajero')