
def sum (number_one, number_two):
    result = number_one + number_two
    return print(f"El resultado de la suma es {result}")

def res (number_one, number_two):
    result = number_one - number_two
    return print(f"El resultado de la resta es {result}")

def multiply (number_one, number_two):
    result = number_one * number_two
    return print(f"El resultado de la multiplicacion es {result}")

def division (number_one, number_two):
    try:
        result = number_one // number_two
        return print(f"El resultado es {result}")
    except ZeroDivisionError:
        return print("No se puede dividr entre 0")
