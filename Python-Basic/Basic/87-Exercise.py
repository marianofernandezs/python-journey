mi_color = str(input("Ingresa un color: "))

mi_color = mi_color.lower()

if mi_color == "verde":
    print("Puede Avanzar")
elif mi_color == "amarillo":
    print("Debe estar alerta")
elif mi_color == "rojo":
    print("Debe detenerse")
else:
    print("Color invalido para el semaforo")
