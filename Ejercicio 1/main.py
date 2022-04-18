from Email import Email
import re, csv

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(regex,correo):
    if(re.search(regex,correo)):
        return True
    else:
        return False

if __name__ == "__main__":
    
    # Primer punto
    
    nombre = input("Ingrese su nombre: ")
    idCuenta = input("Ingrese identificador de cuenta: ")
    dominio = input("Ingrese dominio de su cuenta: ")
    tipoDominio = input("Ingrese el tipo de cominio: ")
    password = input("Ingrese una contraseña para la cuenta: ")
    
    email = Email(idCuenta,dominio,tipoDominio,password)
    
    em = email.retornaEmail()
    
    print("\nEstimado {} te enviaremos un mensaje a la dirección: {}\n".format(nombre, em))
    
    # Segundo punto
    
    email.cambiarContraseña()
    
    # Tercer punto
    
    mail = Email()
    emIngresado = input("\nIngrese una dirección de Email: ")
    if(check(regex, emIngresado)):
        x = mail.crearCuenta(emIngresado)
        if type(x) == Email:
            print('\nSe creó la cuenta exitosamente')
    else:
        print("Correo no valido")
    
    # Cuarto punto
    
    dominio = input('Ingrese un dominio: ')
    cont = 0
    archivo = open('archivo.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        if fila[1] == dominio:
            cont += 1
    print('La cantidad de mails con el dominio ingresado es:', cont)
    archivo.close()