def sum(cantidad_numeros, cont1):
    suma = 0
    while cont1 <= cantidad_numeros:
        frase_suma = f"""Enter variable {cont1}: """
        number1 = float(input(frase_suma))
        suma += number1
        cont1 += 1

    return suma
