import csv
from Registro import Registro

class ManejadorRegistro:
    
    __dias = 30
    __horas = 24
    __listaTemp = []
    
    def __init__(self):
        for f in range(self.__horas):
            self.__listaTemp.append([])
            for c in range(self.__dias):
                self.__listaTemp[f].append(0)
                
    def testArchivo(self):
        archivo = open('variablesmeteorologicas.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear Cabecera'''
                bandera = not bandera
            else:
                dia = int(fila[0])
                hora = int(fila[1])
                temperatura = float(fila[2])
                humedad = int(fila[3])
                presion = int(fila[4])
                reg = Registro(temperatura, humedad, presion)
                self.__listaTemp[hora-1][dia-1] = reg
        archivo.close()
    
    def mayorYmenorTem(self):
        mayor = 0
        menor = 900000000
        for f in range(self.__horas):
            for c in range(self.__dias):
                if(self.__listaTemp[f][c].getTemperatura() > mayor):
                    mayor = self.__listaTemp[f][c].getTemperatura()
                    dT = c
                    hT = f
                if(self.__listaTemp[f][c].getTemperatura() < menor):
                    menor = self.__listaTemp[f][c].getTemperatura()
                    dmT = c
                    hmT = f
        print('\nMayor temperatura: {}°, el día {} a las {}hs'.format(mayor, dT + 1, hT + 1))
        print('Menor temperatura: {}°, el día {} a las {}hs'.format(menor, dmT + 1, hmT + 1))
    
    def mayorYmenorHumedad(self):
        mayor = 0
        menor = 900000000
        for f in range(self.__horas):
            for c in range(self.__dias):
                if(self.__listaTemp[f][c].getHumedad() > mayor):
                    mayor = self.__listaTemp[f][c].getHumedad()
                    d = c
                    h = f
                if(self.__listaTemp[f][c].getHumedad() < menor):
                    menor = self.__listaTemp[f][c].getHumedad()
                    dia = c
                    hora = f
        print('\nMayor humedad: {}°, el día {} a las {}hs'.format(mayor, d + 1, h + 1))
        print('Menor humedad: {}°, el día {} a las {}hs'.format(menor, dia + 1, hora + 1))
        
    def mayorYmenorPresion(self):
        mayor = 0
        menor = 900000000
        for f in range(self.__horas):
            for c in range(self.__dias):
                if(self.__listaTemp[f][c].getPresion() > mayor):
                    mayor = self.__listaTemp[f][c].getPresion()
                    dP = c
                    hP = f
                if(self.__listaTemp[f][c].getPresion() < menor):
                    menor = self.__listaTemp[f][c].getPresion()
                    diaP = c
                    horaP = f
        print('\nMayor presión atmosférica: {}hPa, el día {} a las {}hs'.format(mayor, dP + 1, hP + 1))
        print('Menor presión atmosférica: {}hPa, el día {} a las {}hs'.format(menor, diaP + 1, horaP +1))
        
    def temperaturaProm(self):
        for f in range(self.__horas):
            suma = 0
            for c in range(self.__dias):
                suma += self.__listaTemp[f][c].getTemperatura()
            promedio = suma / self.__dias
            print('{}hs, promedio: {:.2f}'.format(f, promedio))
    
    def listarVariables(self, dia):
        print("\nHora Temperatura Humedad Presión\n")
        for f in range(self.__horas):
            if(type(self.__listaTemp[f][dia-1]) == Registro):
                print('{:>3} {:>8} {:>8} {:>8}'.format(f, self.__listaTemp[f][dia-1].getTemperatura(), self.__listaTemp[f][dia-1].getHumedad(), self.__listaTemp[f][dia-1].getPresion()))
            
