import csv
import numpy as np
from ClaseCama import Cama

class ManejadorCama:
    
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    
    def __init__(self, dimension = 5, incremento = 5):
        self.__camas = np.empty(dimension, dtype = Cama)
        self.__dimension = dimension
        self.__incremento = incremento
    
    def agregarCama(self, unaCama):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__camas.resize(self.__dimension)
        self.__camas[self.__cantidad] = unaCama
        self.__cantidad += 1
    
    def testArchivo(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear Cabecera'''
                bandera = not bandera
            else:
                idC = int(fila[0])
                habitacion = int(fila[1])
                estado = bool(fila[2])
                apellidoYnombre = fila[3]
                diagnostico = fila[4]
                fechaInternacion = fila[5]
                fehaAlta = fila[6]
                cama = Cama(idC, habitacion, estado, apellidoYnombre, diagnostico, fechaInternacion, fehaAlta)
                self.agregarCama(cama)
        archivo.close()
                
    def getApellidoYnombre(self, indice):
        return self.__camas[indice].getApellidoYnombre()
    
    def getIdCama(self, indice):
        return self.__camas[indice].getIdCama()
    
    def getHabitacion(self, indice):
        return self.__camas[indice].getHabitacion()
    
    def getDiagnostico(self, indice):
        return self.__camas[indice].getDiagnostico()
    
    def getFechaInternacion(self, indice):
        return self.__camas[indice].getFechaInternacion()
    
    def getFechaAlta(self, indice):
        return self.__camas[indice].getFechaAlta()
    
    def setFechaAlta(self, indice, fecha):
        self.__camas[indice].setFechaAlta(fecha)
        
    def listarPacientes(self, diag):
        print('\nApellido y Nombre \t IdCama \t Fecha de Internación')
        for i in range(self.__cantidad):
            if(self.__camas[i].getEstado() and self.__camas[i].getDiagnostico() == diag):
                print('{:<20} {:^8} {:^25}'.format(self.__camas[i].getApellidoYnombre(), self.__camas[i].getIdCama(), self.__camas[i].getFechaInternacion()))
    
    def buscarPaciente(self, nombreYapellido):
        pos = 0
        bandera = False
        while pos < self.__cantidad and bandera == False:
            if self.__camas[pos].getApellidoYnombre() == nombreYapellido:
                bandera = True
                return pos
            else:
                pos += 1