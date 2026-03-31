# Crea un archivo de texto
file_txt = open("hola.txt","w+")
file_txt.write("Hola desde Python")

# Abrir un archivo y lee todo el contenido

file_txt = open("hola.txt", "r+")
file_content =file_txt.read()
print(file_content)



# Agregar una nueva linea al final del archivo
file_txt = open("hola.txt","a")
file_txt.write("\nLinea nueva")

#Leer los 10 caracteres del archivo

file_txt = open("hola.txt", "r")
print(file_txt.read(10))

# Uso de seek

file_txt = open("hola.txt", "r")
file_txt.seek(0)
print(file_txt.read())

# Lee e imprime el contenido linea por linea

file_txt = open("hola.txt", "r")
file_txt.seek(0)
for i in file_txt:
    print(i.strip())

#Sobreescribir a un archivo

file_txt = open("hola.txt", "w")
file_boilepart = file_txt.write("Hola esto es el nuevo texto \nAdemas es muy cool")
file_txt.close()

# Usar la función para abrir un archivo utilizando with

with open("hola.txt", "w+") as f:
    f.write("Esto es nuevo en Python")
    f.close()

with open("hola.txt", "r") as f:
    print(f.read())

# Leer archivo linea por linea y mostrar solo lo que contenga Python

file = open("hola.txt", "r")

for i in file:
    i.strip()
    if i.count("Python") > 0 :
        print(file.readline())
    else:
        print("Nada")
