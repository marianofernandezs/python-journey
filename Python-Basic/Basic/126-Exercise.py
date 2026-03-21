def convert_to_int (lista):
    nueva = []
    try:
        for elements in lista:
            elements = int(elements)
            nueva.append(elements)
        return print(f"La lista quedo de la siguiente manera {nueva}")
    except ValueError:
        return print("Error al convertir a numero entero")
    except TypeError:
        return print("Solo se soporta numeros como string")

user_input = str(input("Ingresa tus valores: "))

x = user_input.split(",")


convert_to_int(x)
