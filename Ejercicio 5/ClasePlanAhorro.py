class PlanAhorro:
    
    __cuotasPlan = 60
    __cantCuotasLicitar = 8
    
    __codigo = 0
    __modelo = ''
    __version = ''
    __valor = 0.0
    
    def __init__(self, cod = 0, modelo = '', version = 0, valor = 0.0):
        self.__codigo = cod
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor
        
    @classmethod
    def getCuotasDePlan(cls):
        return cls.__cuotasPlan
    
    @classmethod
    def setCuotasDePlan(cls, cantCuotas):
        cls.__cuotasPlan = cantCuotas
    
    @classmethod
    def getCantCuotasLicitar(cls):
        return cls.__cantCuotasLicitar
    
    @classmethod
    def setCantCuotasLicitar(cls, cuotas):
        cls.__cantCuotasLicitar = cuotas
    
    def montoPagadoParaLicitar(self):
        return self.getCantCuotasLicitar() * self.calcularCuota()
    
    def calcularCuota(self):
        return (self.__valor / self.getCuotasDePlan()) + self.__valor * 0.10
    
    def mostrarDatos(self, st = ''):
        if (st == 'ac'):
            return print("\n{} {} {}".format(self.__codigo, self.__modelo, self.__version))
        else:
            return print("\n{} {} {} {}".format(self.__codigo, self.__modelo, self.__version, self.__valor))
    
    def setValor(self, nValor):
        self.__valor = nValor
        return self.__valor
    
    def getcodi(self):
        return self.__codigo
    
    def getmodel(self):
        return self.__modelo
    
    def getver(self):
        return self.__version
    
    def getvalor(self):
        return self.__valor