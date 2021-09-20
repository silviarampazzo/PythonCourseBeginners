c = int(input("type temperature in celsius"))


def fahrenheit(celsius):
    return round(1.8 * celsius + 32, 2)


print("The Fahrenheit equivalent of " + str(c) + " degrees Celsius is " + str(fahrenheit(c)))