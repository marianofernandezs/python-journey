# Leer archivo linea por linea y mostrar solo lo que contenga Python

file = open("hola.txt", "r")

for i in file:
    if i.count("Python"):
        print(i.strip())
    else:
        print("Nada")
