class Menu:
    __switcher = None
    
    def __init__(self):
        self.__switcher = {'1':self.opcion1,
                           '2':self.opcion2,
                           '3':self.opcion3,
                           '4':self.salir
                           }
    def opcion(self,op,manejador):
        func = self.__switcher.get(op, lambda: print('Opción no válida'))
        if(op=='1' or op=='2' or op=='3'):
            func(manejador)
        else:
            func()
        
    def opcion1(self, manejador):
        manejador.mayorYmenorTem()
        manejador.mayorYmenorHumedad()
        manejador.mayorYmenorPresion()
        
    def opcion2(self, manejador):
        manejador.temperaturaProm()
        
    def opcion3(self, manejador):
        dia = int(input('Ingrese un día para listar sus variables por hora: '))
        manejador.listarVariables(dia)
        
    def salir(self):
        print('Saliendo...')