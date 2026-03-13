mi_edad = int(input("ingresa tu edad: "))

if mi_edad >= 18:
    print("Puedes votar")
elif mi_edad > 15:
    print("Puedes votar con permiso especial")
else:
    print("No puedes votar")
