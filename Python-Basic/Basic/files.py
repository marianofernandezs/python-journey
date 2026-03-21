
def read_file ():
    archive = open("my.txt", "r")
    content = archive.read()
    archive.close()
    return print(f"Se ha leido el contenido del archivo y este se ha cerrado {content}")

def write_file (message): 
    archive = open("my.txt", "w")
    archive.write(message)
    archive.close
    return print(f"Se ha escrito lo ingresado por el usuario {message}")
