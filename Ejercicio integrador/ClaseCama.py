class Cama:
    
    __idCama = 0
    __habitacion = 0
    __estado = bool
    __apellidoYnombre = ''
    __diagnostico = ''
    __fechaInternacion = ''
    __fechaAlta = ''
    
    def __init__(self, idCama, habitacion, estado, apellidoNombre, diagnostico, fechaInternacion, fechaAlta):
        self.__idCama = idCama
        self.__habitacion = habitacion
        self.__estado = estado
        self.__apellidoYnombre = apellidoNombre
        self.__diagnostico = diagnostico
        self.__fechaInternacion = fechaInternacion
        self.__fechaAlta = fechaAlta
    
    def getApellidoYnombre(self):
        return self.__apellidoYnombre
    
    def getEstado(self):
        return self.__estado
    
    def getDiagnostico(self):
        return self.__diagnostico
    
    def getIdCama(self):
        return self.__idCama
    
    def getHabitacion(self):
        return self.__habitacion
    
    def getFechaInternacion(self):
        return self.__fechaInternacion
    
    def getFechaAlta(self):
        return self.__fechaAlta
    
    def setFechaAlta(self, fecha):
        self.__fechaAlta = fecha