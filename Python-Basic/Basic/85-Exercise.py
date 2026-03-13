password = "admin"

user_password = str(input("Ingrese su password: "))

if user_password == password:
    print("Acceso Garantizado")
else:
    print("Acceso Denegado")
