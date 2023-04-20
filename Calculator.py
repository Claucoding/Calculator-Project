# Basic operations calculator
from Operations import sum
import math as m


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
        cantidad_numeros2 = int(
            input("Enter the quantitie of variables: "))
        cont2 = 1
        multi = 1
        while cont2 <= cantidad_numeros2:
            frase_multi = f"""Enter variable {cont2}: """
            n2 = float(input(frase_multi))
            multi *= n2
            cont2 += 1
        print("The total multiplication is: ", multi)
    # Divide
    if operacion == 3:
        numerador = float(input("Enter the numerator: "))
        denominador = float(input("Ingrese The denominator: "))
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
    # Hypotenuse
    if operacion == 4:
        cateto1 = float(input("Enter the adjacent cathetus: "))
        cateto2 = float(input("Ingrese el valor del opposite cathetus: "))
        Hipotenusa = m.sqrt(m.pow(cateto1, 2) + m.pow(cateto2, 2))
        print("The hypotenuse is:", Hipotenusa)
    # Degree to radians
    if operacion == 5:
        grados = float(input("Enter the degrees: "))
        radianes = (grados * m.pi)/180
        print(f"{grados}° are {radianes} radians")
    # Inch to centimeters
    if operacion == 6:
        pulgadas = float(input("Enter the number of inches: "))
        centimetros = (pulgadas*2.54)
        print(f"{pulgadas} inch are {centimetros} centimeters")
    # Pounds to kilos
    if operacion == 7:
        pounds = float(input("Enter the pounds: "))
        kilos = (pounds*0.453592)
        print(f"{pounds} pound are {kilos} kilos")
    # Fahrenheit or Kelvin to Celcius
    if operacion == 8:
        temp = float(input("Enter the temperature: "))
        farorkel = input(
            "Enter 'F' or 'K' if you want to convert Fahrenheit (F) or Kelvin (K) to Celcius: ")
        while farorkel not in ("K", "F"):
            farorkel = input("Error. Enter 'F' or 'K': ")
        if farorkel == "K":
            celcius = temp - 273.15
            print(f"{temp} Kelvin are {celcius}° Celcius")
        if farorkel == "F":
            celcius = 5*(temp-32)/9
            print(f"{temp}° Fahrenheit are {celcius}° Celcius")

    # Infinite cycle's continuity
    continuar = input(
        "Do you want to do another operation? yes/no: ")
    while continuar != "yes" and continuar != "no":
        continuar = input(
            "ERROR. Enter yes or no: ")
    if continuar == "no":
        print("Closing Calculator ...")
        break
