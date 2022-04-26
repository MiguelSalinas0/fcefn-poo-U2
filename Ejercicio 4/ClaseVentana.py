class Ventana:
    __titulo = ''
    __xSupIzq = 0
    __ySupIzq = 0
    __xInfDer = 0
    __yInfDer = 0
    
    def __init__(self, t = '', xSI = 0, ySI = 0, xID = 500, yID = 500):
        self.__titulo = t
        self.__xSupIzq = xSI
        self.__ySupIzq = ySI
        self.__xInfDer = xID
        self.__yInfDer = yID
        
    def getTitulo(self):
        return self.__titulo
    
    def mostrar(self):
        print('{} {} \n\n\n      {} {}'.format(self.__xSupIzq, self.__ySupIzq, self.__xInfDer, self.__yInfDer))
        
    def ancho(self):
        return self.__xInfDer - self.__xSupIzq
    
    def alto(self):
        return self.__yInfDer - self.__ySupIzq
    
    def moverDerecha(self, valor = 1):
        if(self.__xSupIzq < self.__xInfDer):
            self.__xInfDer += valor
            self.__xSupIzq += valor
        
    def moverIzquierda(self, valor = 1):
        if(self.__xSupIzq < self.__xInfDer):
            self.__xInfDer -= valor
            self.__xSupIzq -= valor
        
    def bajar(self, valor = 1):
        if(self.__ySupIzq < self.__yInfDer):
            self.__yInfDer -= valor
            self.__ySupIzq -= valor
        
    def subir(self, valor = 1):
        if(self.__ySupIzq < self.__yInfDer):
            self.__yInfDer += valor
            self.__ySupIzq += valor
        
