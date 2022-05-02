from ManejadorViajeroFrecuente import ManejadorViajeroFrecuente

if __name__ == '__main__':
    unmanejador = ManejadorViajeroFrecuente()
    unmanejador.testArchivo()
    
    print('Listado de viajeros ordenados por millas\n')
    unmanejador.ordenarLista()
    unmanejador.mostrarLista()
    
    millas = int(input('\nIngrese millas para comparar: '))
    viajero = int(input('Ingrese numero de viajero: '))
    unmanejador.comparar(viajero, millas)
    
    print('\n======= Sumar millas =======')
    millas = int(input('Ingrese millas a sumar: '))
    viajero = int(input('Ingrese numero de viajero: '))
    unmanejador.sumarMillas(viajero, millas)
    
    print('\n======= Restar millas =======')
    millas = int(input('Ingrese millas a restar: '))
    viajero = int(input('Ingrese numero de viajero: '))
    unmanejador.restarMillas(viajero, millas)
    
    print('\nListado de viajeros con millas actualizadas\n')
    unmanejador.mostrarLista()