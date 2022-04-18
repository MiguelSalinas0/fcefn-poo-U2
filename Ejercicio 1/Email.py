class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contrasena = ''
    
    def __init__(self, idCuenta="", dominio="", tipoDominio="", password=""):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contrasena = password
        
    def retornaEmail(self):
        return self.__idCuenta + '@' + self.__dominio + '.' +self.__tipoDominio
    
    def getDominio(self):
        return 'El dominio es: {}'.format(self.__tipoDominio)
    
    def crearCuenta(self, direccion):
        dominio = direccion.split("@")
        tipoDominio = dominio[1].split(".")
        password = input("Ingrese una contraseña para la cuenta: ")
        nuevo_mail = Email(dominio[0],tipoDominio[0],tipoDominio[1],password)
        print("\nIdentificador: " + nuevo_mail.__idCuenta)
        print("Dominio: " + nuevo_mail.__dominio)
        print("Tipo de Dominio: " + nuevo_mail.__tipoDominio)
        return nuevo_mail
        
    def cambiarContraseña(self):
        passActual = input("Ingrese la contraseña actual: ")
        if(passActual == self.__contrasena):
            password = input("Ingrese la nueva contraseña: ")
            self.__contrasena = password
            print("Se cambió la contraseña")
        else:
            print("Contraseña incorrecta")