
def index (index_input):
    lista = [1,2,4,5,6,7]
    try:
        index_input = lista [index_input]
        return print(f"El indice fue encontrado en la lista {index_input}")
    except IndexError:
        return print("Error el indice ingresado no existe ")


user_input = int(input("Ingresa el indice para encontrar el elemento en la lista: "))


call = index(user_input)
