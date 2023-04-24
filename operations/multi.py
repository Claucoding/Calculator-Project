"""Multiplication function"""


def multi(cantidad_numeros, cont1):
    """Multiplication"""
    multipli = 1
    while cont1 <= cantidad_numeros:
        frase_multi = f"""Enter variable {cont1}: """
        n2 = float(input(frase_multi))
        multipli *= n2
        cont1 += 1
    return multipli
