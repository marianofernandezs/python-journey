def greets (func, name):
    return func(name)

def salute (val):
    return "Hola, " + val

print(greets(salute,"Mariano"))
