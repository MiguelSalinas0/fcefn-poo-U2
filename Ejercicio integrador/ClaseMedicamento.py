class Medicamento:
    
    __idCama = 0
    __idMedicamento = 0
    __nombreComercial = ''
    __monodroga = ''
    __presentacion = ''
    __cantAplicada = 0
    __precioTotal = 0
    
    def __init__(self, idCama, idMedicamento, nombreComercial, monodroga, presentacion, cantAplicada, precio):
        self.__idCama = idCama
        self.__idMedicamento = idMedicamento
        self.__nombreComercial = nombreComercial
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantAplicada = cantAplicada
        self.__precioTotal = precio
    
    def getIdCama(self):
        return self.__idCama
    
    def getMonodroga(self):
        return self.__monodroga
    
    def getPrecio(self):
        return self.__precioTotal
    
    def getCantidad(self):
        return self.__cantAplicada
    
    def getPresentacion(self):
        return self.__presentacion