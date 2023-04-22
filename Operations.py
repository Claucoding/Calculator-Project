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
