import math as m


def sum(cantidad_numeros, cont1):
    suma = 0
    while cont1 <= cantidad_numeros:
        frase_suma = f"""Enter variable {cont1}: """
        number1 = float(input(frase_suma))
        suma += number1
        cont1 += 1

    return suma


def multi(cantidad_numeros, cont1):
    multipli = 1
    while cont1 <= cantidad_numeros:
        frase_multi = f"""Enter variable {cont1}: """
        n2 = float(input(frase_multi))
        multipli *= n2
        cont1 += 1
    return multipli


def div(numerador, denominador):
    # numerador = float(input("Enter the numerator: "))
    # denominador = float(input("Ingrese The denominator: "))
    condicion = input(
        "Do you want to know the rest of division? yes/no: ")
    while condicion != "yes" and condicion != "no":
        condicion = input(
            "ERROR. Enter yes or no: ")
    if condicion == "yes":
        division = numerador / denominador
        resto = numerador % denominador
        print(" The division result is:",
              division, "and its rest is:", resto)
    if condicion == "no":
        division = numerador / denominador
        print("The division result is: ", division)

    return division


def hypotenuse(cateto1, cateto2):
    Hipotenusa = m.sqrt(m.pow(cateto1, 2) + m.pow(cateto2, 2))

    return Hipotenusa


def degtorad(grados):
    radianes = (grados * m.pi)/180
    print(f"{grados}° are {radianes} radians")

    return radianes


def inchtocent(pulgadas):
    centimetros = (pulgadas*2.54)
    print(f"{pulgadas} inch are {centimetros} centimeters")

    return centimetros


def poundtokilos(pounds):
    kilos = (pounds*0.453592)
    print(f"{pounds} pound are {kilos} kilos")

    return kilos


def farkeltocel(temp, farorkel):
    while farorkel not in ("K", "F"):
        farorkel = input("Error. Enter 'F' or 'K': ")
        if farorkel == "K":
            celcius = temp - 273.15
            print(f"{temp} Kelvin are {celcius}° Celcius")
        if farorkel == "F":
            celcius = 5*(temp-32)/9
            print(f"{temp}° Fahrenheit are {celcius}° Celcius")
