import csv
from ClasePlanAhorro import PlanAhorro

class Manejador:
    
    __listado = []
    
    def __init__(self):
        self.__listado = []
    
    def agregarPlan(self, plan):
        if(type(plan) == PlanAhorro):
            self.__listado.append(plan)
            
    def testArchivo(self):
        archivo = open('Planes.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear Cabecera'''
                bandera = not bandera
            else:
                cod = int(fila[0])
                modelo = fila[1]
                version = fila[2]
                valor = float(fila[3])
                plan = PlanAhorro(cod, modelo, version, valor)
                self.agregarPlan(plan)
        archivo.close()
        
    def mostrarDatos(self):
        for item in self.__listado:
            item.mostrarDatos()
    
    def actualizarValor(self):
        for item in self.__listado:
            item.mostrarDatos('ac')
            valActual = float(input("Ingrese el valor actual del vehículo: "))
            item.setValor(valActual)
    
    def mostrarValoresInfaCuota(self, valor):
        for item in self.__listado:
            if(item.calcularCuota() < valor):
                item.mostrarDatos('ac')
        
    def buscarPlan(self, nro):
        pos = 0
        bandera = False
        while pos < len(self.__listado) and bandera == False:
            if self.__listado[pos].getcodi() == nro:
                bandera = True
                return pos
            else:
                pos += 1
        
    def actualizarCuotasLicitar(self, nuevasCuotas):
        PlanAhorro.setCantCuotasLicitar(nuevasCuotas)
        
    def escribir(self):
        archivo = open('Planes.csv', 'w')
        archivo.write('Cod,modelo,version,valor\n')
        for item in self.__listado:
            archivo.write('{};{};{};{}\n'.format(item.getcodi(), item.getmodel(), item.getver(), item.getvalor()))
        archivo.close()
    
    def montoPagoParaLicitar(self):
        for item in self.__listado:
            item.mostrarDatos('ac')
            print('Monto que se debe haber pagado para licitar: {:.2f}\n'.format(item.montoPagadoParaLicitar()))