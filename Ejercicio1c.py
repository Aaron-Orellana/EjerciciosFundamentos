def Operacion():
    bandera = 0
    while bandera == 0:
            try:
                a = int(input("¿Desea continuar? (1) Si (2) No: "))
                if a == 1 :
                    bandera = 1
                    inicio = 0
                    return inicio
                if a == 2:
                    bandera = 1
                    print("Adios")
                    inicio = 2
                    return inicio
            except ValueError:
                print("Ingrese un numero")

print("-----Teatro-----")
bandera = 0
while bandera == 0: 
    try:
        precio = int(input("Ingrese el valor de la entrada: "))
        if precio >= 0:
            bandera = 1
    except ValueError:
        print("Ingrese un número")
inicio = 0
while inicio == 0:
    print("----------------------------------------")
    bandera = 0
    while bandera == 0:
        try:
            edad = int(input("Ingrese su edad (No esta permitido el ingreso a menores de 5): "))
            if edad >=5:
                bandera = 1
        except ValueError:
            print("Ingrese un numero")
    if edad >= 5 and edad <= 14:
        perdida = precio * 0.35 
        print ("Por el descuento en la entrada de Categoria 1, el teatro deja de percibir : $"+ str(perdida))
        inicio= Operacion()
    if edad >= 15 and edad <= 19:
        perdida = precio * 0.25
        print ("Por el descuento en la entrada de Categoria 2, el teatro deja de percibir : $"+ str(perdida))
        inicio = Operacion()
    if edad >= 20 and edad <= 45:
        perdida = precio * 0.1 
        print ("Por el descuento en la entrada de Categoria 3, el teatro deja de percibir : $" + str(perdida))
        inicio = Operacion()
    if edad >= 46 and edad <= 65:
        perdida = precio * 0.25
        print ("Por el descuento en la entrada de Categoria 4, el teatro deja de percibir : $"+ str(perdida))
        inicio = Operacion()
    if edad >= 66:
        perdida = precio * 0.35
        print ("Por el descuento en la entrada de Categoria 5, el teatro deja de percibir : $"+ str(perdida))
        inicio = Operacion()