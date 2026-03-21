

def handle_error ():
    while True:
        try:
            number_one = int(input("Ingrese un numero : "))
            number_two = int(input("Ingresa un numero : "))
            break;
        except ValueError:
            print("Tienen que ser numeros enteros")
        except TypeError:
            print("No puede ser un float o un string")
    try:
        result = number_one // number_two
        return print(f"El resultado es {result} ")
    except ZeroDivisionError:
        print("Error no se puede dividir entre cero")


handle_error()
