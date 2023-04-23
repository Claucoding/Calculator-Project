# Basic operations calculator
from Operations import *


# Presentation message
Mensaje_inicial = "Simple calculator with the following operations available: \n"
Fila_Operaciones = """1. Sum of integers numbers
 2. Multiplication
 3. Divide
 4. Hypotenuse
 5. Degrees to radians
 6. Inch to centimeters
 7. Pounds to kilos
 8. Fahrenheit or Kelvin to Celcius  \n"""
print(Mensaje_inicial, Fila_Operaciones)

# Infinite operation cycle
continuar = ""
while continuar != "no":
    operacion = int(input("Enter the operation's number to perform: "))

    # Addition and subtraction
    if operacion == 1:
        Total_sum = sum(
            int(input("Enter the quantitie of variables: ")), 1)
        print("The total sum is:", Total_sum)

    # Multiplication
    if operacion == 2:
        Total_multi = multi(
            int(input("Enter the quantitie of variables: ")), 1)
        print("The total multiplication is: ", Total_multi)

    # Divide
    if operacion == 3:
        div(float(input("Enter a numerator: ")),
            float(input("Enter a denominator: ")))

    # Hypotenuse
    if operacion == 4:
        hipotenusa = hypotenuse(float(input("Enter the adjacent cathetus: ")), float(
            input("Ingrese el valor del opposite cathetus: ")))
        print("The hypotenuse is:", hipotenusa)

    # Degree to radians
    if operacion == 5:
        degtorad(float(input("Enter the degrees: ")))

    # Inch to centimeters
    if operacion == 6:
        inchtocent(float(input("Enter the number of inches: ")))

    # Pounds to kilos
    if operacion == 7:
        poundtokilos(float(input("Enter the pounds: ")))

    # Fahrenheit or Kelvin to Celcius
    if operacion == 8:
        farkeltocel(float(input("Enter the temperature: ")),
                    input(
            "Enter 'F' or 'K' if you want to convert Fahrenheit (F) or Kelvin (K) to Celcius: "))

    # Infinite cycle's continuity
    continuar = input(
        "Do you want to do another operation? yes/no: ")
    while continuar != "yes" and continuar != "no":
        continuar = input(
            "ERROR. Enter yes or no: ")
    if continuar == "no":
        print("Closing Calculator ...")
        break
