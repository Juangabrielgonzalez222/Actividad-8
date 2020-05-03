class Conjunto():
    __valores=[]
    def __init__(self,lista):
        if(type(lista)==list):
            self.__valores=lista
        else:
            print("Error el parametro no es una lista")
    def getValores(self):
        return(self.__valores)
    def __add__(self,conjunto):
        if(type(conjunto)==Conjunto):
            union=[]
            union.extend(self.__valores)
            union.extend(conjunto.getValores())
            union=list(set(union))
            return union
        else:
            return "error"
    def __sub__(self,conjunto):
        if(type(conjunto)==Conjunto):
            union=[]
            union.extend(self.__valores)
            conjunto2=conjunto.getValores()
            for valor in conjunto2:
                if(valor in union ):
                    union.remove(valor)
            return union
        else:
            return "error"
    def __eq__(self,conjunto):
        if(type(conjunto)==Conjunto):
            conjunto2=conjunto.getValores()
            if(len(self.__valores)==len(conjunto2)):
                i=0
                while(i<len(conjunto2) and conjunto2[i] in self.__valores):
                    i+=1
                if(i==len(conjunto2)):
                    print("Los conjuntos son iguales")
                else:
                    print("Los conjuntos son distintos")
            else:
                print("Los conjuntos son distintos")
        else:
            print("No es correcto el tipo de dato")
    def Test(self):
        print("Función de testeo:")
        print("Resultado:",self.__sub__(Conjunto([1,2,3,4,5])))
        print("Resultado:",self.__sub__(Conjunto([-1,-2,-3,-4,-5])))
        print("Resultado:",self.__add__(Conjunto([1,3,5,7])))
        print(self.__add__("prueba"))
        self.__eq__(Conjunto([1,2,4]))
        self.__eq__(Conjunto([1,2,3]))
        self.__eq__(Conjunto([-1,-2,-4]))
                
                    
        