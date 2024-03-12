print("-----Teatro-----")
precio = int(input("Ingrese el valor de la entrada: "))
if precio >= 0:
    edad = int(input("Ingrese su edad: "))
    if edad >= 5 and edad <= 14:
        perdida = precio * 0.35 
        print ("Por el descuento en la entrada de Categoria 1, el teatro deja de percibir : $"+ str(perdida))
    if edad >= 15 and edad <= 19:
        perdida = precio * 0.25
        print ("Por el descuento en la entrada de Categoria 2, el teatro deja de percibir : $"+ str(perdida))
    if edad >= 20 and edad <= 45:
        perdida = precio * 0.1 
        print ("Por el descuento en la entrada de Categoria 3, el teatro deja de percibir : $" + str(perdida))
    if edad >= 46 and edad <= 65:
        perdida = precio * 0.25
        print ("Por el descuento en la entrada de Categoria 4, el teatro deja de percibir : $"+ str(perdida))
    if edad >= 66:
        perdida = precio * 0.35
        print ("Por el descuento en la entrada de Categoria 5, el teatro deja de percibir : $"+ str(perdida))