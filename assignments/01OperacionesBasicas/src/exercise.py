def main():
    #escribe tu código abajo de esta línea
    print("Dame un numero:")
    entrada1= input()
    print("Dame otro numero:")
    entrada2= input()
    suma= int(entrada1) + int(entrada2)
    resta= int(entrada1) - int(entrada2)
    multiplicacion= int(entrada1) * int(entrada2)
    print( "Suma:" + str(suma))
    print( "Resta:" + str(resta))
    print( "Multiplicación:" + str(multiplicacion))
    pass


if __name__ == '__main__':
    main()
