print("Programa que determina si un año es bisiesto o no")

año = None
while True:
    if año == None:
        try:
            anio = int(input("Introduce un año: "))
        except ValueError:
            print("Por favor, introduce un año válido")
            continue
    if anio < 1582:
        print("Por favor, introduce un año válido")
        continue 
    elif anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
        