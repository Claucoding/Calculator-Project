"""Division function"""


def div(numerador, denominador):
    """Division"""
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
