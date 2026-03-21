def convert_to_number (my_string):
    try:
        my_string = int(my_string)
    except ValueError:
        print("No se pudo convertir el string a numero")
    return print(my_string)


while True:
    try:
        string = str(input("Ingrese un string: "))
        convert_to_number(string)
        break
    except ValueError:
        print("Se espera un string")
