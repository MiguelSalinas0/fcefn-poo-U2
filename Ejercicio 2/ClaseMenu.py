class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = {'1':self.opcion1,
                           '2':self.opcion2,
                           '3':self.opcion3,
                           '4':self.salir
                           }
    def opcion(self,op,viajero):
        func = self.__switcher.get(op, lambda: print('Opción no válida'))
        if(op=='1' or op=='2' or op=='3'):
            func(viajero)
        else:
            func()
    def opcion1(self,viajero):
        print('Cantidad total de millas acumuladas: {}'.format(viajero.cantidadTotaldeMillas()))
    def opcion2(self, viajero):
        ultMilla = int(input('Ingrese cantidad de millas del últimmo viaje: '))
        viajero.acumularMillas(ultMilla)
        tot = viajero.cantidadTotaldeMillas()
        print('Millas totales: ',tot)
    def opcion3(self,viajero):
        millasCanj = int(input('Ingrese cantidad de millas a canjear: '))
        viajero.canjearMillas(millasCanj)
    def salir(self):
        print('Saliendo...')