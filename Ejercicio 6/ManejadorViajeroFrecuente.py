import csv
from ViajeroFrecuente import ViajeroFrecuente

class ManejadorViajeroFrecuente:
    __listaViajeros = []
    
    def __init__(self):
        self.__listaViajeros = []
    
    def agregarViajero(self, viajero):
        if(type(viajero) == ViajeroFrecuente):
            self.__listaViajeros.append(viajero)
    
    def mostrarLista(self):
        for i in self.__listaViajeros:
            i.mostrarDatos()
    
    def buscarViajero(self, nro):
        pos = 0
        bandera = False
        while pos < len(self.__listaViajeros) and bandera == False:
            if self.__listaViajeros[pos].getNro() == nro:
                bandera = True
                return pos
            else:
                pos += 1
    
    def testArchivo(self):
        archivo = open('ViajeroFrecuente.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear Cabecera'''
                bandera = not bandera
            else:
                nro = int(fila[0])
                dni = int((fila[1].replace('.','')))
                nombre = fila[2]
                apellido = fila[3]
                millas = int(fila[4])
                viajero = ViajeroFrecuente(nro, dni, nombre, apellido, millas)
                self.agregarViajero(viajero)
        archivo.close()
    
    def ordenarLista(self):
        lenght = len(self.__listaViajeros)-1
        for i in range(0,lenght):
            for j in range(0,lenght):
                if self.__listaViajeros[j] > self.__listaViajeros[j+1]:
                    aux = self.__listaViajeros[j]
                    self.__listaViajeros[j] = self.__listaViajeros[j+1]
                    self.__listaViajeros[j+1] = aux
    
    def sumarMillas(self, viajero, millas):
        viaj = self.buscarViajero(viajero)
        if(viaj == None):
            print('ERROR: No se encontró el viajero')
        else:
            self.__listaViajeros[viaj] + millas
            print('Millas totales: {}'.format(self.__listaViajeros[viaj].cantidadTotaldeMillas()))
        
    def restarMillas(self, viajero, millas):
        viaj = self.buscarViajero(viajero)
        if(viaj == None):
            print('ERROR: No se encontró el viajero')
        else:
            self.__listaViajeros[viaj] - millas
            print('Millas totales: {}'.format(self.__listaViajeros[viaj].cantidadTotaldeMillas()))