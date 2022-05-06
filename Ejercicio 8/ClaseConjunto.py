class conjunto:
    
    __lista=[]
    
    def __init__(self):
        self.__lista=[]
        
    def mostrar(self):
        print(self.__lista)
        
    def agregar(self,num):
        self.__lista.append(num)
        self.mostrar()
        
    def getconjunto(self):
        return self.__lista
    
    def __add__(self,union):
        nueva=[]
        nueva.extend(self.__lista)
        nueva.extend(union.getconjunto())
        nueva=set(nueva)
        return nueva
    
    def __sub__(self,resta):
        lista=[]
        lista.extend(self.__lista)
        conjunto=resta.getconjunto()
        for valor in conjunto:
            if(valor in lista):
                lista.remove(valor)
        return lista
    
    def __eq__(self,conju):
        conjunto=conju.getconjunto()
        a=len(self.__lista)
        b=len(conjunto)
        if a==b:
            i=0
            while(i<b and conjunto[i] == self.__lista[i]):
                i+=1
            if(i==a):
                print("Los conjuntos son iguales")
                print("Conjunto 1",self.__lista)
                print("Conjunto 2",conjunto)
            else:
                print("Los conjuntos son distintos")
                print("Conjunto 1",self.__lista)
                print("Conjunto 2",conjunto)
        else:
            print("Los conjuntos son distintos")
            print("Conjunto 1",self.__lista)
            print("Conjunto 2",conjunto)