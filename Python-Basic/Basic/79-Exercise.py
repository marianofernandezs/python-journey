age = int(input("Ingrese su edad: "))

if age > 18:
    print("Eres mayor de edad")
elif age < 18 and age > 0:
    print("Es menor de edad")
else:
    print("El numero ingresado es negativo")
