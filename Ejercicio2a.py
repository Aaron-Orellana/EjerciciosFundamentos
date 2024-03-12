print("-----Bienes Raíces-----")
casa = int(input("Ingrese el valor de la casa: "))
if casa >= 0:
    sueldo = int(input("Ingrese el sueldo: "))
    if sueldo >= 80000:
        pie = round(casa * 0.15, 2)
        cuotas = round((casa * 0.85)/(10*12), 3)
        print ("El pie a pagar es de: $" +str(pie))
        print ("El valor de cuotas durante 10 años es de: $"+ str(cuotas))
    if sueldo >= 0 and sueldo < 80000:
        pie = round(casa * 0.3, 2)
        cuotas = round((casa * 0.7)/(7*12), 3)
        print ("El pie a pagar es de: $"+str(pie))
        print ("El valor de cuotas durante 10 años es de: $"+str(cuotas))