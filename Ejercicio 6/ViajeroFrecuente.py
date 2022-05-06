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
        print('Viajero: {}, millas: {}'.format(self.__num_viajero, self.__millasAcum))

    def cantidadTotaldeMillas(self):
        return self.__millasAcum
    
    def getNro(self):
        return self.__num_viajero
    
    def __gt__(self, otro):
        if(self.__millasAcum > otro.__millasAcum):
            return False
        else:
            return True
    
    def __add__(self, millas):
        self.__millasAcum += millas
        
    def __sub__(self, millas):
        self.__millasAcum -= millas