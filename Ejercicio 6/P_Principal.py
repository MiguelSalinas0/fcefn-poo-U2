from ManejadorViajeroFrecuente import ManejadorViajeroFrecuente

if __name__ == '__main__':
    unmanejador = ManejadorViajeroFrecuente()
    unmanejador.testArchivo()
    
    print('Listado de viajeros ordenados por millas\n')
    unmanejador.ordenarLista()
    unmanejador.mostrarLista()
    
    print('\n======= Sumar millas =======')
    viajero = int(input('Ingrese numero de viajero: '))
    millas = int(input('Ingrese millas a sumar: '))
    unmanejador.sumarMillas(viajero, millas)
    
    print('\n======= Restar millas =======')
    viajero = int(input('Ingrese numero de viajero: '))
    millas = int(input('Ingrese millas a restar: '))
    unmanejador.restarMillas(viajero, millas)
    
    print('\nListado de viajeros con millas actualizadas\n')
    unmanejador.mostrarLista()
