"""Temperature function"""


def farkel_to_cel(temp, farorkel):
    """Fahrenheit or Kelvin temperature to Celcius degrees transformation"""
    while farorkel not in ("K", "F"):
        farorkel = input("Error. Enter 'F' or 'K': ")
        if farorkel == "K":
            celcius = temp - 273.15
            print(f"{temp} Kelvin are {celcius}° Celcius")
        if farorkel == "F":
            celcius = 5*(temp-32)/9
            print(f"{temp}° Fahrenheit are {celcius}° Celcius")
