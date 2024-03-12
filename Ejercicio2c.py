inicio = 0
casa = -1
while inicio == 0:
    print("-----Bienes Raíces-----")
    print("0- Salir")
    print("1- Valor de casa")
    print("2- Calcular pie y cuotas")
    bandera = 0
    while bandera == 0:
        try:
            op = int(input("Ingrese su opción: "))
            if op >= 0 or op <= 2:
                bandera = 1
        except ValueError:
            print("Ingrese una opción válida")
    bandera = 0
    if op == 1:
        while bandera == 0:
            try:
                casa = int(input("Ingrese el valor de la casa: "))
                if casa >= 0:
                    bandera = 1
            except ValueError:
                print("Ingrese un valor válido")
    if op == 2:
        if casa == -1:
            print("Debe ingresar el valor de la casa primero")
        if casa >= 0:
            bandera = 0
            while bandera == 0:
                try:
                    sueldo = int(input("Ingrese el sueldo: "))
                    bandera = 1
                except ValueError:
                    print("Ingrese un valor mayor o igual a 0")
            if sueldo >= 80000:
                pie = round(casa * 0.15, 3)
                cuotas = round((casa * 0.85)/(10*12), 3)
                print ("-----------------------------")
                print ("El pie a pagar es de: $" +str(pie))
                print ("El valor de cuotas durante 10 años es de: $"+ str(cuotas))
            if sueldo >= 0 and sueldo < 80000:
                pie = round(casa * 0.3, 3)
                cuotas = round((casa * 0.7)/(7*12), 3)
                print ("-----------------------------")
                print ("El pie a pagar es de: $"+str(pie))
                print ("El valor de cuotas durante 10 años es de: $"+str(cuotas))
    if op == 0:
        print ("Adios")
        inicio = 1