import csv
from ClaseMedicamento import Medicamento

class ManejaMedicamento:
    
    __listaMedicamento = []
    __total = 0
    
    def __init__(self):
        self.__listaMedicamento = []
    
    def agregarMedicamento(self, medicamento):
        if(type(medicamento) == Medicamento):
            self.__listaMedicamento.append(medicamento)
    
    def testArchivo(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear Cabecera'''
                bandera = not bandera
            else:
                idC = int(fila[0])
                idM = int(fila[1])
                nombreComercial = fila[2]
                monodroga = fila[3]
                presentacion = fila[4]
                cantAplicada = int(fila[5])
                precio = int(fila[6])
                medicamento = Medicamento(idC, idM, nombreComercial, monodroga, presentacion, cantAplicada, precio)
                self.agregarMedicamento(medicamento)
        archivo.close()
        
    def getPrecio(self, indice):
        return self.__listaMedicamento[indice].getPrecio()
    
    def getCantidad(self, indice):
        return self.__listaMedicamento[indice].getCantidad()
    
    def getPresentacion(self, indice):
        return self.__listaMedicamento[indice].getPresentacion()
    
    def buscarMedicamento(self, nro):
        print('\nMedicamento/Monodroga \t Presentación \t Cantidad \t Precio')
        self.__total = 0
        for item in self.__listaMedicamento:
            idCama = item.getIdCama()
            if idCama == nro:
                print('{:<20} {:^20} {:^8} {:^10}'.format(item.getMonodroga(), item.getPresentacion(), item.getCantidad(), item.getPrecio()))
                self.__total += item.getPrecio()
        print('Total adeudado: {:^80}'.format(self.__total))