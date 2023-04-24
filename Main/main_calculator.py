"""Basic operations  calculator"""

import operations as o

# Presentation message
MENSAJE_INICIAL = "Simple calculator with the following operations available: \n"
FILA_OPERACIONES = """1. Sum of integers numbers
 2. Multiplication
 3. Divide
 4. Hypotenuse
 5. Degrees to radians
 6. Inch to centimeters
 7. Pounds to kilos
 8. Fahrenheit or Kelvin to Celcius  \n"""
print(MENSAJE_INICIAL, FILA_OPERACIONES)

# Infinite operation cycle
CONTINUE = ""
while CONTINUE != "no":
    operacion = int(input("Enter the operation's number to perform: "))

    # Integer sum
    if operacion == 1:
        Total_sum = o.integer_sum(
            int(input("Enter the quantitie of variables: ")), 1)
        print("The total sum is:", Total_sum)

    # Multiplication
    if operacion == 2:
        Total_multi = o.multi(
            int(input("Enter the quantitie of variables: ")), 1)
        print("The total multiplication is: ", Total_multi)

    # Divide
    if operacion == 3:
        o.div(float(input("Enter a numerator: ")),
              float(input("Enter a denominator: ")))

    # Hypotenuse
    if operacion == 4:
        hipotenusa = o.hypotenuse(float(input("Enter the adjacent cathetus: ")), float(
            input("Ingrese el valor del opposite cathetus: ")))
        print("The hypotenuse is:", hipotenusa)

    # Degree to radians
    if operacion == 5:
        o.deg_to_rad(float(input("Enter the degrees: ")))

    # Inch to centimeters
    if operacion == 6:
        o.inch_to_cent(float(input("Enter the number of inches: ")))

    # Pounds to kilos
    if operacion == 7:
        o.pound_to_kilos(float(input("Enter the pounds: ")))

    # Fahrenheit or Kelvin to Celcius
    if operacion == 8:
        o.farkel_to_cel(float(input("Enter the temperature: ")),
                        input(
            "Enter 'F' or 'K' if you want to convert Fahrenheit (F) or Kelvin (K) to Celcius: "))

    # Infinite cycle's continuity
    CONTINUE = input(
        "Do you want to do another operation? yes/no: ")
    while CONTINUE != "yes" and CONTINUE != "no":
        CONTINUE = input(
            "ERROR. Enter yes or no: ")
    if CONTINUE == "no":
        print("Closing Calculator ...")
        break
