from Clase import Conjunto
if __name__ == '__main__':
    def carga(numero):
        lista=[]
        print("Ingrese los valores del conjunto {} y s para finalizar el ingreso".format(numero))
        valor=input("Ingrese un valor:")
        while(valor!= 's'):
            valor=int(valor)
            if(type(valor==int)):
                lista.append(valor)
            else:
                print("Tipo de valor incorrecto solo se permiten enteros, o S para salir")
            valor=input("Ingrese un valor:")
        lista=list(set(lista))
        return Conjunto(lista)
    
    def op1(conjunto1):
        conjunto2=carga(2)
        resultado=conjunto1+conjunto2
        if(resultado!="Error"):
            print("Conjunto resultante: ",resultado)
        else:
            print("Hubo un error en el tipo de dato ingresado")
    def op2(conjunto1):
        conjunto2=carga(2)
        resultado=conjunto1-conjunto2
        if(resultado!="Error"):
            print("Conjunto resultante: ",resultado)
        else:
            print("Hubo un error en el tipo de dato ingresado")
    def op3(conjunto1):
        conjunto2=carga(2)
        conjunto1==conjunto2
    def op4(conjunto1):
        conjunto1.Test()
    def op5():
        print("Usted salio del programa")
    op=None
    lista=[]
    dicdeopciones={1:op1,2:op2,3:op3,4:op4,5:op5}
    conjunto1=carga(1)
    while(op!=5):
        print("Menú:")
        print("Ingrese 1 para unir otro conjunto al ingresado previamente")
        print("Ingrese 2 para diferenciar otro conjunto al ingresado previamente")
        print("Ingrese 3 para comparar si un conjunto ingresado es igual al ingresado previamente ")
        print("Ingrese 4 para llevar a cabo un test")
        print("Ingrese 5 para salir")
        op=int(input("Ingrese la opción:"))
        funcion=dicdeopciones.get(op,lambda:print("Valor incorrecto ingresado, rango 1-5, 5 para salir"))
        if(op==5):
            funcion()
        else:
            funcion(conjunto1)