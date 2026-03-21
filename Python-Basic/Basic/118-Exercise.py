
def division (dividen, divisor):
    result = int
    try:
        result = dividen // divisor
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero. ")

    return print(f"The result is {result}")

number_one = int(input("Enter your dividen: "))
number_two = int(input("Enter your divisor: "))

div = division(number_one, number_two)
