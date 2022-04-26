class Registro:
    __temperatura = 0.0
    __humedad = 0
    __presion = 0
    
    def __init__(self, t = 0.0, h = 0, p = 0):
        self.__temperatura = t
        self.__humedad = h
        self.__presion = p
        
    def getTemperatura(self):
        return self.__temperatura
    
    def getHumedad(self):
        return self.__humedad
    
    def getPresion(self):
        return self.__presion