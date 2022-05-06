from ClaseConjunto import conjunto
from ClaseMenu import Menu

if __name__ == "__main__":
    
    menu = Menu()
    
    a = conjunto()
    b = conjunto()
    
    num=input("Ingesar valor positivo para cargar el primer conjunto: ")
    while(num != 'fin'):
        num=int(num)
        if(type(num)==int):
            a.agregar(num)
            num=input("Ingesar valor positivo para cargar el primer conjunto, finalizar con 'fin': ")
        else:
            print("ERROR: número mal ingresado")
    
    num=input("\nIngesar valor positivo para cargar el segundo conjunto: ")
    while(num != 'fin'):
        num=int(num)
        if(type(num)==int):
            b.agregar(num)
            num=input("Ingesar valor positivo para cargar el primer conjunto, finalizar con 'fin': ")
        else:
            print("ERROR: número mal ingresado")
    
    salir = False
    while not salir:
        print('\n______________ Menu ______________\n')
        print('[1]   Sumar los objetos ingresados')
        print('[2]   Restar los objetos ingresados')
        print('[3]   Saber si son iguales')
        print('[4]   Salir')
        print()
        op = input('Seleccione una opcion: ')
        menu.opcion(op,a,b)
        salir = op == '4'