class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millasAcum = 0
    
    def __init__(self, num, dni, nombre, apellido, millasAc):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAc
    
    def mostrarDatos(self):
        print('\nNumero de viajero: {}'.format(self.__num_viajero))
        print('DNI: {}'.format(self.__dni))
        print('Nombre: {}'.format(self.__nombre))
        print('Apellido: {}'.format(self.__apellido))
        print('Millas: {}'.format(self.__millasAcum))
    
    def cantidadTotaldeMillas(self):
        return self.__millasAcum
    
    def acumularMillas(self, millas):
        self.__millasAcum += millas
        return self.__millasAcum
    
    def canjearMillas(self, millas):
        if(millas <= self.__millasAcum):
            print('Se pueden canjear las millas')
            millasRestantes = self.__millasAcum - millas
            print('Millas restantes: ',millasRestantes)
            self.__millasAcum = millasRestantes
        else:
            print('ERROR: millas insuficientes')
    
    def getNro(self):
        return self.__num_viajero