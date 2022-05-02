class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = {'1':self.opcion1,
                           '2':self.opcion2,
                           '3':self.opcion3,
                           '4':self.opcion4,
                           '5':self.salir
                           }
    def opcion(self,op,manejador):
        func = self.__switcher.get(op, lambda: print('Opción no válida'))
        if(op=='1' or op=='2' or op=='3' or op=='4'):
            func(manejador)
        else:
            func()
    def opcion1(self,manejador):
        manejador.actualizarValor()
        manejador.escribir()
    def opcion2(self,manejador):
        cuota = float(input('Ingrese un valor para ver los planes cuyas cuotas son inferiores: '))
        manejador.mostrarValoresInfaCuota(cuota)
    def opcion3(self,manejador):
        manejador.montoPagoParaLicitar()
    def opcion4(self,manejador):
        plan = int(input('Ingrese un codigo de plan para modificar las cuotas para licitar: '))
        indice = manejador.buscarPlan(plan)
        if (indice != None):
            cuotas = int(input('Ingrese la nueva cantidad de cuotas: '))
            manejador.actualizarCuotasLicitar(cuotas)
            print('Cambio exitoso!!!')
        else:
            print('No se encontró el plan')
    def salir(self):
        print('Saliendo...')