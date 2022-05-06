class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = {'1':self.opcion1,
                           '2':self.opcion2,
                           '3':self.opcion3,
                           '4':self.salir
                           }
    def opcion(self,op,a,b):
        func = self.__switcher.get(op, lambda: print('Opción no válida'))
        if(op=='1' or op=='2' or op=='3'):
            func(a,b)
        else:
            func()
    def opcion1(self,a,b):
        suma = a + b
        print("Resultado de la suma: ",suma)
        
    def opcion2(self,a,b):
        resta=a-b
        print("Resultado de la resta: ",resta)
        
    def opcion3(self,a,b):
        a==b
        
    def salir(self):
        print('Saliendo...')