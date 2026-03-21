def calculate (num):
    try:
        if(num < 0):
            raise ValueError
            
        result = num ** 0.5

        return print(f"El resultado de tu raiz cuadrada es {result}")
    except ValueError:
            return print("La raiz cuadrada no puede ser negativa")
            

user_input = int(input("Ingresa tu numero: "))


calculate(user_input)
